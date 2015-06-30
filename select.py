
import io_file

def select_table():

 #select table
 sTable = raw_input('Enter an Table Name : ')

 str = io_file.read_file(sTable, 'rb')

 loaded_objects = []
 loaded_objects.append(str)

 print loaded_objects