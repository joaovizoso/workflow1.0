import cv2
import numpy as np
import tesserocr as tr
from PIL import Image
from pathlib import Path
import folderManager
import docManager
import json

#coords = [x,y,w,h]

def define_regions(image):

	regions = []
	
	img = Image.open(image)
	
	with tr.PyTessBaseAPI() as api:
		api.SetImage(img)
		boxes = api.GetComponentImages(tr.RIL.TEXTLINE,True)
		i = 1
		for (_,box,_,_) in boxes:

			x,y,w,h = box['x'],box['y'],box['w'],box['h']
			region = {}
			region['id'] = "line_1_" + str(i)
			region['bbox'] = [x,y,x+w,y+h]
			region['coords'] = [x,y,w,h]
			region['filename'] = ""
			region['text'] = []
			region['word_conf'] = [] 
			region['hocr_path'] = ""
			i+=1
			regions.append(region)

	return regions


def get_coords(regions):

	coords=[]
	for i in range(len(regions)):
		coords.append(regions[i]['coords'])
	return coords	


def crop(coords,image):

	img = cv2.imread(image)
	x,y,w,h= int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]) 
	crop_img = img[y:y+h,x:x+w].copy()
	crop_img = cv2.copyMakeBorder(crop_img,50,50,50,50,cv2.BORDER_CONSTANT,value=[255,255,255])

	return crop_img


def save(name):
	path = Path.cwd()/"tmp"/name/"regions"
	path2 = Path.cwd()/"tmp"/name/"pages"
	blocks = []

	for image in path.glob("*.tiff"):

		regions = define_regions(str(image))
		block = {}
		block['image'] = str(image.parts[-1])
		block['regions'] = regions
		blocks.append(block)

		for region in regions:
			filename = path/str(image.stem + '_%s.tiff'%(regions.index(region)+1))
			region['filename'] = str(filename)
			region['hocr_path'] = str(path2/image.stem) + '.hocr'
			result = crop(region['coords'],str(image))
			cv2.imwrite(str(filename),result)

		image.unlink()

	with open(path/'regions.JSON','w') as file:
		json.dump(blocks,file)

	docManager.update_field(name,'segment',0)
	
	return blocks


