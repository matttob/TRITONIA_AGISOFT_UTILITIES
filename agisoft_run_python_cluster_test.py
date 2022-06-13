import Metashape

app = Metashape.app
docpath = app.document.path
doc = Metashape.Document()
chunk = Metashape.app.document.chunk


network_server = '192.168.44.250' #The same name as the host name in the network monitor

Metashape.app.settings.network_path = 'W:/'  #The drive that is mapped to the network

client = Metashape.NetworkClient()

doc.open(docpath, read_only=False, ignore_lock=True)
# save latest changes
doc.save()

tasks = []  # create task list

chunk = doc.chunk


task = Metashape.Tasks.RunScript()
# task.path = "w:/MATT\TRITONIA_AGISOFT_UTILITIES\import_images_from_folders_metashape.py"
task.path = "w:/MATT\TRITONIA_AGISOFT_UTILITIES/apply_mask_to_all_chunks.py"  

tasks.append(task)



# convert task list to network tasks
network_tasks = []
for task in tasks:
    if task.target == Metashape.Tasks.DocumentTarget:
        network_tasks.append(task.toNetworkTask(doc))
    else:
        network_tasks.append(task.toNetworkTask(chunk))

client = Metashape.NetworkClient()
client.connect(app.settings.network_host)  # server ip
batch_id = client.createBatch(docpath, network_tasks)
client.setBatchPaused(batch_id, paused = False)

doc.save()
Metashape.app.messageBox("Tasks have been sent do the network. Please reopen this project without saving and it will display the progress of the jobs you have just sent.")
