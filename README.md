# This Repo will contain code and workflow methods for transforming video footage into Agisoft models

The photogrammetry workflow is based upon the Tritonia Scientific LTD Photogrammetry SOP, which has been curated from the USGS 'Processing Coastal Imagery with Agisoft Metashape Professional Edition, Version 1.6 — Structure From Motion Workflow Documentation'. 

The following flowchart presents a workflow to transform raw video files into models with minimal interaction with the Agiosft GUI
(https://user-images.githubusercontent.com/93919314/171664648-9b2dc808-cd81-4d2d-b002-6dac091cc1e2.png)
## Extracting and Importing Frames
#### rov_video_frame_extraction.ipynb
#### import_images_from_folders_metashape.py
## Preparing Images 
#### disable_low_quality_images.py
Disables images in all chunks less than a stated value
#### apply_mask_to_all_chunks.py
This reads in a single mask in image format and applies this mask to all images in all chunks
#### auto_maksing_object_interference.py (TO DO)
## Align Photos
#### align_photos.py 
Aligns photos in all chunks according to the parameters stated in the SOP
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
