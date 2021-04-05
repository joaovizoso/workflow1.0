from pathlib import Path
import parser_r as pr
import json

def get_ocr(name):
	path = Path.cwd()/"tmp"/name/"regions"/"regions.JSON"
	with open(path,"rb") as file:
		data = json.load(file)
		return data


def get_hocr(name,page):
	lines = []
	path = Path.cwd()/"tmp"/name/"pages"/str(page+'.hocr')
	areas = pr.get_areas(path)
	for area in areas:
		line = pr.get_lines(path,area['id'])
		for element in line:
			lines.append(element)
	return lines


def compare(name,page):
	aux = get_ocr(name)
	d1 = get_hocr(name,page)

	image = page + ".tiff"

	for page in aux:
		if page['image'] == image:
			d2 = page['regions']

	for i in d1:
		for h in d2:
			if i['bbox'] == h['bbox'] and (i['word_conf'] != h['word_conf']):
				print(i['text'])
				print(h['text'])

				print(i['word_conf'])
				print(h['word_conf'])
				print(" ")
				print(" ")
				
				best = [max(value) for value in zip(i['word_conf'],h['word_conf'])]
				for r in range(len(best)):
					if best[r] == h['word_conf'][r]:
						i['text'][r] = h['text'][r] 
						i['word_conf'][r] = h['word_conf'][r]

				print(i['text'])
				print(i['word_conf'])
				print("_______________")
	

				
					

compare("tessinput.tiff","page_2") 
