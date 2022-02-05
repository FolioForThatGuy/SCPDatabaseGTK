# Here we imported the 'setup' module which allows us to install Python scripts to the local system beside performing some other tasks, you can find the documentation here: https://docs.python.org/2/distutils/apiref.html 
from distutils.core import setup 
import os
def copy_dir(files):
	dir_path = files
	base_dir = os.path.join('MODULE_DIR_HERE', dir_path)
	for (dirpath, dirnames, files) in os.walk(base_dir):
		for f in files:
			yield os.path.join(dirpath.split('/', 1)[1], f)
setup(name = "scpdatabase", # Name of the program. 
      version = "1.0", # Version of the program. 
      description = "YOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", # You don't need any help here. 
      author = "ASHER", # Nor here. 
      author_email = "jonnymyboi@icloud.com",# Nor here :D 
      license='GPLv3', # The license of the program. 
      scripts=['python_scpdatabase.py','webserver.py'], # This is the name of the main Python script file, in our case it's "myprogram", it's the file that we added under the "myprogram" folder. 

# Here you can choose where do you want to install your files on the local system, the "myprogram" file will be automatically installed in its correct place later, so you have only to choose where do you want to install the optional files that you shape with the Python script 
      data_files = [ ("lib/scpdatabase", ["ui.glade"]),# This is going to install the "ui.glade" file under the /usr/lib/myprogram path. 
      		     ('lib/scpdatabase/files', [f for f in copy_dir('files')]),
      		     ('lib/scpdatabase/img', [f for f in copy_dir('img')]), 
                     ("share/applications", ["ScpDatabase.desktop"]) ] ) # And this is going to install the .desktop file under the /usr/share/applications folder, all the folder are automatically installed under the /usr folder in your root partition, you don't need to add "/usr/ to the path. 

