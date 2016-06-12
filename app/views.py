from app import app
from pymongo import MongoClient
import json
from bson import ObjectId
import requests
from jsonencoder import JSONEncoder
from bson import BSON
from bson import json_util,ObjectId
from response import *
client = MongoClient('mongodb://localhost:27017/')
db = client.tms




'''
Every software firm uses some sort of ticketing system to easily track the tasks that are being performed.
A user must be able to create and update a ticket (with title, description, category, Priority, Status, Resolution, Start date/End date , Reporter etc). Also the ticket should be assignable to a user. User must have the ability to comment on the ticket. There must be feature to get all the tickets for a user and get comments for the tickets as well. In addition, there must be ability to filter them based on assigned user, status, resolution or start/end date. 

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
	active_tickets = db.tickets.find({'active': 'true'})
	return (active_tickets[0]["title"])
	#return render_template('index.html',
	#    active_tickets=active_tickets)

@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/create_ticket')
def create_ticket():
	return "ticket_created"


@app.route('/assign_ticket')
def assign_tickets():
	return "ticket assigned"

@app.route('/get_tickets')
def get_tickets():
	try:
		http_response = CustomResponse(200,"Get tickets successful" , manager.get_tickets(request.data))
		return http_response.get_success_message()
	except:
		http_response = CustomResponse(11111,"There was some exception in getting tickets" , "")
		return http_response.get_failed_message()

@app.route('/get_users')
def get_users():
	return "get users"

@app.route('/change_status')
def change_status():
	return "change _status"

@app.route('/history')
def history():
	return "history"