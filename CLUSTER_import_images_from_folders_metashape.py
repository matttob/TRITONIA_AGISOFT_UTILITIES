import PhotoScan

client = PhotoScan.NetworkClient()

task1 = PhotoScan.NetworkTask()
task1.name = 'RunScript'
task1.params['path'] = r"C:\Users\MatthewToberman\Desktop\TRITONIA_AGISOFT_UTILITIES\import_images_from_folders_metashape.py" #path to the script to be executed
# task1.params['args'] = "argument1 argument2" #string of the arguments with space as separator

path = r"C:\Users\MatthewToberman\Desktop\cluster_test_project.psx"
client.connect('192.168.44.250') #server ip
batch_id = client.createBatch(path, [task1])
client.resumeBatch(batch_id)
print("Job started...")