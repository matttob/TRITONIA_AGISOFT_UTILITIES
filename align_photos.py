import Metashape

for chunk in Metashape.app.document.chunks:
    
    chunk.matchPhotos(keypoint_limit = 40000, tiepoint_limit = 10000, generic_preselection = True, reference_preselection = True)

    chunk.alignCameras()
   
