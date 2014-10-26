# -*- coding: utf-8 -*-

from pyexiv2 import ImageMetadata, ExifTag

def Extract(foto):
	metadata = ImageMetadata(foto)
	metadata.read()

	for item in metadata.exif_keys:
		tag = metadata[item]
		print tag
		f = open("Exifinfo.txt","a")
		f.write(str(tag) + "\n")

d1 = raw_input("Foto: ")
Extract(d1)