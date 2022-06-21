import Metashape

doc = Metashape.app.document

for chunk in list(doc.chunks):
        if not len(chunk.cameras):
            doc.remove(chunk)