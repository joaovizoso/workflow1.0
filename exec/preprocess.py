import os 
from tesserocr import PyTessBaseAPI, RIL
from PIL import Image
from pathlib import Path
import folderManager
import docManager

# Produces hocr file 
# Produces input image 


def pre(image):
	img = Image.open(image)

	with PyTessBaseAPI() as api:
		api.SetImage(img)
		hocr_file = api.GetHOCRText(0)
		input_img = api.GetThresholdedImage()


	return hocr_file, input_img



def pre_process(name):
	folderManager.create_REG_TMP(name)
	path = Path.cwd()/"tmp"/name/"pages"
	destination = Path.cwd()/"tmp"/name/"regions"
	
	for image in path.glob("*.tiff"):
		
		filename = path/str(image.stem+".hocr")
		imgname = destination/str(image.stem+".tiff")
		
		hocr_file, input_img = pre(image)
		
		input_img.save(str(imgname))
		
		with open(str(filename),"w") as f:  
			f.write(str(hocr_file))

		docManager.update_field(name,'preprocess',0)

