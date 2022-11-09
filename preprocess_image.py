#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:28:19 2022

@author: ali
"""

import glob
import cv2
import os

def parse_path(img_path):
    img_file = img_path.split('/')[-1]
    img_filename = img_file.split('.')[0]
    return img_file,img_filename

def Get_Binary_images(img_dir):
    os.makedirs('./runs/detect/noline_gray_images',exist_ok=True)
    img_list = glob.glob(os.path.join(img_dir,'*.jpg'))
    for img_path in img_list:
        print(img_path)
        im = cv2.imread(img_path)
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
       
        img_file,img_filename = parse_path(img_path)
        
        save_img_file = img_filename + '_gray.jpg'
        file_path = os.path.join('./runs/detect/noline_gray_images/',save_img_file)
        cv2.imwrite(file_path,im_gray)

if __name__=="__main__":
    
    img_dir = r'/home/ali/GitHub_Code/YOLO/YOLOV5/runs/detect/factory_data/crops_noline/noline'
    
    Get_Binary_images(img_dir)