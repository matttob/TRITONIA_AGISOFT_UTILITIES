import Metashape

for chunk in Metashape.app.document.chunks:
    
    chunk.buildDem(source_data=Metashape.DenseCloudData, interpolation=Metashape.EnabledInterpolation)
