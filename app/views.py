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
	#return render_template('index.html')
	#clusters = [Cluster([p]) for p in initial]
	active_tickets = db.tickets.find()
	l = []
	for i in active_tickets:
		l.append(i)
	activeTickets = [(Ticket(i)) for i in l]
	for i in activeTickets:
		print i.title
	#activeTickets = [Ticket(i) for i in active_tickets]
	#print activeTickets
	return render_template('index.html', tickets=activeTickets)
	#return (active_tickets[0]["title"])
	#return render_template('index.html',
	#    active_tickets=active_tickets)


@app.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
	if request.method == 'GET':
		return render_template('create.html')
	if request.method == 'POST':
		#print request.form.items()
		dic = {}
		for k,v in request.form.items():
			dic[k] = v
		op = json.dumps(dic)
		print op
		try:
			http_response = CustomResponse(200,"Creating tickets successful", manager.create_ticket(op))
			return http_response.get_success_message()
		except Exception as e:
			print e
			http_response = CustomResponse(11111,"There was some exception in creating ticket" , "")
			return http_response.get_failed_message()


@app.route('/assign_ticket', methods=['POST'])
def assign_tickets():
	try:
		http_response = CustomResponse(200,"Ticket assigned", manager.assign_ticket(request.data))
		return http_response.get_success_message()
	except:
		http_response = CustomResponse(11111,"There was some exception in assigning ticket" , "")
		return http_response.get_failed_message()

@app.route('/get_tickets', methods=['GET', 'POST'])
def get_tickets():
	if request.method == 'GET':
		return render_template('gettickets.html')
	if request.method == 'POST':
		#print request.form.items()
		dic = {}
		for k,v in request.form.items():
			dic[k] = v
		op = json.dumps(dic)
		print op
	return manager.get_tickets(op)
	try:
		http_response = CustomResponse(200,"Get tickets successful" , manager.get_tickets(op))
		return http_response.get_success_message()
	except Exception as e:
		print e
		http_response = CustomResponse(11111,"There was some exception in getting tickets" , "")
		return http_response.get_failed_message()

@app.route('/get_users')
def get_users():
	return "get users not implemented"

@app.route('/change_status', methods=['POST'])
def change_status():
	return manager.change_status(request.data)
	return "change _status"

@app.route('/change_resolution', methods=['POST'])
def change_resolution():
	return manager.change_resolution(request.data)


@app.route('/history')
def history():
	return "history"