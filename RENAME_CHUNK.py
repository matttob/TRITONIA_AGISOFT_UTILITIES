
import Metashape


chunk = Metashape.app.document.chunks

for thisChunk in chunk:
	for camera in thisChunk.cameras:
		if camera.photo.path.count("/") > 1:
			thisChunk.label = ("_".join([camera.photo.path.rsplit("/",3)[1],])) + (" ") + ("_".join([camera.photo.path.rsplit("/",2)[1],]))
		else:
			print("Can't rename ")
print("Script finished")
