import cv2
import numpy as np
import os


batch_size = 1000
inp_shape = (256, 256)

data_path = "data/"
raw_data_path = os.path.join(data_path, "raw")
prepared_data_path = os.path.join(data_path, "prepared")
if not os.path.isdir(prepared_data_path):
	os.makedirs(prepared_data_path)

files = os.listdir(raw_data_path)
folders = []
for file in files:
	if os.path.isdir(os.path.join(raw_data_path, file)):
		folders.append(file)

counter = 1
def dump_np(data, folder_name):
	global counter
	directory = os.path.join(prepared_data_path, folder_name)
	if not os.path.isdir(directory):
		os.makedirs(directory)
	file_path = os.path.join(directory, str(counter))
	np.save(file_path, data)
	counter += 1
		

for folder in folders:
	folder_path = os.path.join(raw_data_path, folder)
	files = os.listdir(folder_path)
	bulk = []
	for i, file in enumerate(files, 1):
		file_path = os.path.join(folder_path, file)
		image = cv2.imread(file_path)
		image = cv2.resize(image, (inp_shape[1], inp_shape[0]))
		bulk.append(image)

		if len(bulk) >= batch_size or i == len(files):
			print("dumping")
			bulk = np.asarray(bulk)
			dump_np(bulk, folder)
			bulk = []

		print("Folder: %s, Files: %s/%s"%(folder, i,len(files)))

print("Completed")