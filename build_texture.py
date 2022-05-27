import Metashape


for chunk in Metashape.app.document.chunks:

    chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=16384, fill_holes=True, ghosting_filter=True, texture_type=Metashape.DiffuseMap, transfer_texture=True  ) 