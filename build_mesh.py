import Metashape
#for all chunks in the project 
for chunk in Metashape.app.document.chunks:
    #build mesh
    chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation, face_count=Metashape.HighFaceCount, source_data=Metashape.DenseCloudData, vertex_colors=True,
    vertex_confidence=True, volumetric_masks=False, keep_depth=False, subdivide_task=True)