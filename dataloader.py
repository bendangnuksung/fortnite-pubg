import numpy as np
import os


DATA_PATH = "data/prepared"


class Data():

	def __init__(self):
		self.data_counter = 0
		self.file_counter = 0
		self._load_files()
		self._load_data()


	def _load_files(self):
		folders = os.listdir(DATA_PATH)
		if len(folders) != 2:
			print("There should be only 2 folders in : %s", DATA_PATH)
			exit()
		self.folder_path_A = os.path.join(DATA_PATH, folders[0])
		self.folder_path_B = os.path.join(DATA_PATH, folders[1])
		self.files_A = os.listdir(self.folder_path_A)
		self.files_B = os.listdir(self.folder_path_B)


	def _load_data(self):
		self.data_A = np.load(os.path.join(self.folder_path_A, self.files_A[self.file_counter]))
		self.data_B = np.load(os.path.join(self.folder_path_B, self.files_B[self.file_counter]))
		self.file_counter += 1


	def get_data(self, batch_size):
		if self.data_counter >= len(self.data_A) or self.data_counter >= len(self.data_B):
			if self.file_counter > len(self.files_A) - 1 or self.file_counter > len(self.files_B) - 1:
				print("Data exhausted, Re Initialize")
				self.__init__()
				return None, None
			else:
				self._load_data()
				self.data_counter = 0

		if self.data_counter + batch_size >= len(self.data_A) or self.data_counter + batch_size >= len(self.data_B):
			remaining_A = len(self.data_A) - (self.data_counter)
			remaining_B = len(self.data_B) - (self.data_counter)
			new_batch_size = min([remaining_A, remaining_B])
			data_A = self.data_A[self.data_counter: self.data_counter + new_batch_size]
			data_B = self.data_B[self.data_counter: self.data_counter + new_batch_size]
		else:
			data_A = self.data_A[self.data_counter: self.data_counter + batch_size]
			data_B = self.data_B[self.data_counter: self.data_counter + batch_size]

		self.data_counter += batch_size

		return data_A, data_B


if __name__ == "__main__":
	data = Data()
	while True:
		a,b = data.get_data(100)
		if a is None or b is None:
			break
		print(a.shape, b.shape)