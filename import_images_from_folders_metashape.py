import Metashape
from pathlib import Path

# create list of image file names

# Enter path of highest tier of video files directory structure
video_files_highest_directory = Metashape.app.getExistingDirectory("W:\CHEVRON\AA_DONT_CHANGE_Chevron2022\71-15")
video_files_highest_directory += "/"
video_files_highest_directory=Path(video_files_highest_directory)
# Search in all sub directories for any files with .mpg extension and create list of full file paths for each video file
video_file_paths = [str(pp) for pp in video_files_highest_directory.glob("**/*.mpg")]

# loop thogh each directoty that contains a video file and find the 'FRAMES' directory  within that make a list of the full path names of each image and imort into agisoft
for image_directories in video_file_paths:
    image_file_path = image_directories.split('\\')
    cropped_image_folder = ('/'.join(map(str, image_file_path[0:-1])))
    image_direcroty = ([ f.path for f in os.scandir(cropped_image_folder) if f.is_dir() ])
    image_direcroty = Path(image_direcroty[0])
    image_file_paths = [str(pp) for pp in image_direcroty.glob("**/*.jpg")]


    doc = Metashape.app.document
    chunk = doc.addChunk()
    chunk.label = image_file_path[-1]

    chunk.addPhotos(image_file_paths)
    Metashape.app.update()  