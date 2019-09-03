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
                new_destination = misc_destination + "/" + filename     #default folder for files that dont fit into any category.

                src = folder_to_track + "/" + filename
                if fileExt in imageExtensions:
                    new_destination = image_destination + "/" + filename
                elif fileExt in videoExtensions:
                    new_destination = video_destination + "/" + filename
                elif fileExt in songExtensions:
                    new_destination = song_destination + "/" + filename
                elif fileExt in docExtensions:
                    new_destination = doc_destination + "/" + filename
                elif fileExt in zipExtensions:
                    new_destination = zip_destination + "/" + filename

                os.rename(src, new_destination)


# Modify the folder path accordingly
folder_to_track = 'path-to-Downloads'
misc_destination = 'path-to-Downloads/misc'
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
