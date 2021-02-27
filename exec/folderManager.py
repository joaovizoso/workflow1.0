from pathlib import Path 
import os


# Folder Manager
# Add and remove folders


def create_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name 
	if not Path(folder).exists():
		Path(folder).mkdir()


def create_OCR_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name/"ocr"
	if not Path(folder).exists():
		Path(folder).mkdir()


def create_PAGES_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name/"pages"
	if not Path(folder).exists():
		Path(folder).mkdir()


def create_REG_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name/"regions"
	if not Path(folder).exists():
		Path(folder).mkdir()


def create_RESULT(name): 

	previous = Path.cwd().parents[0]
	folder = previous/"results"/name
	if not Path(folder).exists():
		Path(folder).mkdir()


def delete_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name
	folder.rmdir()


def delete_OCR_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name/"ocr"
	for f in folder.glob("*.pdf"):
		f.unlink()
	folder.rmdir()
	

#Verificar se não é necessário apagar ficheiros das pastas

def delete_REG_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name/"regions"
	folder.rmdir()

def delete_IMG_TMP(name):

	current = Path.cwd()
	folder = current/"tmp"/name/"pages"
	folder.rmdir()


