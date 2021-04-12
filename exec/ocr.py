import tesserocr as tr
from PIL import Image
from pathlib import Path
import json 
import docManager

def ocr(name):
	path = Path.cwd()/"tmp"/name/"regions"
	regions = get_data(name)

	for image in path.glob("*.tiff"):
		img = Image.open(image)	
		with tr.PyTessBaseAPI(psm=tr.PSM.SINGLE_LINE) as api:
			api.SetImage(img)
			text = api.GetUTF8Text().replace("\n","").split()
			conf = api.AllWordConfidences()
			update_field(name,str(image),"text",text)
			update_field(name,str(image),"word_conf",conf)

	docManager.delete_regions(name)

def update_data(name,data):
	path = Path.cwd()/"tmp"/name/"regions"/"regions.JSON"
	with open(path,'w') as file:
		json.dump(data,file)


def get_data(name):
	path = Path.cwd()/"tmp"/name/"regions"/"regions.JSON"
	with open(path,"rb") as file:
		data = json.load(file)
		return data

def update_field(name,image,field,value):
	data = get_data(name)

	for element in data:
		for region in element['regions']:
			if region['filename'] == image:
				in1 = data.index(element)
				in2 = data[in1]['regions'].index(region)
				data[in1]['regions'][in2][field] = value

	update_data(name,data)
	docManager.update_field(name,'ocr',0)
