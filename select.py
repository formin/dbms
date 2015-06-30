
import io_file
import search

def select_table():

 #select table
 sTable = raw_input('Enter an Table Name : ')

 shr = io_file.read_file_header(sTable, 'rb')

 #select Column
 sColumn = raw_input('Enter an Column Name : ')

 sHReturn = search.h_find(shr, sColumn)

 str = io_file.read_file(sTable, 'rb')

 #select Column Value
 sValue = raw_input('Enter an Column Value : ')

 sDReturn = search.data_find(str, sValue, sHReturn)

 print str[sDReturn]