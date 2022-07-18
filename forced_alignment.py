import Metashape
#for all chunks in the project 
for chunk in Metashape.app.document.chunks: 
    #for all cameras in each chunk 
    for camera in chunk.cameras:
        #if camera is aligned then disable
        if  camera.transform:
            camera.enabled = False
            #otherwise enable
        else: camera.enabled = True 
#align all (enabled) cameras. Downscale quality scale: Highest = 0, High = 1, Medium = 2, Low = 4, Lowest = 8
chunk.matchPhotos(downscale = 2, generic_preselection=False, reference_preselection=False, filter_mask=False, mask_tiepoints=True, keypoint_limit=40000, tiepoint_limit=4000, guided_matching=False)
chunk.alignCameras(adaptive_fitting=False)

for chunk in Metashape.app.document.chunks:
    for camera in chunk.cameras:
        #enable all not aligned cameras
        if  camera.transform:
            camera.enabled = True


    
