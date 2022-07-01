import Metashape
from pathlib import Path
import os
import sys

frame_interval = 2

# create list of image file names

# Enter path of highest tier of video files directory structure
# video_files_highest_directory = Metashape.app.getExistingDirectory("Choose starting folder from which to search for video files")
# video_files_highest_directory += "/"
video_files_highest_directory = r"W:\CHEVRON\AA_DONT_CHANGE_Chevron2022\GS-MIKE_FLARE"

doc = Metashape.app.document
chunk = doc.addChunk()
chunk.label = video_files_highest_directory

video_files_highest_directory=Path(video_files_highest_directory)
# Search in all sub directories for any files with .mpg extension and create list of full file paths for each video file
video_file_paths_mpg = [str(pp) for pp in video_files_highest_directory.glob("**/*.mpg")]
video_file_paths_asf = [str(pp) for pp in video_files_highest_directory.glob("**/*.asf")]
video_file_paths = video_file_paths_mpg + video_file_paths_asf


# loop thogh each directoty that contains a video file and find any sub direcrorires directory  within that make a list of the full path names of each image and imort into agisoft
for video_file_names in video_file_paths:
    split_video_file_path = video_file_names.split('\\')

    directory_containing_video_files = ('/'.join(map(str, split_video_file_path[0:-1])))
    
    
    image_direcroties = ([ f.path for f in os.scandir(directory_containing_video_files) if f.is_dir() ])
    # loop through all subdirectories
    
    for video_file_sub_names in image_direcroties:
        image_direcroty = Path(video_file_sub_names)
        # print(image_direcroty)
        image_file_paths = [str(pp) for pp in image_direcroty.glob("**/*.jpg")]
        arg = sys.argv
        image_file_paths =  image_file_paths[0 : -1  : frame_interval]

        if len(image_file_paths) > 10:
            chunk.addPhotos(image_file_paths)
    
Metashape.app.update()  
