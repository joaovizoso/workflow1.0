import cv2
import numpy as np
import tesserocr as tr
from PIL import Image
from pathlib import Path
import folderManager

#coords = [x,y,w,h]

def define_regions(image):

	regions = []
	cv_img = cv2.imread(image)
	pil_img = Image.fromarray(cv_img)
	api = tr.PyTessBaseAPI()

	try:
		api.SetImage(pil_img)
		boxes = api.GetComponentImages(tr.RIL.TEXTLINE,True)
		i = 1
		for (_,box,_,_) in boxes:
			x,y,w,h = box['x'],box['y'],box['w'],box['h']
			region = {}
			region['id'] = i
			region['text'] = []
			region['coords'] = [x,y,w,h]
			i+=1
			regions.append(region)
	finally:
		api.End()

	return regions


def get_coords(regions):

	coords=[]
	for i in range(len(regions)):
		coords.append(regions[i]['coords'])
	return coords


def crop(coords,image):

	img = cv2.imread(image)
	x = int(coords[0])
	y = int(coords[1])
	w = int(coords[2])
	h = int(coords[3])
	crop_img = img[y:y+h,x:x+w].copy()

	return crop_img


def save(name):
	folderManager.create_REG_TMP(name)
	path = Path.cwd()/"tmp"/name/"pages"
	destination = str(Path.cwd()/"tmp"/name/"regions")
	i=1 
	
	for image in path.glob("*.tiff"):

		regions = define_regions(str(image))
		coords = get_coords(regions)
		

		for region in range(len(coords)):
			result = crop(coords[region],str(image))
			cv2.imwrite(destination+'/%s_%s.tiff'%(i,region),result)

		i+=1

	print("Done")


print(define_regions("44_82.tiff"))

