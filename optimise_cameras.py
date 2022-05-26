import Metashape

for chunk in Metashape.app.document.chunks:
    chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy=True, fit_b1=False, fit_b2=False, fit_k1=True,
fit_k2=True, fit_k3=True, fit_k4=False, fit_p1=True, fit_p2=True, fit_corrections=False,
adaptive_fitting=False, tiepoint_covariance=False)
print("Camera optimisation complete")
