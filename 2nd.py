from threading import *

#thread without using a class

# def display():
#     for i in range(0,10):
#         print("Child Thread")

# t = Thread(target=display)    #Creating Thread Object
# t.start()
# for _ in range(0,10):
#     print("Main Thread")



#thread by extending the thread class
# class Test(Thread):
#     def run(self):
#         for _ in range(0,10):
#             print("Child Thread")

# t= Test()
# t.start()
# for _ in range(0,10):
#     print("Main Thread")



# Thread without extending the thread class
# class Temp:
#     def display(self):
#         for i in range(1,10):
#             print(i)

# t1=Temp()
# t=Thread(target=t1.display)
# t.start()
# for _ in range(0,10):
#     print("Child Thread")



# print(current_thread().getName())
# current_thread().setName("RK")

# def fun():
#     for i in range(1,11):
#         print(i)

# t = Thread(target=fun)      # Creating Thread Object
# print(t.is_alive())   


# th = current_thread().name
# print(th)
# import gc

# gc.isenabled()
# for x in enumerate():
#     print(x.name)



# import time
 
# # creating a function
# def thread_1():                     
#   for i in range(5):
#     print('this is thread T')
#     time.sleep(3)
 
# T = Thread(target = thread_1)
# T.setDaemon(True)                  
# T.start()                          
# time.sleep(5)
# print('this is Main Thread')


