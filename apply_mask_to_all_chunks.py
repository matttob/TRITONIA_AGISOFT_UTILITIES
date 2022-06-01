import Metashape
mask_image_path = r"C:\Users\MatthewToberman\Desktop\rov_baner_mask.png"

for chunk in Metashape.app.document.chunks:

    chunk.generateMasks(path=mask_image_path ,masking_mode=Metashape.MaskingMode.MaskingModeFile,mask_operation=Metashape.MaskOperationReplacement, tolerance=10)
