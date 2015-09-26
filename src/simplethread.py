import threading

class SimpleThread(threading.Thread):
    def __init__(self,refresh_time, cycle_count, email, event=threading.Event()):
        threading.Thread.__init__(self)
        self.stopped = event
        self.refresh_time = refresh_time * 60
        self.cycle_count = cycle_count
        self.count = 1
        self.email = email

    def run(self):
	    for i in range(self.cycle_count):
		    self.stopped.wait(self.refresh_time)
		    print "Emailing"
		    progress = "\nThis is reminder %d of %d." % (self.count, self.cycle_count)
		    self.email.send(self.email.msg + progress)
		    self.count += 1
            self.stopped.set()
