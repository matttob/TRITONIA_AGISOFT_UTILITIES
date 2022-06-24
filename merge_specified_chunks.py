import Metashape
import sys

doc = Metashape.app.document
# make_dictionary of agisoft keys and names
chunk_dict = {}
for chunk in Metashape.app.document.chunks: 
    chunk_dict[chunk.label.split('_')[0]] = chunk.key

arg = sys.argv
list_of_chunks = [chunk_dict.get(key) for key in arg[1].split(',')[1:]]

doc.mergeChunks(chunks=list_of_chunks)
Metashape.app.document.chunks[-1].label =  arg[1].split(',')[0]





