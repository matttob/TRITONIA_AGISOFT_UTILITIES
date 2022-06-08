import Metashape

client = Metashape.NetworkClient()

task1 = Metashape.NetworkTask()
task1.name = 'RunScript'
task1.params['path'] = r"CLUSTER_TEST_import_images_from_folders_metashape.py" #path to the script to be executed
# task1.params['args'] = "argument1 argument2" #string of the arguments with space as separator

path = r"Cluster_test_project.psx"
client.connect('192.168.44.250') #server ip
batch_id = client.createBatch(path, [task1])
print('batch ID - ' + str(batch_id))
client.setBatchPaused(batch_id, paused = False)
print("Job started...")