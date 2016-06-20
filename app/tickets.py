class Ticket:
	def __init__(self,ticket):
		self.id = ticket.get("_id")
		self.title = ticket.get("title")
		self.category = ticket.get("category")
		self.status = ticket.get("status")
		self.description = ticket.get("description")
		self.reporter = ticket.get("reporter")
		self.comments = ticket.get("comments")
		self.assignedto = ticket.get("assignedto")
		self.resolutions = ticket.get("resolutions")
		self.start = ticket.get("start")
		self.end = ticket.get("end")
		self.priority = ticket.get("priority")


	def get_dict(self):
		return_val={'id': self.id, 'title': self.title,
					'category': self.category, 'status': self.status,
					'description': self.description, 'reporter': self.reporter, 'comments': self.comments,
					'assignedto': self.assignedto, 'resolutions': self.resolutions, 'start': self.start,
					'end': self.end, 'description' : self.description
					}
		return return_val