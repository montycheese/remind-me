from creds import DEFAULT_RECEIVER, SENDER, SENDER_PWD
from simplethread import SimpleThread
from simpleemail import Email


USE_DEFAULT_EMAIL = True


def main():
	task = raw_input("Input message to be reminded: ")
	interval = float(raw_input("Select # of minutes between reminders: "))
	cycle_count = int(raw_input("How many reminders do you want: "))
	task += "\nYou will be reminded every %6.1f minute(s)." % interval	
	
	receivers = [DEFAULT_RECEIVER]
	if not USE_DEFAULT_EMAIL:
		receivers = raw_input("Input email addresses to send to seperated by spaces: ").split(" ")
		
	email = Email(SENDER, SENDER_PWD, receivers, task)
	thread = SimpleThread(interval, cycle_count, email)
	print "Starting!"
	thread.start()

if __name__ == "__main__":
	main()
