
import io_file

def insert_table():

 running = True
 sList = []


 #select table
 sTable = raw_input('Enter an Table Name : ')
 str = io_file.read_file_header(sTable, 'rb')

 for i in range(0,len(str)):
     sColumn = raw_input('Enter an Insert Value Column '+str[i]+' : ')
     sList.append(sColumn)
 else:
    print 'End'
    io_file.write_file(sTable, sList, 'ab')
