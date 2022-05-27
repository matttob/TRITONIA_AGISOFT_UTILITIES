import Metashape

for chunk in Metashape.app.document.chunks:


    chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation, face_count=Metashape.HighFaceCount,
    face_count_custom=200000, source_data=Metashape.DenseCloudData, vertex_colors=True,
    vertex_confidence=True, volumetric_masks=False, keep_depth=True, subdivide_task=True)