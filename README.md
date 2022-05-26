# This Repo will contain code and workflow methods for transforming video footage into Agisoft models

The photogrammetry workflow is based upon the Tritonia Scientific LTD Photogrammetry SOP, which has been curated from the USGS 'Processing Coastal Imagery with Agisoft Metashape Professional Edition, Version 1.6 — Structure From Motion Workflow Documentation'. 

The following flowchart presents a workflow to transform raw video files into models with minimal interaction with the Agiosft GUI.
(https://user-images.githubusercontent.com/93919314/170470108-befc9c9d-d48a-4192-bd15-8909b74d0329.png)
## Extracting and Importing Frames
#### ROV_FOOTAGE_FRAME_EXTRACTION.py
#### import_images_from_folders_metashape.py
## Preparing Images 
#### DISABLE_LOW_QUALITY_IMAGES.py
Disables images in all chunks less than a stated value
#### AUTO_MASKING.py (TO DO)
## Align Cameras
#### ALIGN_CAMERAS.py (TO DO)
#### OPTIMISE_CAMERAS.py
Optimises camera alignment with default settings 
## Gradual Selection
#### RECUNC_GRADUALSELECTION.py
Removes points based on the reconstruction uncertainty level outlined in the SOP
#### PROJACC_GRADUALSELECTION.py
Removes points based on the projection accuracy level outlined in the SOP
#### REPERR_GRADUALSELECTION.py
Removes points based on the reprojection error level outlined in the SOP
## Build Dense Cloud 
#### BUILD_DENSE_CLOUD.py (TO DO)
#### DENSECLOUD_CONFIDENCE_FILTER.py
Removes points based on the densecloud point confidence outlined in the SOP
## Build Mesh 
#### BUILD_MESH.py (TO DO)
## Build Texture
#### BUILD_TEXTURE.py (TO DO)
## Build DEM
#### BUILD_DEM.py (TO DO)
## Export model 
#### EXPORT_MODEL (TO DO)
