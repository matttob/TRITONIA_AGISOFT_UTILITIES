import Metashape

for chunk in Metashape.app.document.chunks:

    #Downscale quality scale: Ultra High = 1, High = 2, Medium = 4, Low = 8, Lowest = 16
    chunk.buildDepthMaps(downscale = 2, filter_mode = Metashape.ModerateFiltering)

    chunk.buildDenseCloud(point_colors=True, point_confidence=False, keep_depth=True, max_neighbors=100, subdivide_task=True, workitem_size_cameras=20, max_workgroup_size=100)

    
