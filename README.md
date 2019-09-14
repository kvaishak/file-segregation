# File-segregation
Python script for segregating the files in any folder according to its type.

#### Use case -  Here I am using it for automaticaly segregate files that I have downloaded to specific Folders based on its type.

## Steps
- Clone the code to your desktop.
- Using the `pip install watchdog` Install the package watchdog.
- Go into the code and edit the location of folders in the variables 
  - The varaible name corresponds to what type of files will be moved under it. 
  - The files that doesnt fit into any category list that have been defined will fall into the `misc` folder location.
  - You can edit what type of file formats should fall under each category by appending/removing from the respective list.
- Once the location and file type is edited according to your preference run the file using `python fileMove.py`

## Additional Step
- Copy the python file and rename it with file extension `fileName.command`.
- Run the command `chmod +x fileName.command`.
- Double click on the file to execute it automatically.
