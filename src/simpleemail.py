import smtplib, creds
#declare constants in creds file

class Email():
	def __init__(self, from_addr, from_pwd, to_addr=[], msg = ""):
		self.from_addr = from_addr
		self.from_pwd = from_pwd
		self.to_addr = to_addr
		self.msg = msg
		self.server = smtplib.SMTP()
	
	def send(self, message = ""):
		if self.to_addr == "":
			print "No receiver specificed."
			return
			#use exception later
		self.server.connect(creds.GMAIL_HOST, creds.GMAIL_PORT)
		self.server.ehlo()
		self.server.starttls()
		self.server.ehlo()
		self.sender = self.from_addr
		#log into server
		self.server.login(self.from_addr, self.from_pwd)
		try:
			if message == "":
				message = self.msg
			self.server.sendmail(self.from_addr, self.to_addr, message)
			self.server.quit()
			print "Email sent success"
		except:
			print "ERROR: unable to send email"
			#exit()
	
	def set_message(self, message):
		self.msg = message
	
	def set_reciever_email(self, email):
		self.to_addr.append(email)

