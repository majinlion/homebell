
'''
Every software firm uses some sort of ticketing system to easily track the tasks that are being performed.
A user must be able to create and update a ticket (with title, description, category, Priority, Status, Resolution, 
	Start date/End date , Reporter etc). Also the ticket should be assignable to a user. User must have the ability to 
comment on the ticket. There must be feature to get all the tickets for a user and get comments for the tickets as well. 
In addition, there must be ability to filter them based on assigned user, status, resolution or start/end date. 

Hints-
  - Create new tickets
  - Assign a ticket to a user
  - Change status or resolution of a ticket
  - Get all tickets associated with user (with filtering and pagination options)
  - Fetch comments associated with the ticket (with pagination option)

Bonus points:
- Should support the feature to track and show the activity history
- Add Tests or perform TDD

'''



tickets : {
	"title": string,
	"description" : string,
	"category" : string,
	"Priority" : string,
	"Status" : string,
	"Resolution" : string,
	"Start" : datetime,
	"End" : datetime,
	"Reporter" : string,
	"AssignedTo" : string,
	"Comments" : [string]
}
{
	"_id" : ObjectId("575d4fb62fa42b8828600b2b"),
	"title" : "fanproblem",
	"description" : "Fan's regulator is not working",
	"category" : "rew",
	"priority" : "normal",
	"status" : "acknowledge",
	"resolutions" : "not fixed",
	"start" : "20160101",
	"end" : "00000000",
	"reporter" : "amit",
	"assignedto" : "karthik",
	"comments" : [
		"fix soon"
	]
}

{
	"_id" : ObjectId("575d4fb62fa42b8828600b2b"),
	"title" : "fanproblem",
	"description" : "Fan's regulator is not working",
	"category" : "rew",
	"priority" : "normal",
	"status" : "acknowledge",
	"resolutions" : "not fixed",
	"start" : "20160101",
	"end" : "00000000",
	"reporter" : "amit",
	"assignedto" : "karthik",
	"comments" : [
		"fix soon"
	]
}