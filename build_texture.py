import Metashape

for chunk in Metashape.app.document.chunks:

    chunk.buildUV(page_count=1, texture_size=8192)

    chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=16384, fill_holes=True, ghosting_filter=True, texture_type = Metashape.Model.TextureType.DiffuseMap, transfer_texture=True  ) 