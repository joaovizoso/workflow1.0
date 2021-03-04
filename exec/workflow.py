#!/usr/bin/env python3

import split
import docManager


def to_do(doc):	
	n = doc['name']

	if (doc['split']):
		print("Splitting %s"%n)
		split.split_pages(n)	
		print("%s splitted"%n)

	#if (doc['o']):
		#recognize(n)
	
	#if (doc['m']):
		#merge(n)
	
	docManager.delete_data(n)


def main():
	docManager.write_name()
	docs = docManager.get_data()	
	for doc in docs:
		to_do(doc)
	print("Done")


if __name__ == "__main__":
	main()

