#!/usr/bin/env python
from watchdog.observers import Observer #pip install watchdog for this to work.
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            ext = filename.split('.')
            # print(ext)
            if len(ext) > 1:
                fileExt = ext[len(ext) - 1]
                new_destination = misc_destination    #default folder for files that dont fit into any category.
                i = 1
                src = folder_to_track + "/" + filename
                if fileExt in imageExtensions:
                    new_destination = image_destination
                elif fileExt in videoExtensions:
                    new_destination = video_destination
                elif fileExt in songExtensions:
                    new_destination = song_destination
                elif fileExt in docExtensions:
                    new_destination = doc_destination
                elif fileExt in zipExtensions:
                    new_destination = zip_destination

                new_name = filename
                file_exists = os.path.isfile(new_destination + '/' + new_name)
                while(file_exists):
                    i+=1
                    new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                    # based on the number of '/' present in the folder to track modify the number inside the bracket.
                    # for example here i have used the path [/Users/vaishak/Downloads] -> three backslashes so (3+1) inside the bracket
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(new_destination + "/" + new_name)
                    

                new_name = new_destination + "/" + new_name
                os.rename(src, new_name)


# Modify the folder path accordingly
folder_to_track = 'path-to-Downloads'
misc_destination = 'path-to-Downloads/uncategorised'
song_destination = 'path-to-Downloads/songs'
video_destination = 'path-to-Downloads/video'
image_destination = 'path-to-Downloads/image'
doc_destination = 'path-to-Downloads/docs'
zip_destination = 'path-to-Downloads/zip'

imageExtensions = ['jpg', 'png', 'jpeg', 'gif', 'tif']
videoExtensions = ['mp4', 'avi', 'mov', 'wmv', 'flv', '3gp']
songExtensions = ['mp3', 'aac', 'wma', 'ac3', 'eac3', 'pcm']
docExtensions = ['pdf', 'doc', 'docx', 'gdoc', 'xls', 'xlsx', 'ppt', 'pptx', 'txt']      #you can add other file extensions you need to track of here like pptx, etc.
zipExtensions = ['zip']

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
