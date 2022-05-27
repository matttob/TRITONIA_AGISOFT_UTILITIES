import Metashape

for chunk in Metashape.app.document.chunks:
    
    chunk.matchPhotos(downscale = 2, generic_preselection=False, reference_preselection=False, filter_mask=False, mask_tiepoints=True, keypoint_limit=40000, tiepoint_limit=4000, guided_matching=False)

    chunk.alignCameras(adaptive_fitting=False)

    chunk.buildDepthMaps(downscale = 2, filter_mode = Metashape.MildFiltering) #DOWNSCALE: Ultra = 1, High = 2, Medium = 4, Low = 8, Lowest = 16
   
