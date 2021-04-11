#coding:utf-8
import datetime
from datetime import date

''' ===============           pgm                =============  '''
d1 = datetime.datetime(2019, 12, 29, 7, 59, 58)
d2 = datetime.datetime(2019, 12, 30, 7, 59, 58)

if d1<d2:
	print("d1 est plus ancien que d2")
else:
	print("d1 est plus récent que d2")

"""" =========================="""
d1 = datetime.date(2019, 12, 29)
print(d1.year)
print(type(d1))

d1 = datetime.time(20, 12, 29)
print(d1)
print(type(d1))

#=================
print(date.today()) 

now = date.today()
date_de_naissance = datetime.date(1992,5,6)
print("{} ans".format(now.year - date_de_naissance.year))