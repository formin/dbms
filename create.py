
import io_file

def create_table():

 running = True
 sList = []

 #create table
 sTable = raw_input('Enter an Table Name : ')

 while running:
  #create table
  sColumn = raw_input('Enter an Add Column Name (Exit 0): ')

  if sColumn == '0':
      print 'Exit'
      running = False
      io_file.write_file(sTable, sList, 'wb')
  else:
   sList.append(sColumn)
   print sList

 else:
  print sList
