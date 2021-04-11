#coding:utf-8
import time
import threading

from threading import Thread

def Myfonction1():
	i = 1
	while i<3:
		print("Qannaf")
		time.sleep(0.4)
		i+=1

def Myfonction2():
	i = 1
	while i<3:
		print("AL-SAHMI")
		time.sleep(0.3)
		i+=1

Myfonction1()
Myfonction2()

th1 = Thread(target = Myfonction1)
th2 = Thread(target = Myfonction2)

th1.start()
th2.start()


th1.join()
th2.join()

print("Fin de programme ...")


#=============================================#
class myclass (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):
		i = 0
		while i<3:
			print(threading.current_thread())
			time.sleep(0.4)
			i+=1



th1 = myclass()
th2 = myclass()

th1.start()
th2.start()


th1.join()
th2.join()

print("Fin de programme ...")


#verouiller les impremmante
""""========================================"""
my_lock = threading.RLock()
class myclass (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):
		i = 0
		while i<3:
			with my_lock:
				letters = "ABC"
				for element in letters:
					print(element)
					time.sleep(0.4)
			i+=1



th1 = myclass()
th2 = myclass()

th1.start()
th2.start()


th1.join()
th2.join()

print("Fin de programme ...")
