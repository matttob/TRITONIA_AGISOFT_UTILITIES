

import Metashape


for chunk in Metashape.app.document.chunks:
    chunk.analyzePhotos(chunk.cameras)
    for camera in chunk.cameras:
        if float(camera.meta["Image/Quality"]) < 0.5:
            camera.enabled = False




