
import Metashape

#for all chunks in the project 
for chunk in Metashape.app.document.chunks:
    #estimating image quality 
    chunk.analyzePhotos(chunk.cameras)
    for camera in chunk.cameras:
        #disable camera if <0.5 quality
        if float(camera.meta["Image/Quality"]) < 0.5:
            camera.enabled = False

