import Metashape
#for all chunks in the project 
for chunk in Metashape.app.document.chunks:
    
    #align all photos. Downscale quality scale: Highest = 0, High = 1, Medium = 2, Low = 4, Lowest = 8
    chunk.matchPhotos(downscale = 2, generic_preselection=False, reference_preselection=False, filter_mask=False, mask_tiepoints=True, keypoint_limit=40000, tiepoint_limit=4000, guided_matching=False) 

    chunk.alignCameras(adaptive_fitting=False)

   
