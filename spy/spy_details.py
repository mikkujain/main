#from datetime import datetime	
class Spy:

	def __init__(self,name,salutation,age,rating):
		self.name=name
		self.salutation=salutation
		self.age=age
		self.rating=rating
		self.is_online=True
		self.chats=[]
		self.current_status_message = None

class chatMessage:

	def __init__(self, message, send_by_me):
		self.message=message
		#self.timestamp=datetime.now()
		self.send_by_me=send_by_me
		



