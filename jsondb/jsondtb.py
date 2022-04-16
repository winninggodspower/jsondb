from cryptography.fernet import Fernet
from contextlib import contextmanager
import json
import os.path

basic_jsd = """{ 
"data":[]
}"""

class json_database:

	def __init__(self,list_,file ,id=False):

		list_.append({'id':id})  #adding the value of id to the list

		if not os.path.isfile(file):
		#uploading the basic json code to file if file is newly created
		    basic = json.loads(basic_jsd)
		    with open(file,'w') as f:
			    json.dump(basic,f,indent=2)

		# important instances
		self.columns = list_
		self.dbfile = file
		self.is_encrypted = False
		self.emp_key = Fernet.generate_key()


	#methods that lets us view data
	def view_data(self):
		with open(self.dbfile,'r') as f:
			db = json.load(f)["data"]

		return db

    #methods that lets us view data for class use
	def view_data_class(self):
		with open(self.dbfile,'r') as f:
			db = json.load(f)

		return db

	# method that add rows to the database
	def add_row(self,list_):

		#loading the existing database to work on
		db=self.view_data_class()

        # adding the data to the dic
		dic = {}
		for keys,values in zip(self.columns,list_):
			creat = {keys:values}
			dic.update(creat)

		try:
		    #if user usses id then add the id
			if self.columns[-1]['id'] == True:
				#get previous id
				db = self.view_data_class()
				old_id = int(db['data'][-1]['id']) #getting old id

				new_id = old_id + 1 #setting new id
				dic.update({'id':new_id})

		except:
			dic.update({'id':1})


		db['data'].append(dic)



		#saving the aded data back
		with open (self.dbfile,'w') as f:
			json.dump(db, f, indent=2)

	#method that delete a dict from the database
	def delete_row(self,column,value):
		db = self.view_data_class()
		deleted = False

		for row in db['data']:
			if row[column] == value:
				db['data'].remove(row)
				deleted = True
				break

		with open (self.dbfile,'w') as f:
			json.dump(db, f, indent=2)

		if 'id' in self.columns:
			self.refactor_id()

		return deleted

	def refactor_id(self):
		if not self.columns[-1]['id'] == True:
			raise Exception('database does not contain field id')
			return

		db = self.view_data_class()
		init_id = 1
		for row in db['data']:
			row['id'] = init_id
			init_id += 1

		with open (self.dbfile,'w') as f:
			json.dump(db, f, indent=2)
			return 'sucess'
			 		

	def update_row_element(self, row_, value_, **kwargs):
		db = self.view_data_class()

		for row in db['data']:
			check = map(lambda key: True if kwargs[key] == row[key] else False, kwargs.keys())
			if all(check):
				print(check)
				row[row_] = value_
				break
			# if row[column] == value:
			# 	row[old_value]=new_value

		with open (self.dbfile,'w') as f:
			json.dump(db, f, indent=2)
			return 'sucess'

	def get_row(self, column, value):
		db = self.view_data()

		for row in db:
			if row[column] == value:
				return row

	def filter_row(self, **kwargs):
		db = self.view_data_class()
		elements = []

		for row in db['data']:
			check = map(lambda key: True if kwargs[key] == row[key] else False, kwargs.keys())
			if all(check):
				elements.append(row)

		return None if len(elements) == 0 else elements

	# context manager to encrypt and decrypt your file
	@contextmanager
	def SecureData(self):
		data = self.decrypt_data()

		yield data

		self.encrypt_data()
		
	def encrypt_data(self):
		f = Fernet(self.emp_key)

		if self.is_encrypted:
			return

		byte_data = json.dumps(self.view_data_class()).encode('utf-8')
		encrypted_data = f.encrypt(byte_data).decode()

		self.upload_data(encrypted_data)
		self.is_encrypted = True

	def decrypt_data(self):
		if not self.is_encrypted:
			return None

		f = Fernet(self.emp_key)

		byte_data = json.dumps(self.view_data_class()).encode('utf-8')
		decrypted_data = json.loads(f.decrypt(byte_data).decode())

		self.upload_data(decrypted_data)
		self.is_encrypted = False

		return decrypted_data
		
	
	def upload_data(self,data):
		with open (self.dbfile,'w') as f:
			# f.write(data.encode())
			json.dump(data, f ,indent = 2)


