#!/usr/bin/env python3

import split
import docManager
import preprocess
import regions
import ocr
import compare
import merge

def to_do(doc):	
	n = doc['name']

	if (doc['split']):
		print("Splitting %s"%n)
		split.split_pages(n)	
		print("%s splitted"%n)

	if (doc['preprocess']):
		print("Preprocessing %s"%n)
		preprocess.pre_process(n)
		print("%s preprocessed"%n)

	if (doc['segment']):
		print("Segmenting %s"%n)
		regions.save(n)
		print("%s segmented"%n)
	
	if (doc['ocr']):
		print("OCR %s"%n)
		ocr.ocr(n)
		print("%s OCR done"%n)

	if (doc['compare']):
		print("Comparing results of %s"%n)
		compare.modify(n) 
		print("%s results compared"%n)

	if (doc['merge']):
		print("Comparing results of %s"%n)
		merge.merge(n)
		print("%s results compared"%n)
		
	
	docManager.delete_data(n)


def main():
	docManager.write_name()
	docs = docManager.get_data()	
	for doc in docs:
		to_do(doc)
	print("Done")


if __name__ == "__main__":
	main()

