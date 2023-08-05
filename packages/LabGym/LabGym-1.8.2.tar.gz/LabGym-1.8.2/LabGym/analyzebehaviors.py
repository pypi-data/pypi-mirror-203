'''
Copyright (C)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)#fulltext. 

For license issues, please contact:

Dr. Bing Ye
Life Sciences Institute
University of Michigan
210 Washtenaw Avenue, Room 5403
Ann Arbor, MI 48109-2216
USA

Email: bingye@umich.edu
'''



from .tools import *
from .tracker import TrackAnimals
import os
import gc
import cv2
import datetime
import moviepy.editor as mv
import numpy as np
import math
from collections import OrderedDict,deque
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from matplotlib.colors import LinearSegmentedColormap,Normalize
from matplotlib.colorbar import ColorbarBase
import pandas as pd
import seaborn as sb


TA=TrackAnimals()


class AnalyzeAnimal():

	def __init__(self):

		self.path_to_video=None
		self.basename=None
		self.fps=None
		self.framewidth=None
		self.kernel=None
		self.results_path=None
		self.analyze=None
		self.delta=None
		self.animal_number=None
		self.auto=1
		self.t=0
		self.duration=5
		self.length=None
		self.animal_area=None
		self.invert=None
		self.background=None
		self.background_low=None
		self.background_high=None
		self.model=None
		self.batch_size=32
		self.detector_batch=100
		self.skipped_frames=[]
		self.all_time=[]
		self.register_counts=OrderedDict()
		self.animal_inners=OrderedDict()
		self.animal_contours=OrderedDict()
		self.animal_centers=OrderedDict()
		self.animal_angles=OrderedDict()
		self.animal_heights=OrderedDict()
		self.animal_blobs=OrderedDict()
		self.animations=OrderedDict()
		self.pattern_images=OrderedDict()
		self.event_probability=OrderedDict()
		self.all_behavior_parameters=OrderedDict()
		

	def prepare_analysis(self,path_to_video,results_path,animal_number,delta=1.2,names_and_colors=None,framewidth=None,minimum=0,analyze=0,path_background=None,auto=1,t=0,duration=5,ex_start=0,ex_end=None,length=15,invert=0,dynamic=0):

		# delta: an estimated fold change (1.2) of the light intensity for optogenetics only
		# names_and_colors: the behavior names and their representing colors
		# framewidth: the width of the frame to resize
		# minimum: 0: use minimum or maximum pixel value for background extraction
		# analyze: if not 0, track animals without analyzing behaviors
		# path_background: if not None, load backgrounds (need to put the background images under the name 'background.jpg', 'background_low.jpg' and 'background_high.jpg' in the 'path_background' path)
		# auto: 0: optogenetic stimulation onset as start_t; 1: t
		# t: if auto is else, t is the start_t
		# duration: the duration for data generation / analysis
		# ex_start: the start time point for background extraction
		# ex_end: the end time point for background extraction, if None, use the entire video
		# length: the number of input frames for assessing the behavior
		# invert: 0: animals brighter than the background; 1: invert the pixel value (for animals darker than the background); 2: use absdiff
		# dynamic: if not 0, using Detectors
		
		print('Processing video...')
		print(datetime.datetime.now())

		self.path_to_video=path_to_video
		self.basename=os.path.basename(self.path_to_video)
		self.fps=mv.VideoFileClip(self.path_to_video).fps
		self.framewidth=framewidth
		self.results_path=os.path.join(results_path,os.path.splitext(self.basename)[0])
		self.animal_number=animal_number
		self.analyze=analyze
		self.t=t
		self.duration=duration
		self.length=length

		capture=cv2.VideoCapture(self.path_to_video)
		while True:
			retval,frame=capture.read()
			break
		capture.release()

		print('The original video framesize: '+str(frame.shape[1])+' X '+str(frame.shape[0]))
		print('Video fps: '+str(self.fps))

		if self.analyze==0:

			behavior_names=list(names_and_colors.keys())

			for behavior_name in behavior_names:
				self.all_behavior_parameters[behavior_name]=OrderedDict()
				self.all_behavior_parameters[behavior_name]['color']=names_and_colors[behavior_name]
				
				for parameter_name in ['acceleration','angle','count','distance','duration','intensity_area','intensity_length','latency','magnitude_area','magnitude_length','probability','speed','velocity','vigor_area','vigor_length']:
					self.all_behavior_parameters[behavior_name][parameter_name]=OrderedDict()

		else:

			for parameter_name in ['acceleration','angle','distance','intensity_area','intensity_length','magnitude_area','magnitude_length','speed','velocity','vigor_area','vigor_length']:
				self.all_behavior_parameters[parameter_name]=OrderedDict()

		if not os.path.isdir(self.results_path):
			os.mkdir(self.results_path)
			print('Folder created: '+str(self.results_path))
		else:
			print('Folder already exists: '+str(self.results_path))

		if dynamic==0:

			self.delta=delta
			self.auto=auto
			self.invert=invert

			if self.auto==0:
				es_start=None
			else:
				es_start=self.t

			constants=estimate_constants(self.path_to_video,self.delta,self.animal_number,framewidth=self.framewidth,minimum=minimum,ex_start=ex_start,ex_end=ex_end,t=es_start,duration=self.duration,invert=self.invert,path_background=path_background)

			self.animal_area=constants[4]
			self.kernel=constants[5]
			self.background=constants[0]
			self.background_low=constants[1]
			self.background_high=constants[2]
			cv2.imwrite(os.path.join(self.results_path,'background.jpg'),constants[0])
			cv2.imwrite(os.path.join(self.results_path,'background_low.jpg'),constants[1])
			cv2.imwrite(os.path.join(self.results_path,'background_high.jpg'),constants[2])

			if self.auto==0:
				self.t=constants[3]

		print('Video processing completed!')


	def acquire_parameters(self,deregister=1,dim_tconv=32,dim_conv=64,channel=1,categorizer_type=2,inner_code=0,std=0,background_free=0):

		# deregister: 0: link new animal to deregistered animal, otherwise never re-link if an animal is deregistered
		# dim_tconv: dimension of animation, used in Categorizer
		# dim_conv: dimension of pattern image, used in Categorizer
		# channel: for Animation Analyzer, 1: gray scale
		# categorizer_type: 0: use Pattern Recognizer; 1: Animation Analyzer; 2: combined
		# inner_code: 0: include inner contours of animal body parts in pattern images
		# std: std for excluding static pixels in inners
		# background_free: 0: do not include background in blobs

		print('Acquiring information in each frame...')
		print(datetime.datetime.now())

		background=self.background
		background_low=self.background_low
		background_high=self.background_high
		
		if self.invert==1:
			background=np.uint8(255-background)
			background_low=np.uint8(255-background_low)
			background_high=np.uint8(255-background_high)

		capture=cv2.VideoCapture(self.path_to_video)

		frame_count=0
		frame_count_analyze=0
		temp_frames=deque(maxlen=self.length)

		start_t=round((self.t-self.length/self.fps),2)
		if start_t<0:
			start_t=0.00
		if self.duration==0:
			end_t=float('inf')
		else:
			end_t=start_t+self.duration

		while True:

			retval,frame=capture.read()
			time=round((frame_count+1)/self.fps,2)

			if time>=end_t:
				break
			if frame is None:
				break

			if time>=start_t:

				self.all_time.append(round((time-start_t),2))
				lost_track=0
				
				if (frame_count_analyze+1)%1000==0:
					print(str(frame_count_analyze+1)+' frames analyzed...')
					print(datetime.datetime.now())

				if self.framewidth is not None:
					frame=cv2.resize(frame,(self.framewidth,int(frame.shape[0]*self.framewidth/frame.shape[1])),interpolation=cv2.INTER_AREA)

				(contours,inners)=contour_frame(frame,self.animal_number,background,background_low,background_high,self.delta,self.animal_area,invert=self.invert,inner_code=inner_code,kernel=self.kernel)

				if len(contours)==0:

					self.skipped_frames.append(frame_count_analyze)

					if len(TA.centers)>0:
						lost_track+=1
						for n in list(TA.centers.keys()):
							if lost_track>2*self.fps:
								TA.centers[n].append((-10000,-10000))
							else:
								TA.centers[n].append(TA.centers[n][-1])
							TA.contours[n].append(TA.contours[n][-1])
							TA.angles[n].append(-10000)
							TA.heights[n].append(-10000)
							if inner_code==0:
								TA.factors1[n].append(TA.factors1[n][-1])
							if categorizer_type!=0:
								if background_free==0:
									self.animal_blobs[n].append(np.zeros((dim_tconv,dim_tconv,channel),dtype='uint8'))
								self.animations[n].append(np.zeros((self.length,dim_tconv,dim_tconv,channel),dtype='uint8'))
							if categorizer_type!=1:
								self.pattern_images[n].append(np.zeros((dim_conv,dim_conv,3),dtype='uint8'))

				else:

					lost_track=0

					if background_free!=0:
						temp_frames.append(frame)

					(new_contours,centers,angles,heights)=get_parameters(frame,contours)

					if len(TA.centers)==0:

						frame_count_from_initial=len(self.skipped_frames)

						n=0
						while n<len(centers):
							if inner_code==0:
								factor1=inners[n]
							else:
								factor1=None
							TA.register_animal(n,contours[n],centers[n],angles[n],heights[n],factor1=factor1)
							n+=1

						for n in list(TA.centers.keys()):
							self.register_counts[n]=frame_count_from_initial
							if categorizer_type!=0:
								if background_free==0:
									self.animal_blobs[n]=deque(maxlen=self.length)
									blob=extract_blob(frame,TA.contours[n][0],channel=channel)
									self.animal_blobs[n].append(img_to_array(cv2.resize(blob,(dim_tconv,dim_tconv),interpolation=cv2.INTER_AREA)))
								self.animations[n]=deque()
								self.animations[n].append(np.zeros((self.length,dim_tconv,dim_tconv,channel),dtype='uint8'))
							if categorizer_type!=1:
								self.pattern_images[n]=deque()
								self.pattern_images[n].append(np.zeros((dim_conv,dim_conv,3),dtype='uint8'))						

					else:

						max_distance=math.sqrt(self.animal_area)*2

						if inner_code==0:
							factors1=inners
						else:
							factors1=None
							
						TA.track_animal(self.fps,max_distance,contours,centers,angles,heights,deregister=deregister,factors1=factors1)
							
						if categorizer_type!=0:

							for n in list(self.animations.keys()):
								if len(self.animations[n])<self.length:
									if background_free==0:
										if TA.angles[n][-1]==-10000:
											self.animal_blobs[n].append(np.zeros((dim_tconv,dim_tconv,channel),dtype='uint8'))
										else:
											blob=extract_blob(frame,TA.contours[n][-1],channel=channel)
											self.animal_blobs[n].append(img_to_array(cv2.resize(blob,(dim_tconv,dim_tconv),interpolation=cv2.INTER_AREA)))
									self.animations[n].append(np.zeros((self.length,dim_tconv,dim_tconv,channel),dtype='uint8'))
								else:
									(y_bt,y_tp,x_lf,x_rt)=crop_frame(frame,TA.contours[n][-self.length:])
									if background_free==0:
										if TA.angles[n][-1]==-10000:
											self.animal_blobs[n].append(np.zeros((dim_tconv,dim_tconv,channel),dtype='uint8'))
										else:
											blob=extract_blob(frame,TA.contours[n][-1],channel=channel)
											self.animal_blobs[n].append(img_to_array(cv2.resize(blob,(dim_tconv,dim_tconv),interpolation=cv2.INTER_AREA)))
										self.animations[n].append(np.array(self.animal_blobs[n]))
									else:
										i=0
										animation=deque(maxlen=self.length)
										while i<self.length:
											if TA.angles[n][-self.length:][i]==-10000:
												blob=np.zeros((dim_tconv,dim_tconv,channel),dtype='uint8')
											else:
												if i>=len(temp_frames):
													blob=np.zeros((dim_tconv,dim_tconv,channel),dtype='uint8')
												else:
													blob=extract_blob(temp_frames[i],TA.contours[n][-self.length:][i],y_bt=y_bt,y_tp=y_tp,x_lf=x_lf,x_rt=x_rt,background_free=1,channel=channel)	
													blob=cv2.resize(blob,(dim_tconv,dim_tconv),interpolation=cv2.INTER_AREA)
											animation.append(img_to_array(blob))
											i+=1
										self.animations[n].append(np.array(animation))

							if len(TA.centers)>len(self.animations):
								frame_count_from_initial=self.register_counts[0]+len(self.animations[0])-1
								for n in list(TA.centers.keys()):
									if n not in list(self.animations.keys()):
										self.register_counts[n]=frame_count_from_initial
										if background_free==0:
											self.animal_blobs[n]=deque(maxlen=self.length)
											blob=extract_blob(frame,TA.contours[n][0],channel=channel)
											self.animal_blobs[n].append(img_to_array(cv2.resize(blob,(dim_tconv,dim_tconv),interpolation=cv2.INTER_AREA)))
										self.animations[n]=deque()
										self.animations[n].append(np.zeros((self.length,dim_tconv,dim_tconv,channel),dtype='uint8'))	

						if categorizer_type!=1:

							for n in list(self.pattern_images.keys()):
								if len(self.pattern_images[n])<self.length:
									self.pattern_images[n].append(np.zeros((dim_conv,dim_conv,3),dtype='uint8'))
								else:
									(y_bt,y_tp,x_lf,x_rt)=crop_frame(frame,TA.contours[n][-self.length:])
									if inner_code==0:
										pattern_image=concatenate_blobs(frame,TA.contours[n][-self.length:],y_bt=y_bt,y_tp=y_tp,x_lf=x_lf,x_rt=x_rt,inners=TA.factors1[n][-self.length:],std=std)
									else:
										pattern_image=concatenate_blobs(frame,TA.contours[n][-self.length:],y_bt=y_bt,y_tp=y_tp,x_lf=x_lf,x_rt=x_rt,inners=None,std=0)
									pattern_image=cv2.resize(pattern_image,(dim_conv,dim_conv),interpolation=cv2.INTER_AREA)
									self.pattern_images[n].append(np.array(pattern_image))

							if len(TA.centers)>len(self.pattern_images):
								frame_count_from_initial=self.register_counts[0]+len(self.pattern_images[0])-1
								for n in list(TA.centers.keys()):
									if n not in list(self.pattern_images.keys()):
										self.register_counts[n]=frame_count_from_initial
										self.pattern_images[n]=deque()
										self.pattern_images[n].append(np.zeros((dim_conv,dim_conv,3),dtype='uint8'))

				frame_count_analyze+=1

			frame_count+=1

		capture.release()

		self.animal_centers=TA.centers
		self.animal_contours=TA.contours
		self.animal_angles=TA.angles
		self.animal_heights=TA.heights
		if inner_code==0:
			self.animal_inners=TA.factors1

		TA.clear_tracker()

		'''
		dim=max(dim_tconv,dim_conv)
		if dim<=64:
			self.batch_size=3000
		elif dim<=128:
			self.batch_size=1000
		elif dim<=256:
			self.batch_size=200
		else:
			self.batch_size=32
		'''

		print('Information acquisition completed!')


	def categorize_behaviors(self,path_to_categorizer,categorizer_type=2,uncertain=0):

		# uncertain: the differece between the highest probability and second highest probability to output 'NA' when categorize the behaviors

		print('Categorizing animal behaviors...')
		print(datetime.datetime.now())

		if categorizer_type!=0:
			animations=self.animations[0]
		if categorizer_type!=1:
			pattern_images=self.pattern_images[0]

		if len(self.animal_centers)>1:
			for n in list(self.animal_centers.keys()):
				if n>0:
					if categorizer_type!=0:
						animations+=self.animations[n]
					if categorizer_type!=1:
						pattern_images+=self.pattern_images[n]

		del self.animations
		del self.pattern_images
		gc.collect()

		if categorizer_type==0:
			inputs=np.array(pattern_images,dtype='float32')/255.0
		elif categorizer_type==1:
			inputs=np.array(animations,dtype='float32')/255.0
		else:
			inputs=[np.array(animations,dtype='float32')/255.0,np.array(pattern_images,dtype='float32')/255.0]

		categorizer=load_model(path_to_categorizer)
		predictions=categorizer.predict(inputs,batch_size=self.batch_size)

		behavior_names=list(self.all_behavior_parameters.keys())
		for behavior_name in behavior_names:
			for i in list(self.animal_centers.keys()):
				self.all_behavior_parameters[behavior_name]['probability'][i]=[-1]*len(self.all_time)
				self.event_probability[i]=[['NA',-1]]*len(self.all_time)

		idx=0
		for n in list(self.animal_centers.keys()):
			i=self.length+self.register_counts[n]
			idx+=i
			skipped_frames=self.skipped_frames[self.register_counts[n]:]
			while i<len(self.animal_centers[n]):				
				if self.animal_angles[n][i]!=-10000:
					check=0
					for a in self.animal_angles[n][i-self.length:i]:
						if a==-10000:
							check+=1
					if check<=self.length/2:
						prediction=predictions[idx]
						for behavior_name in behavior_names:
							if len(behavior_names)==2:
								if behavior_names.index(behavior_name)==0:
									probability=1-prediction[0]
								else:
									probability=prediction[0]
							else:
								probability=prediction[behavior_names.index(behavior_name)]
							self.all_behavior_parameters[behavior_name]['probability'][n][i]=probability
						if len(behavior_names)==2:
							if prediction[0]>0.5:
								if prediction[0]-(1-prediction[0])>uncertain:
									self.event_probability[n][i]=[behavior_names[1],prediction[0]]
							if prediction[0]<0.5:
								if (1-prediction[0])-prediction[0]>uncertain:
									self.event_probability[n][i]=[behavior_names[0],1-prediction[0]]
						else:
							if sorted(prediction)[-1]-sorted(prediction)[-2]>uncertain:
								self.event_probability[n][i]=[behavior_names[np.argmax(prediction)],max(prediction)]
				
				idx+=1
				i+=1

		del predictions
		gc.collect()

		print('Behavioral categorization completed!')


	def generate_data(self,deregister=1,inner_code=0,std=0,background_free=0,skip_redundant=1):

		# skip_redundant: number of overlapped frames to skip
		
		print('Generating behavior examples...')
		print(datetime.datetime.now())

		background=self.background
		background_low=self.background_low
		background_high=self.background_high
		
		if self.invert==1:
			background=np.uint8(255-background)
			background_low=np.uint8(255-background_low)
			background_high=np.uint8(255-background_high)

		capture=cv2.VideoCapture(self.path_to_video)

		frame_count=0
		temp_frames=deque(maxlen=self.length)

		start_t=round((self.t-self.length/self.fps),2)
		if start_t<0:
			start_t=0.00
		if self.duration==0:
			end_t=float('inf')
		else:
			end_t=start_t+self.duration

		while True:

			retval,frame=capture.read()
			time=round((frame_count+1)/self.fps,2)

			if time>=end_t:
				break
			if frame is None:
				break

			if time>=start_t:

				if self.framewidth is not None:
					frame=cv2.resize(frame,(self.framewidth,int(frame.shape[0]*self.framewidth/frame.shape[1])),interpolation=cv2.INTER_AREA)

				(contours,inners)=contour_frame(frame,self.animal_number,background,background_low,background_high,self.delta,self.animal_area,invert=self.invert,inner_code=inner_code,kernel=self.kernel)

				if len(contours)>0:

					temp_frames.append(frame)

					(new_contours,centers,angles,heights)=get_parameters(frame,contours)

					if len(TA.centers)==0:

						n=0
						while n<len(centers):
							if inner_code==0:
								factor1=inners[n]
							else:
								factor1=None
							TA.register_animal(n,contours[n],centers[n],angles[n],heights[n],factor1=factor1)
							n+=1

						for n in list(TA.centers.keys()):
							individual_path=os.path.join(self.results_path,str(n))
							if not os.path.isdir(individual_path):
								os.mkdir(individual_path)

					else:

						max_distance=math.sqrt(self.animal_area)*2

						if inner_code==0:
							factors1=inners
						else:
							factors1=None
							
						TA.track_animal(self.fps,max_distance,contours,centers,angles,heights,deregister=deregister,factors1=factors1)

						for n in list(TA.centers.keys()):
							individual_path=os.path.join(self.results_path,str(n))
							if not os.path.isdir(individual_path):
								os.mkdir(individual_path)

						if len(TA.centers[0])%skip_redundant==0:

							for n in list(TA.centers.keys()):

								if len(TA.centers[n])>self.length:

									(y_bt,y_tp,x_lf,x_rt)=crop_frame(frame,TA.contours[n][-self.length:])
									
									if inner_code==0:
										animation_name=os.path.splitext(self.basename)[0]+'_'+str(n)+'_'+str(frame_count)+'_std'+str(std)+'.avi'
									else:
										animation_name=os.path.splitext(self.basename)[0]+'_'+str(n)+'_'+str(frame_count)+'.avi'
									path_animation=os.path.join(self.results_path,str(n),animation_name)
									h=y_tp-y_bt
									w=x_rt-x_lf
									writer=cv2.VideoWriter(path_animation,cv2.VideoWriter_fourcc(*'MJPG'),self.fps/5,(w,h),True)

									i=0
									while i<self.length:
										if TA.angles[n][-self.length:][i]==-10000:
											blob=np.zeros_like(frame)[y_bt:y_tp,x_lf:x_rt]
										else:
											if i>=len(temp_frames):
												blob=np.zeros_like(frame)[y_bt:y_tp,x_lf:x_rt]
											else:
												blob=extract_blob(temp_frames[i],TA.contours[n][-self.length:][i],y_bt=y_bt,y_tp=y_tp,x_lf=x_lf,x_rt=x_rt,analyze=1,background_free=background_free,channel=frame.shape[2])
										writer.write(blob)
										i+=1
									writer.release()

									if inner_code==0:
										pattern_image_name=os.path.splitext(self.basename)[0]+'_'+str(n)+'_'+str(frame_count)+'_std'+str(std)+'.jpg'
									else:
										pattern_image_name=os.path.splitext(self.basename)[0]+'_'+str(n)+'_'+str(frame_count)+'.jpg'
									path_pattern_image=os.path.join(self.results_path,str(n),pattern_image_name)
									if inner_code==0:
										pattern_image=concatenate_blobs(frame,TA.contours[n][-self.length:],y_bt=y_bt,y_tp=y_tp,x_lf=x_lf,x_rt=x_rt,inners=TA.factors1[n][-self.length:],std=std)
									else:
										pattern_image=concatenate_blobs(frame,TA.contours[n][-self.length:],y_bt=y_bt,y_tp=y_tp,x_lf=x_lf,x_rt=x_rt,inners=None,std=0)
									cv2.imwrite(path_pattern_image,pattern_image)

								n+=1
									
			frame_count+=1

		capture.release()
		TA.clear_tracker()

		print('Behavior example generation completed!')


	def craft_data(self):

		print('Crafting data...')
		print(datetime.datetime.now())

		to_delete=[]
		lengths=[]

		for i in list(self.animal_centers.keys()):
			
			if len(self.animal_centers[i])<len(self.all_time)*3/4:
				to_delete.append(i)
				lengths.append(len(self.animal_centers[i]))
			else:
				check=0
				for x in self.animal_angles[i]:
					if x==-10000:
						check+=1	
				if check>len(self.animal_centers[i])/4:
					to_delete.append(i)
					lengths.append(len(self.animal_centers[i]))

		if len(to_delete)==len(self.animal_centers):
			to_delete.remove(to_delete[np.argmax(lengths)])
		
		for i in to_delete:
			del self.register_counts[i]
			del self.animal_centers[i]
			del self.animal_contours[i]
			del self.animal_angles[i]
			del self.animal_heights[i]
			if self.analyze==0:
				if len(self.animations[i])>0:
					del self.animations[i]
				if len(self.pattern_images[i])>0:
					del self.pattern_images[i]

		for i in list(self.animal_centers.keys()):
			difference=self.register_counts[i]
			if difference>0:
				padding=[-10000]*difference
				self.animal_angles[i]=padding+self.animal_angles[i]
				self.animal_heights[i]=padding+self.animal_heights[i]
				padding=[(-10000,-10000)]*difference
				self.animal_centers[i]=padding+self.animal_centers[i]
				padding=[self.animal_contours[i][0]]*difference
				self.animal_contours[i]=padding+self.animal_contours[i]
				if self.analyze==0:
					if len(self.animations[i])>0:
						padding=deque([self.animations[i][0]])*difference
						self.animations[i]=padding+self.animations[i]
					if len(self.pattern_images[i])>0:
						padding=deque([self.pattern_images[i][0]])*difference
						self.pattern_images[i]=padding+self.pattern_images[i]

			if len(self.animal_centers[i])>len(self.all_time):
				difference=len(self.animal_centers[i])-len(self.all_time)
				self.animal_centers[i]=self.animal_centers[i][:-difference]
				self.animal_contours[i]=self.animal_contours[i][:-difference]
				self.animal_angles[i]=self.animal_angles[i][:-difference]
				self.animal_heights[i]=self.animal_heights[i][:-difference]
				if self.analyze==0:
					if len(self.animations[i])>0:
						self.animations[i]=self.animations[i][:-difference]
					if len(self.pattern_images[i])>0:
						self.pattern_images[i]=self.pattern_images[i][:-difference]

		print('Completed!')

			
	def annotate_video(self,to_include=None,show_legend=0):

		# to_include: the behaviors selected for annotation; None: just track animals
		# show_legend: 0: display the legends (all names in colors for behavioral categories) in the annotated video

		print('Annotating video...')
		print(datetime.datetime.now())

		text_scl=max(min(self.background.shape[0],self.background.shape[1])/750,0.5)
		text_tk=max(1,int(min(self.background.shape[0],self.background.shape[1])/1000))

		if self.analyze==0:
			colors={}
			for behavior_name in list(self.all_behavior_parameters.keys()):
				if self.all_behavior_parameters[behavior_name]['color'][1][0]!='#':
					colors[behavior_name]=(255,255,255)
				else:
					hex_color=self.all_behavior_parameters[behavior_name]['color'][1].lstrip('#')
					color=tuple(int(hex_color[i:i+2],16) for i in (0,2,4))
					colors[behavior_name]=color[::-1]
			
			if len(to_include)!=len(list(self.all_behavior_parameters.keys())):
				for behavior_name in list(self.all_behavior_parameters.keys()):
					if behavior_name not in to_include:
						del colors[behavior_name]
			
			if show_legend==0:	
				scl=min(self.background.shape[0],self.background.shape[1])/1500
				if 25*(len(list(colors.keys()))+1)<self.background.shape[0]:
					intvl=25
				else:
					intvl=int(self.background.shape[0]/(len(list(colors.keys()))+1))

		capture=cv2.VideoCapture(self.path_to_video)
		writer=None
		frame_count=0
		frame_count_analyze=0
		index=0

		start_t=round((self.t-self.length/self.fps),2)
		if start_t<0:
			start_t=0.00
		if self.duration==0:
			end_t=float('inf')
		else:
			end_t=start_t+self.duration

		while True:
			retval,frame=capture.read()
			time=round((frame_count+1)/self.fps,2)

			if time>=end_t:
				break
			if frame is None:
				break

			if time>=start_t:

				if self.framewidth is not None:
					frame=cv2.resize(frame,(self.framewidth,int(frame.shape[0]*self.framewidth/frame.shape[1])),interpolation=cv2.INTER_AREA)

				if self.analyze==0:
					if show_legend==0:
						n=1
						for i in list(colors.keys()):
							cv2.putText(frame,i,(10,intvl*n),cv2.FONT_HERSHEY_SIMPLEX,scl,colors[i],text_tk)
							n+=1

				if frame_count_analyze not in self.skipped_frames:

					for i in list(self.animal_centers.keys()):

						if frame_count_analyze<len(self.animal_centers[i]):

							if self.animal_angles[i][frame_count_analyze]!=-10000:
								cx=self.animal_centers[i][frame_count_analyze][0]
								cy=self.animal_centers[i][frame_count_analyze][1]
								cv2.putText(frame,str(i)+':',(cx-10,cy-10),cv2.FONT_HERSHEY_SIMPLEX,text_scl/2,(255,255,255),text_tk)
								cv2.circle(frame,(cx,cy),text_tk*4,(255,0,0),-1)

								if self.analyze==0:
									if self.event_probability[i][frame_count_analyze][0]=='NA':
										cv2.drawContours(frame,[self.animal_contours[i][frame_count_analyze]],0,(255,255,255),1)
										cv2.putText(frame,'NA',(cx+5,cy-10),
										cv2.FONT_HERSHEY_SIMPLEX,text_scl/2,(255,255,255),text_tk)
									else:
										name=self.event_probability[i][frame_count_analyze][0]
										probability=str(round(self.event_probability[i][frame_count_analyze][1]*100))+'%'
										if name in list(colors.keys()):
											color=colors[self.event_probability[i][frame_count_analyze][0]]
											cv2.drawContours(frame,[self.animal_contours[i][frame_count_analyze]],0,color,1)
											cv2.putText(frame,name+' '+probability,(cx+5,cy-10),cv2.FONT_HERSHEY_SIMPLEX,text_scl/2,color,text_tk)
										else:
											cv2.drawContours(frame,[self.animal_contours[i][frame_count_analyze]],0,(255,255,255),1)
											cv2.putText(frame,'NA',(cx+5,cy-10),cv2.FONT_HERSHEY_SIMPLEX,text_scl/2,(255,255,255),text_tk)
								else:
									cv2.drawContours(frame,[self.animal_contours[i][frame_count_analyze]],0,(255,255,255),1)

					index+=1

				if writer is None:
					(h,w)=frame.shape[:2]
					writer=cv2.VideoWriter(os.path.join(self.results_path,'Annotated video.avi'),cv2.VideoWriter_fourcc(*'MJPG'),self.fps,(w,h),True)

				writer.write(frame)

				frame_count_analyze+=1

			frame_count+=1

		capture.release()
		writer.release()

		print('Video annotation completed!')


	def analyze_parameters(self,normalize=0,included_parameters=[]):

		# normalize: 0: normalize the distance (in pixel) to the animal contour area

		all_parameters=[]
		if 'angle' in included_parameters:
			all_parameters.append('angle')
		if '3 length parameters' in included_parameters:
			all_parameters+=['intensity_length','magnitude_length','vigor_length']
		if '3 areal parameters' in included_parameters:
			all_parameters+=['intensity_area','magnitude_area','vigor_area']
		if '4 locomotion parameters' in included_parameters:
			all_parameters+=['acceleration','speed','velocity']

		if self.analyze==0:

			for behavior_name in list(self.all_behavior_parameters.keys()):

				for i in list(self.event_probability.keys()):
					if 'count' in included_parameters:
						self.all_behavior_parameters[behavior_name]['count'][i]=0
					if 'duration' in included_parameters:
						self.all_behavior_parameters[behavior_name]['duration'][i]=0.0
					if '4 locomotion parameters' in included_parameters:
						self.all_behavior_parameters[behavior_name]['distance'][i]=0.0
					if 'latency' in included_parameters:
						self.all_behavior_parameters[behavior_name]['latency'][i]='NA'
			
				for parameter_name in all_parameters:
					for i in list(self.event_probability.keys()):
						self.all_behavior_parameters[behavior_name][parameter_name][i]=[np.nan]*len(self.all_time)

		else:

			for i in list(self.animal_centers.keys()):
				if '4 locomotion parameters' in included_parameters:
					self.all_behavior_parameters['distance'][i]=0.0
				for parameter_name in all_parameters:
					self.all_behavior_parameters[parameter_name][i]=[np.nan]*len(self.all_time)
				
		if len(included_parameters)>0:

			for i in list(self.animal_centers.keys()):

				n=self.length+self.register_counts[i]
				skipped_frames=self.skipped_frames[self.register_counts[i]:]

				while n<len(self.animal_centers[i])-1:

					if self.analyze==0:

						behavior_name=self.event_probability[i][n][0]

						if behavior_name!='NA':

							if 'angle' in included_parameters:
								end_center=self.animal_centers[i][n]
								start_center=self.animal_centers[i][n-self.length]
								if end_center!=(-10000,-10000) and start_center!=(-10000,-10000):
									if end_center[0]-start_center[0]!=0:
										radius=np.arctan((end_center[1]-start_center[1])/(end_center[0]-start_center[0]))
										move_angle=math.degrees(radius)
									else:
										move_angle=90
									if self.animal_angles[i][n]!=-10000 and self.animal_angles[i][n]!=-1:
										angle=abs(move_angle-self.animal_angles[i][n])
										if angle>90:
											angle=abs(180-angle)
										self.all_behavior_parameters[behavior_name]['angle'][i][n]=angle

							if 'count' in included_parameters:
								if behavior_name!=self.event_probability[i][n-1][0]:
									self.all_behavior_parameters[behavior_name]['count'][i]+=1
									
							if 'duration' in included_parameters:
								self.all_behavior_parameters[behavior_name]['duration'][i]+=round(1/self.fps,2)

							if 'latency' in included_parameters:
								if self.all_behavior_parameters[behavior_name]['latency'][i]=='NA':
									self.all_behavior_parameters[behavior_name]['latency'][i]=self.all_time[n]

							if '3 length parameters' in included_parameters:
								heights_diffs=[]
								for h in self.animal_heights[i][n-self.length:n]:
									if h!=-10000 and self.animal_heights[i][n]!=-10000:
										height_diff=abs(h-self.animal_heights[i][n])/h
									else:
										height_diff=0.0
									heights_diffs.append(height_diff)
								magnitude_length=max(heights_diffs)
								vigor_length=magnitude_length/((self.length-np.argmax(heights_diffs))/self.fps)
								intensity_length=sum(heights_diffs)/(self.length/self.fps)
								if magnitude_length>0:
									self.all_behavior_parameters[behavior_name]['magnitude_length'][i][n]=magnitude_length
								if vigor_length>0:
									self.all_behavior_parameters[behavior_name]['vigor_length'][i][n]=vigor_length
								if intensity_length>0:
									self.all_behavior_parameters[behavior_name]['intensity_length'][i][n]=intensity_length

							if '4 locomotion parameters' in included_parameters:
								distance_traveled=0.0
								d=n-self.length
								while d<n-1:
									start_center=self.animal_centers[i][d]
									end_center=self.animal_centers[i][d+1]
									if start_center!=(-10000,-10000) and end_center!=(-10000,-10000):
										dt=math.dist(end_center,start_center)
									else:
										dt=0.0
									distance_traveled+=dt
									d+=1
								if normalize==0:
									calibrator=math.sqrt(cv2.contourArea(self.animal_contours[i][n]))
									distance_traveled=distance_traveled/calibrator
								speed=distance_traveled/(self.length/self.fps)
								end_center=self.animal_centers[i][n]
								if end_center!=(-10000,-10000):
									displacements=[]
									for ct in self.animal_centers[i][n-self.length:n]:
										if ct!=(-10000,-10000):
											displacements.append(math.dist(end_center,ct))
										else:
											displacements.append(0)
									displacement=max(displacements)
									if normalize==0:
										displacement=displacement/calibrator
									velocity=displacement/((self.length-np.argmax(displacements))/self.fps)
									self.all_behavior_parameters[behavior_name]['velocity'][i][n]=velocity
								velocities_max=[]
								velocities_min=[]
								for v in self.all_behavior_parameters[behavior_name]['velocity'][i][n-self.length:n]:
									if v!=np.nan:
										velocities_max.append(v)
										velocities_min.append(v)
									else:
										velocities_max.append(-float('inf'))
										velocities_min.append(float('inf'))
								vmax=max(velocities_max)
								vmin=min(velocities_min)
								if vmax!=-float('inf') and vmin!=float('inf'):
									if np.argmax(velocities_max)!=np.argmin(velocities_min):
										t=abs(np.argmax(velocities_max)-np.argmin(velocities_min))/self.fps
										self.all_behavior_parameters[behavior_name]['acceleration'][i][n]=(vmax-vmin)/t
								self.all_behavior_parameters[behavior_name]['distance'][i]+=distance_traveled
								self.all_behavior_parameters[behavior_name]['speed'][i][n]=speed

							if '3 areal parameters' in included_parameters:
								mask=np.zeros_like(self.background)
								cv2.drawContours(mask,[self.animal_contours[i][n]],0,(255,255,255),-1)
								mask=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
								area_diffs=[]
								for ct in self.animal_contours[i][n-self.length:n]:
									prev_mask=np.zeros_like(self.background)
									cv2.drawContours(prev_mask,[ct],0,(255,255,255),-1)
									prev_mask=cv2.cvtColor(prev_mask,cv2.COLOR_BGR2GRAY)
									xlf1,ybt1,w,h=cv2.boundingRect(self.animal_contours[i][n])
									xrt1=xlf1+w
									ytp1=ybt1+h
									xlf2,ybt2,w,h=cv2.boundingRect(ct)
									xrt2=xlf2+w
									ytp2=ybt2+h
									xlf=min(xlf1,xlf2)
									xrt=max(xrt1,xrt2)
									ybt=min(ybt1,ybt2)
									ytp=max(ytp1,ytp2)
									curr_mask=mask[ybt:ytp,xlf:xrt]
									prev_mask=prev_mask[ybt:ytp,xlf:xrt]
									diff=cv2.bitwise_xor(prev_mask,curr_mask)
									#diff[diff!=0]=255
									area_diff=(np.sum(diff)/255)/(np.sum(prev_mask)/255)
									area_diffs.append(area_diff)
								magnitude_area=max(area_diffs)
								vigor_area=magnitude_area/((self.length-np.argmax(area_diffs))/self.fps)
								intensity_area=sum(area_diffs)/(self.length/self.fps)
								if magnitude_area>0:
									self.all_behavior_parameters[behavior_name]['magnitude_area'][i][n]=magnitude_area
								if vigor_area>0:
									self.all_behavior_parameters[behavior_name]['vigor_area'][i][n]=vigor_area
								if intensity_area>0:
									self.all_behavior_parameters[behavior_name]['intensity_area'][i][n]=intensity_area

					else:

						if 'angle' in included_parameters:
							end_center=self.animal_centers[i][n]
							start_center=self.animal_centers[i][n-self.length]
							if end_center!=(-10000,-10000) and start_center!=(-10000,-10000):
								if end_center[0]-start_center[0]!=0:
									radius=np.arctan((end_center[1]-start_center[1])/(end_center[0]-start_center[0]))
									move_angle=math.degrees(radius)
								else:
									move_angle=90
								if self.animal_angles[i][n]!=-10000 and self.animal_angles[i][n]!=-1:
									angle=abs(move_angle-self.animal_angles[i][n])
									if angle>90:
										angle=abs(180-angle)
									self.all_behavior_parameters['angle'][i][n]=angle

						if '3 length parameters' in included_parameters:
							heights_diffs=[]
							for h in self.animal_heights[i][n-self.length:n]:
								if h!=-10000 and self.animal_heights[i][n]!=-10000:
									height_diff=abs(h-self.animal_heights[i][n])/h
								else:
									height_diff=0.0
								heights_diffs.append(height_diff)
							magnitude_length=max(heights_diffs)
							vigor_length=magnitude_length/((self.length-np.argmax(heights_diffs))/self.fps)
							intensity_length=sum(heights_diffs)/(self.length/self.fps)
							if magnitude_length>0:
								self.all_behavior_parameters['magnitude_length'][i][n]=magnitude_length
							if vigor_length>0:
								self.all_behavior_parameters['vigor_length'][i][n]=vigor_length
							if intensity_length>0:
								self.all_behavior_parameters['intensity_length'][i][n]=intensity_length

						if '4 locomotion parameters' in included_parameters:
							distance_traveled=0.0
							d=n-self.length
							while d<n-1:
								start_center=self.animal_centers[i][d]
								end_center=self.animal_centers[i][d+1]
								if start_center!=(-10000,-10000) and end_center!=(-10000,-10000):
									dt=math.dist(end_center,start_center)
								else:
									dt=0.0
								distance_traveled+=dt
								d+=1
							if normalize==0:
								calibrator=math.sqrt(cv2.contourArea(self.animal_contours[i][n]))
								distance_traveled=distance_traveled/calibrator
							speed=distance_traveled/(self.length/self.fps)
							end_center=self.animal_centers[i][n]
							if end_center!=(-10000,-10000):
								displacements=[]
								for ct in self.animal_centers[i][n-self.length:n]:
									if ct!=(-10000,-10000):
										displacements.append(math.dist(end_center,ct))
									else:
										displacements.append(0)
								displacement=max(displacements)
								if normalize==0:
									displacement=displacement/calibrator
								velocity=displacement/((self.length-np.argmax(displacements))/self.fps)
								self.all_behavior_parameters['velocity'][i][n]=velocity
							velocities_max=[]
							velocities_min=[]
							for v in self.all_behavior_parameters['velocity'][i][n-self.length:n]:
								if v!=np.nan:
									velocities_max.append(v)
									velocities_min.append(v)
								else:
									velocities_max.append(-float('inf'))
									velocities_min.append(float('inf'))
							vmax=max(velocities_max)
							vmin=min(velocities_min)
							if vmax!=-float('inf') and vmin!=float('inf'):
								if np.argmax(velocities_max)!=np.argmin(velocities_min):
									t=abs(np.argmax(velocities_max)-np.argmin(velocities_min))/self.fps
									self.all_behavior_parameters['acceleration'][i][n]=(vmax-vmin)/t
							self.all_behavior_parameters['distance'][i]+=distance_traveled
							self.all_behavior_parameters['speed'][i][n]=speed

						if '3 areal parameters' in included_parameters:
							mask=np.zeros_like(self.background)
							cv2.drawContours(mask,[self.animal_contours[i][n]],0,(255,255,255),-1)
							mask=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
							area_diffs=[]
							for ct in self.animal_contours[i][n-self.length:n]:
								prev_mask=np.zeros_like(self.background)
								cv2.drawContours(prev_mask,[ct],0,(255,255,255),-1)
								prev_mask=cv2.cvtColor(prev_mask,cv2.COLOR_BGR2GRAY)
								xlf1,ybt1,w,h=cv2.boundingRect(self.animal_contours[i][n])
								xrt1=xlf1+w
								ytp1=ybt1+h
								xlf2,ybt2,w,h=cv2.boundingRect(ct)
								xrt2=xlf2+w
								ytp2=ybt2+h
								xlf=min(xlf1,xlf2)
								xrt=max(xrt1,xrt2)
								ybt=min(ybt1,ybt2)
								ytp=max(ytp1,ytp2)
								curr_mask=mask[ybt:ytp,xlf:xrt]
								prev_mask=prev_mask[ybt:ytp,xlf:xrt]
								diff=cv2.bitwise_xor(prev_mask,curr_mask)
								#diff[diff!=0]=255
								area_diff=(np.sum(diff)/255)/(np.sum(prev_mask)/255)
								area_diffs.append(area_diff)
							magnitude_area=max(area_diffs)
							vigor_area=magnitude_area/((self.length-np.argmax(area_diffs))/self.fps)
							intensity_area=sum(area_diffs)/(self.length/self.fps)
							if magnitude_area>0:
								self.all_behavior_parameters['magnitude_area'][i][n]=magnitude_area
							if vigor_area>0:
								self.all_behavior_parameters['vigor_area'][i][n]=vigor_area
							if intensity_area>0:
								self.all_behavior_parameters['intensity_area'][i][n]=intensity_area

					n+=1

				if self.analyze==0:
				
					if 'duration' in included_parameters:
						for behavior_name in list(self.all_behavior_parameters.keys()):
							if self.all_behavior_parameters[behavior_name]['duration'][i]!=0.0:
								self.all_behavior_parameters[behavior_name]['duration'][i]+=round(self.length/self.fps,2)
							else:
								self.all_behavior_parameters[behavior_name]['duration'][i]='NA'

					if '4 locomotion parameters' in included_parameters:
						for behavior_name in list(self.all_behavior_parameters.keys()):
							if self.all_behavior_parameters[behavior_name]['distance'][i]==0.0:
								self.all_behavior_parameters[behavior_name]['distance'][i]='NA'


	def export_results(self,normalize=0,included_parameters=[]):

		print('Quantifying animal behaviors...')
		print(datetime.datetime.now())

		self.analyze_parameters(normalize=normalize,included_parameters=included_parameters)

		print('Completed!')

		print('Exporting results...')
		print(datetime.datetime.now())

		if self.analyze==0:
			events_df=pd.DataFrame.from_dict(self.event_probability,orient='index',columns=self.all_time)
			if len(self.all_time)<16000:
				events_df.to_excel(os.path.join(self.results_path,'all_event_probability.xlsx'),float_format='%.2f')
			else:
				events_df.to_csv(os.path.join(self.results_path,'all_event_probability.csv'),float_format='%.2f')

		all_parameters=[]

		if self.analyze==0:
			all_parameters.append('probability')
			
		if 'angle' in included_parameters:
			all_parameters.append('angle')
		if 'count' in included_parameters:
			all_parameters.append('count')
		if 'duration' in included_parameters:
			all_parameters.append('duration')
		if 'latency' in included_parameters:
			all_parameters.append('latency')
		if '3 length parameters' in included_parameters:
			all_parameters+=['intensity_length','magnitude_length','vigor_length']
		if '3 areal parameters' in included_parameters:
			all_parameters+=['intensity_area','magnitude_area','vigor_area']
		if '4 locomotion parameters' in included_parameters:
			all_parameters+=['acceleration','distance','speed','velocity']

		if self.analyze==0:

			for behavior_name in list(self.all_behavior_parameters.keys()):
				behavior_path=os.path.join(self.results_path,behavior_name)
				if not os.path.isdir(behavior_path):
					os.mkdir(behavior_path)

				summary=[]

				for parameter_name in all_parameters:
					if parameter_name in ['count','duration','distance','latency']:
						summary.append(pd.DataFrame.from_dict(self.all_behavior_parameters[behavior_name][parameter_name],orient='index',columns=[parameter_name]).reset_index(drop=True))
					else:
						individual_df=pd.DataFrame.from_dict(self.all_behavior_parameters[behavior_name][parameter_name],orient='index',columns=self.all_time)
						if parameter_name!='probability' and parameter_name!='angle':
							summary.append(individual_df.mean(axis=1,skipna=True).to_frame().reset_index(drop=True).rename(columns={0:parameter_name+'_mean'}))
							summary.append(individual_df.max(axis=1,skipna=True).to_frame().reset_index(drop=True).rename(columns={0:parameter_name+'_max'}))
							summary.append(individual_df.min(axis=1,skipna=True).to_frame().reset_index(drop=True).rename(columns={0:parameter_name+'_min'}))
						if len(self.all_time)<16000:
							individual_df.to_excel(os.path.join(behavior_path,parameter_name+'.xlsx'),float_format='%.2f')
						else:
							individual_df.to_csv(os.path.join(behavior_path,parameter_name+'.csv'),float_format='%.2f')

				if len(summary)>=1:
					pd.concat(summary,axis=1).to_excel(os.path.join(behavior_path,'all_summary.xlsx'),float_format='%.2f')

		else:

			summary=[]

			for parameter_name in all_parameters:
				if parameter_name=='distance':
					summary.append(pd.DataFrame.from_dict(self.all_behavior_parameters[parameter_name],orient='index',columns=['distance']).reset_index(drop=True))
				else:
					individual_df=pd.DataFrame.from_dict(self.all_behavior_parameters[parameter_name],orient='index',columns=self.all_time)

					if parameter_name!='angle':
						summary.append(individual_df.mean(axis=1,skipna=True).to_frame().reset_index(drop=True).rename(columns={0:parameter_name+'_mean'}))
						summary.append(individual_df.max(axis=1,skipna=True).to_frame().reset_index(drop=True).rename(columns={0:parameter_name+'_max'}))
						summary.append(individual_df.min(axis=1,skipna=True).to_frame().reset_index(drop=True).rename(columns={0:parameter_name+'_min'}))

					if len(self.all_time)<16000:
						individual_df.to_excel(os.path.join(self.results_path,parameter_name+'.xlsx'),float_format='%.2f')
					else:
						individual_df.to_csv(os.path.join(self.results_path,parameter_name+'.csv'),float_format='%.2f')

			if len(summary)>=1:
				pd.concat(summary,axis=1).to_excel(os.path.join(self.results_path,'all_summary.xlsx'),float_format='%.2f')			

		print('All results exported in: '+str(self.results_path))


