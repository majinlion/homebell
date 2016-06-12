from app import app
from pymongo import MongoClient
import json
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client.tms


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
	return "find"

@app.route('/get_users')
def get_users():
	return "get users"

@app.route('/change_status')
def change_status():
	return "change _status"

@app.route('/history')
def history():
	return "history"