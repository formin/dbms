
import io_file
import search

def select_table():

 #select table
 sTable = raw_input('Enter an Table Name : ')

 str = io_file.read_file(sTable, 'rb')

 #select Column
 #sColumn = raw_input('Enter an Column Name : ')

 #select Column Value
 sValue = raw_input('Enter an Column Value : ')

 sReturn = search.find(str, sValue)

 print str[sReturn]