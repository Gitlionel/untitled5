
# class Animal(object):
#
#     def run(self):
#         print('Anlima is rinning')
#
#         class Dog(Animal):
#             def run(self):
#                 #dog = Dog()
#                 #dog.run()
#                 print('dog is running')
#
#         class cat (Animal):
#             def run(self):
#                 print('cat is rinning')
#
# ani = Animal().run()
# class Screen(object):
#     @property
#     def width(self):
#
#         return self._width
#     @width.setter
#     def width(self,value):
#         self._width = value
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,value):
#         self._height = value
#     @property
#     def resolution(self):
#         return self._height*self._width
# s = Screen()
# s.height = 768
# s.width = 1024
# print(s.resolution)
# assert s.resolution == 786432,'1024*768 = %d?'%s.resolution


# class Hello(object):
#     def hello(self,name = 'lc'):
#         print("hello,%s" % name)
from io import StringIO
f = StringIO()
# print(f.write('kefkdvm'))
# print(f.write('jsd'))
# print(f.getvalue())
f = StringIO('sklds!\n\nsakdskld?')
while True:
    s = f.readline()
    if s == '':
        break
print(StringIO(s.strip(s)))

#  multiprocessing模块提供了一个Process类来代表一个进程对象,启动一个子进程并等待其结束
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')
