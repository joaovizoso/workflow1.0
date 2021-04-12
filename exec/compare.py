from pathlib import Path
import parser_r as pr
import parser_w as pw
import json
import docManager

def get_ocr(name):
	path = Path.cwd()/"tmp"/name/"regions"/"regions.JSON"
	with open(path,"rb") as file:
		data = json.load(file)
		return data


def get_hocr(name,page):
	lines = []
	areas = pr.get_areas(page)
	for area in areas:
		line = pr.get_lines(page,area['id'])
		for element in line:
			lines.append(element)
	return lines


def compare(name,page):
	aux = get_ocr(name)
	d1 = get_hocr(name,page)
	new_d1 = []

	image = str(page.stem) + ".tiff"

	for page in aux:
		if page['image'] == image:
			d2 = page['regions']

	for i in d1:
		for h in d2:
			if i['bbox'] == h['bbox'] and (i['word_conf'] != h['word_conf']):
				
				best = [max(value) for value in zip(i['word_conf'],h['word_conf'])]
				for r in range(len(best)):
					if best[r] == h['word_conf'][r]:
						i['text'][r] = h['text'][r] 
						i['word_conf'][r] = h['word_conf'][r]

				new_d1.append(i)

			elif  i['bbox'] == h['bbox'] and (i['word_conf'] == h['word_conf']):

				new_d1.append(i)

	return new_d1


def modify(name):
	path = Path.cwd()/"tmp"/name/"pages"
	for page in path.glob("*.hocr"):
		changes = compare(name,page)
		pw.change_hocr(page,changes)

	docManager.update_field(name,'compare',0)
					


