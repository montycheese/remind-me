from smtplib import SMTPException
from creds import SENDER
from threading import Thread, Event
import simpleemail

class SimpleThread(Thread):
    def __init__(self, refresh_time, cycle_count, email, event=Event()):
        Thread.__init__(self)
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
		    try:
		    	self.email.send(self.email.msg + progress)
		    	self.count += 1
		    except SMTPException:
		    	print '''Username/Password combination for %s or or hostname  refused.\nPlease re-check your credientials.''' % SENDER
		    	self.stopped.set()
                        return
                    except Exception:
                        print 'most likely lost internet connection, exiting'
                        return
            self.stopped.set()
