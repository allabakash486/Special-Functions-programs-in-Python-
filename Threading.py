import threading,time
def method():
    for i in range(5):
        print('Hello')
def method1():
    for i in range(5):
        print('Hi')
            
Task1 = threading.Thread(target=method)
Task2 = threading.Thread(target=method1)
Task1.start()
Task2.start()

    
