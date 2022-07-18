import Metashape
mask_image_path = r"W:\\CHEVRON\\TRITONIA_AGISOFT_UTILITIES\\rov_banner_mask_SANHA_DPP.png"

for chunk in Metashape.app.document.chunks:

    chunk.generateMasks(path=mask_image_path ,masking_mode=Metashape.MaskingMode.MaskingModeFile,mask_operation=Metashape.MaskOperationReplacement, tolerance=10)
