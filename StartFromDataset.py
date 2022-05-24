import os
from sys import argv
import track


directory = os.fsencode(argv[1])
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    if filename.endswith(".jpg"):
        image_path = str(argv[1]) + filename
        track.main(image_path, 'IV' ,'pytorch', True, False)
    else:
         continue