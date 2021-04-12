import json
from pathlib import Path
import shutil
from PIL import Image

docs = []


def write_name():
	path = Path.cwd().parents[0]/"docs"

	for file in path.glob("*.tif"):
		file.rename(file.with_suffix(".tiff"))

	for file in path.glob("*.tiff"):
		if check_name(file):
			add_doc(file)
			update_data(docs)


def check_name(path):
	names = []
	file = Path.cwd()/"tmp"/"docs.JSON"
	
	if file.is_file():
		data = get_data()
		for element in data:
			names.append(element['name'])

	name = path.parts[-1]

	if name in names:
		return False
	else:
		return True


def add_doc(path):
	img = Image.open(path)
	pages_left = img.n_frames
	doc={}
	doc['name'] = path.parts[-1]
	doc['split'] = pages_left
	doc['preprocess'] = 1
	doc['segment'] = 1
	doc['ocr'] = 1
	doc['compare'] = 1
	doc['merge'] = 1
	docs.append(doc)


def update_field(name,field,value):
	data = get_data()

	for element in data:
		if element['name'] == name: 
			ind = data.index(element)
			data[ind][field] = value

	update_data(data)


def get_field(name,field):
	data = get_data()

	for element in data:
		if element['name'] == name:
			return element[field]


def delete_data(name):
	data = get_data()

	for element in data:
		if element['name'] == name:
			data.remove(element)

	update_data(data)


def update_data(data):
	path = str(Path.cwd()/"tmp"/"docs.JSON")
	with open(path,'w') as file:
		json.dump(data,file)


def get_data():
	path = Path.cwd()/"tmp"/"docs.JSON"
	with path.open() as file:
		data = json.load(file)
		return data


def delete_page(name,page):
	path = Path.cwd()/"tmp"/name/"pages"/"page_%s.tiff"%page
	path.unlink()

def delete_regions(name):
	path = Path.cwd()/"tmp"/name/"regions"
	for elem in path.glob("*.tiff"):
		elem.unlink()


def is_finished(name):
	source = Path.cwd().parents[0]/"docs"/name
	destination = Path.cwd().parents[0]/"results"/name/name
	shutil.move(source,destination)
