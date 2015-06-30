
import select
import insert
import create

stype = int(raw_input('Enter an integer 1.create table 2.insert table 3.select table : '))

if stype == 1:
 create.create_table()
elif stype == 2:
 insert.insert_table()
elif stype == 3:
 select.select_table()
else:
 print 'exit'

