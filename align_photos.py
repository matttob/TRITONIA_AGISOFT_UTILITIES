import Metashape

for chunk in Metashape.app.document.chunks:
    
    chunk.matchPhotos(keypoint_limit = 40000, tiepoint_limit = 10000, generic_preselection = True, reference_preselection = True)

    chunk.alignCameras()

    chunk.buildDepthMaps(downscale = 2, filter_mode = Metashape.MildFiltering) #DOWNSCALE: Ultra = 1, High = 2, Medium = 4, Low = 8, Lowest = 16
   
