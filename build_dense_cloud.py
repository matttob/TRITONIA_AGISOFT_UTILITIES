import Metashape

#densecloud,
for chunk in Metashape.app.document.chunks:

    chunk.buildDenseCloud(quality = Metashape.HighQuality,point_colors=True, point_confidence=True, keep_depth=True, max_neighbors=100, subdivide_task=True, filter = Metashape.ModerateFiltering)
