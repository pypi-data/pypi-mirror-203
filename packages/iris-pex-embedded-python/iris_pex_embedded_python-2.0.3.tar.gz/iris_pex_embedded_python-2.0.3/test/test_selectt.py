import iris
import os
import sys

# print var env LD_LIBRARY_PATH
print(os.environ.get('LD_LIBRARY_PATH'))

os.chdir('/usr/irissys/bin/')
from ctypes import *
CDLL("/usr/irissys/bin/pythonint.so")

iris.sql.exec('select 1')
iris.system.SQL.Purge()
iris.sql.exec('select 1')