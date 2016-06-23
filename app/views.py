from app import app
from pymongo import MongoClient
import json
from bson import ObjectId
from flask import request, render_template
import requests
from jsonencoder import JSONEncoder
from bson import BSON
from bson import json_util,ObjectId
from response import *
from tickets import *
import manager
client = MongoClient('mongodb://localhost:27017/')
db = client.tms



'''
Every software firm uses some sort of ticketing system to easily track the tasks that are being performed.
A user must be able to create and update a ticket (with title, description, category, Priority, Status, Resolution, 
	Start date/End date , Reporter etc). Also the ticket should be assignable to a user. User must have the ability to
	 comment on the ticket. There must be feature to get all the tickets for a user and get comments for the tickets
	  as well. In addition, there must be ability to filter them based on assigned user, status, resolution or start/end date. 

Hints-
  - Create new tickets
  - Assign a ticket to a user
  - Change status or resolution of a ticket
  - Get all tickets associated with user (with filtering and pagination options)
  - Fetch comments associated with the ticket (with pagination option)

Bonus points:
- Should support the feature to track and show the activity history
- Add Tests or perform TDD

You are free to use any technologies you want. Create database structure to support the feature. 
'''

@app.route('/')
def home_page():
	active_tickets = db.tickets.find()
	l = []
	for i in active_tickets:
		l.append(i)
	activeTickets = [(Ticket(i)) for i in l]
	return render_template('index.html', tickets=activeTickets)


@app.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
	if request.method == 'GET':
		return render_template('create.html')
	if request.method == 'POST':
		dic = {}
		for k,v in request.form.items():
			dic[k] = v
		op = json.dumps(dic)
		try:
			http_response = CustomResponse(200,"Creating tickets successful", manager.create_ticket(op))
			return http_response.get_success_message()
		except Exception as e:
			print e
			http_response = CustomResponse(11111,"There was some exception in creating ticket" , "")
			return http_response.get_failed_message()

@app.route('/comment_ticket', methods = ['GET', 'POST'])
def comment_ticket():
	ticketId = request.args.get('ticketId')
	try:
		skipValue = int(request.args.get('skipValue'))
	except:
		skipValue = 0
	op = {}
	op['_id'] = ticketId
	l = []
	current_ticket = db.tickets.find({"_id":ObjectId(op['_id'])})
	for i in current_ticket:
		l.append(i)
	ticket_info = [(Ticket(i)) for i in l]

	if request.method == 'GET':
		ct = 0
		for comment in ticket_info[0].comments:
			ct+=1
		maxValue = min(skipValue+5,ct)
		comment_list = ticket_info[0].comments[skipValue:maxValue]
		return render_template('commentTicket.html', ticketInfo = ticket_info[0],comment_list = comment_list)

	if request.method == 'POST':
		dic = {}
		for k,v in request.form.items():
			dic[k] = v
		op = json.dumps(dic)
	try:
		return manager.comment_ticket(op)
	except:
		http_response = CustomResponse(11111,"There was some exception in commenting on the ticket" , "")
		return http_response.get_failed_message()

@app.route('/assign_ticket', methods=['GET', 'POST'])
def assign_tickets():
	ticketId = request.args.get('ticketId')
	op = {}
	op['_id'] = ticketId
	l = []
	current_ticket = db.tickets.find({"_id":ObjectId(op['_id'])})
	for i in current_ticket:
		l.append(i)
	ticket_info = [(Ticket(i)) for i in l]
	if request.method == 'GET':
		return render_template('updateTicket.html', ticketInfo = ticket_info[0])

	if request.method == 'POST':
		dic = {}
		for k,v in request.form.items():
			dic[k] = v
		op = json.dumps(dic)
	try:
		return manager.update_ticket(op)
	except:
		http_response = CustomResponse(11111,"There was some exception in updating ticket" , "")
		return http_response.get_failed_message()

@app.route('/get_tickets', methods=['GET', 'POST'])
def get_tickets():
	if request.method == 'GET':
		return render_template('gettickets.html')
	if request.method == 'POST':
		dic = {}
		for k,v in request.form.items():
			dic[k] = v
		op = json.dumps(dic)
	try:
		return_value = manager.get_tickets(op)
		l = []
		for i in return_value:
			l.append(i)
		ticket_info = [(Ticket(i)) for i in l]
		return render_template('ticketList.html', tickets = ticket_info)
	except Exception as e:
		print e
		http_response = CustomResponse(11111,"There was some exception in getting tickets" , "")
		return http_response.get_failed_message()


@app.route('/history', methods=['GET','POST'])
def history():
	return manager.get_history()