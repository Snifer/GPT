# -*- coding: utf-8 -*-
from PIL import Image
import os

def clean(archivo): 
	d2 = os.path.splitext(archivo)[1]
	try: 
		foto = Image.open(archivo)
		foto.save("copiasinmeta"+ d2)
	except: 
		print d2,"No soportado"	

d1= raw_input ("Foto: ")
clean(d1)
