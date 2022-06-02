import Metashape
#for all chunks in the project 
for chunk in Metashape.app.document.chunks:
    #build DEM
    chunk.buildDem(source_data=Metashape.DenseCloudData, interpolation=Metashape.EnabledInterpolation)
