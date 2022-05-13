import Metashape

for chunk in Metashape.app.document.chunks:

    chunk.dense_cloud.setConfidenceFilter(0,2) #shows only dense points with confidence between 0 and 2
    chunk.dense_cloud.removePoints(list(range(128))) #removes all "visible" points of the dense cloud
    chunk.dense_cloud.resetFilters() #resets filters to show remaining points


# test change    