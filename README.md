# This Repo will contain code and workflow methods for transforming video footage into Agisoft models

The photogrammetry workflow is based upon the Tritonia Scientific LTD Photogrammetry SOP, which has been curated from the USGS 'Processing Coastal Imagery with Agisoft Metashape Professional Edition, Version 1.6 — Structure From Motion Workflow Documentation'. 

The following flowchart presents a workflow to transform raw video files into models with minimal interaction with the Agiosft GUI
(https://user-images.githubusercontent.com/93919314/170470108-befc9c9d-d48a-4192-bd15-8909b74d0329.png)
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
#### optimise_cameras.py
Optimises camera alignment with default settings 
## Gradual Selection
#### recunc_gradual_selection.py
Removes points based on the reconstruction uncertainty level outlined in the SOP
#### projacc_gradual_selection.py
Removes points based on the projection accuracy level outlined in the SOP
#### reperr_gradual_selection.py
Removes points based on the reprojection error level outlined in the SOP
## Build Dense Cloud 
#### build_densecloud.py 
#### densecloud_confidence_filter.py
Removes points based on the densecloud point confidence outlined in the SOP
## Build Mesh 
#### build_mesh.py 
## Build Texture
#### build.texture.py 
## Build DEM
#### build_dem.py 
## Export model 
#### export_model (TO DO)
