import threading
from time import sleep

class T(threading.Thread):
      def __init__(self, n):
        threading.Thread.__init__(self, name="t"+n)
        self.n = n

      def run(self):
          print "Process", self.n
          sleep(10)


p1=T("1")
p2=T("2")

p1.setDaemon(True)
p2.setDaemon(True)

p1.start()
p2.start()

p1.join()
p2.join()

