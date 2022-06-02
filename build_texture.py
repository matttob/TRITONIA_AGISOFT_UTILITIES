import Metashape
#for all chunks in the project 
for chunk in Metashape.app.document.chunks:
    #building texture
    chunk.buildUV(mapping_mode=Metashape.GenericMapping, page_count=1, texture_size=8192)

    chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=16384, fill_holes=True, ghosting_filter=True, texture_type = Metashape.Model.TextureType.DiffuseMap, transfer_texture=True  ) 