import simplethread as st
import simpleemail as se
import creds

USE_DEFAULT_EMAIL = True


def main():
	task = raw_input("Input message to be reminded: ")
	interval = int(raw_input("Select # of minutes between reminders: "))
	cycle_count = int(raw_input("How many reminders do you want: "))
	task += "\nYou will be reminded every %d minute(s)." % interval	
	
	receivers = [creds.DEFAULT_RECEIVER]
	if not USE_DEFAULT_EMAIL:
		receivers = raw_input("Input email addresses to send to seperated by spaces: ").split(" ")
		
	email = se.Email(creds.SENDER, creds.SENDER_PWD, receivers, task)
	thread = st.SimpleThread(interval, cycle_count, email)
	thread.start()

if __name__ == "__main__":
	main()
