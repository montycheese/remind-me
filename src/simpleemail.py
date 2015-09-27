from smtplib import SMTP, SMTPConnectError, SMTPServerDisconnected, SMTPException
from creds import GMAIL_HOST, GMAIL_PORT

class Email():
	def __init__(self, from_addr, from_pwd, to_addr=[], msg=""):
		self.from_addr = from_addr
		self.from_pwd = from_pwd
		self.to_addr = to_addr
		self.msg = msg
	
	def send(self, message=""):
		if self.to_addr == "":
			print "No receiver specificed."
			raise SMTPException
		try:
			server = SMTP(GMAIL_HOST, GMAIL_PORT)
			server.ehlo()
			server.starttls()
			server.ehlo()
			#log into server
			server.login(self.from_addr, self.from_pwd)
			if message == "":
				message = self.msg
				
			server.sendmail(self.from_addr, self.to_addr, message)
			server.quit()
			print "Email sent success."
			
		except (SMTPConnectError, SMTPServerDisconnected):
			print "Unable to connect"

	def set_message(self, message):
		self.msg = message
	
	def set_reciever_email(self, email):
		self.to_addr.append(email)

