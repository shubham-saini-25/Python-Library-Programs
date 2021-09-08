# importing required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "my_file.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    
	zip.printdir()

	# extracting the files
	zip.extractall()
 
	print('Done!')