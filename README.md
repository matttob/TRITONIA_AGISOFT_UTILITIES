# This Repo will contain code and workflow methods for transforming video footage into Agisoft models

The photogrammetry workflow is based upon the Tritonia Scientific LTD Photogrammetry SOP, which has been curated from the USGS 'Processing Coastal Imagery with Agisoft Metashape Professional Edition, Version 1.6 — Structure From Motion Workflow Documentation'. 

The following flowchart presents a workflow to transform raw video files into models with minimal interaction with the Agiosft GUI

(https://user-images.githubusercontent.com/93919314/176164325-c5620dfc-6439-4d03-85ac-0623d2b0150c.png)


## Extracting and Importing Frames
#### rov_video_frame_extraction.ipynb
Loop through all data directories and sub directories and search for any video files. Then extract frames from each of these directories and store in sub directory.
#### import_images_from_folders_metashape.py
Loop through all data directories and sub directories and import images into Agisoft. Each set of each images is imported as a chunk with the name of the video and depth range of the video as the chunk name
## Preparing Images 
#### disable_low_quality_images.py
Disables images in all chunks less than a stated value
#### remove_empty_chunks.py
Remove all empty chunks
#### apply_mask_to_all_chunks.py
This reads in a single mask in image format and applies this mask to all images in all chunks
#### auto_maksing_object_interference.py (TO DO)
## Align Photos
#### align_photos.py 
Aligns photos in all chunks according to the parameters stated in the SOP (Except Highest accuracy)
#### optimise_cameras.py
Optimises camera alignment with default settings for all chunks 
## Gradual Selection
#### recunc_gradual_selection.py
Removes points based on the reconstruction uncertainty level outlined in the SOP for tie point clouds in all chunks
#### projacc_gradual_selection.py
Removes points based on the projection accuracy level outlined in the SOP for tie point clouds in all chunks
#### reperr_gradual_selection.py
Removes points based on the reprojection error level outlined in the SOP for tie point clouds in all chunks
## Build Dense Cloud 
#### build_densecloud.py 
Builds denseclouds in all chunks according to the parameters stated in the SOP
#### densecloud_confidence_filter.py
Removes points based on the densecloud point confidence outlined in the SOP for tie point clouds in all chunks
## Build Mesh 
Builds mesh in all chunks according to the parameters stated in the SOP
#### build_mesh.py 
## Build Texture
#### build.texture.py 
Builds texture in all chunks according to the parameters stated in the SOP
## Build DEM
#### build_dem.py 
Builds DEM in all chunks according to the parameters stated in the SOP
## Export model 
#### export_model (TO DO)
