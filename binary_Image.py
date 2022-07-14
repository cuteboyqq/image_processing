#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:47:59 2022

@author: ali
"""

import cv2
import numpy as np

SHOW_VIDEO = True
RECORD_BINARY = False
RECORD_ORI = True
if SHOW_VIDEO:
    path = "/home/ali/factory_video/f.mp4"
    #path = "/home/ali/YOLOV4/assets/2022-03-08-new-video/Manhattan_Day.mp4"
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    c = 1
    width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)) # to get width of the frame
    height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # to get height of the frame
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*"VIDX"), 20.0, (1280,960),True)
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    if RECORD_BINARY:
        out = cv2.VideoWriter("binary_video.mp4", fourcc, 60, (width, height),0)
    elif RECORD_ORI:
        out = cv2.VideoWriter("ori_video.mp4", fourcc, 60, (width, height))
    while(vidcap.isOpened()):
        if success:
            if c > 100:
                height, width = image.shape[:2]
                cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
                cv2.imshow('frame',image)
                if RECORD_ORI:
                    out.write(image)
                
                im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
                cv2.imshow('gray',im_gray)
                
                (thresh, binary) = cv2.threshold(im_gray, 20, 255, cv2.THRESH_BINARY)
                cv2.namedWindow('binary', cv2.WINDOW_NORMAL)
                #image = cv2.resize(image, (1920, 1080), interpolation=cv2.INTER_AREA)
                #img_rgb = image[:,:,::-1]
               
                cv2.imshow('binary',binary)
                #binary_f = cv2.flip(binary, 0)
                if RECORD_BINARY:
                    out.write(binary) 
                
                kernel = np.ones((3,3), np.uint8)
                dilation = cv2.dilate(binary, kernel, iterations = 2)
                erosion = cv2.erode(dilation, kernel, iterations = 2)
                
                cv2.namedWindow('dilate_erosion', cv2.WINDOW_NORMAL)
                cv2.imshow('dilate_erosion',erosion)
                
                erosion = cv2.erode(binary, kernel, iterations = 2)
                dilation = cv2.dilate(erosion, kernel, iterations = 2)
                cv2.namedWindow('erosion_dilation', cv2.WINDOW_NORMAL)
                cv2.imshow('erosion_dilation',dilation)
                
                cv2.waitKey(5)
                
        success,image = vidcap.read()
        print(c)
        c+=1
        if c > 35000:
            out.release()

SHOW_IMG = False

if SHOW_IMG:
    path = "/home/ali/factory_video/fi.png"
    
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
    cv2.imshow('gray',gray)
    (thresh, im_bw) = cv2.threshold(gray, 20, 250, cv2.THRESH_BINARY)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',im_bw)
    
    key = cv2.waitKey(0)
  