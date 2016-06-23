from app import app
from pymongo import MongoClient
import json
from bson import ObjectId
import requests
from jsonencoder import JSONEncoder
from bson import BSON
from bson import json_util,ObjectId
from response import *
import utils
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost:27017/')
db = client.tms


def get_tickets(input):
	try:
		data = json.loads(input)
	except Exception as e:
		print e
	result =[]
	match_str = {}
	match_str = utils.get_match_query(data)
	pipe = []
	pipe.append({"$match" : match_str})
	pipe.append(
				{"$project": {
	            "_id": 1,
	            "title" : 1,
	            "description" : 1,
				"category" : 1,
				"priority" : 1,
				"status" : 1,
				"resolutions" : 1,
				"start" : 1,
				"end" : 1,
				"reporter" : 1,
				"assignedto" : 1,
				"comments" : 1
	            }})
	x = db.tickets.aggregate(pipeline=pipe)
	result = list(x)
	return result

def get_ticket_info(input):
	result =[]
	try:
		c = db.tickets.find({"_id":ObjectId(input['_id'])})
	except Exception as e:
		print e
	result = list(c)
	return result

def create_ticket(input):
	data = json.loads(input)
	try:
		_id = db.tickets.insert(data)
		db.history.insert_one(
			{
			"_id" : ObjectId(_id),
			"dataArray" : [data]
			}
			)
		return "Ticket Created"
	except Exception as e:
		return e


def update_ticket(input):
	data = {}
	data = json.loads(input)
	try:
		db.tickets.update_one(
			{
				"_id" : ObjectId(data["id"])
			},
			{
				"$set": 
				{
            		"assignedto": data["assignedto"],
            		"status" : data["status"],
            		"resolutions" : data["resolutions"],
            		"assignedto" : data["assignedto"]
            	}
            }
		)
		a = db.history.update_one(
			{
			"_id" : ObjectId(data["id"])
			},
			{
				"$push" : {"dataArray" : data}
			}
			)
		return "Ticket Updated"
	except Exception as e:
		print e
		return "Failed To Update"

def comment_ticket(input):
	data = json.loads(input)
	try:
		db.tickets.update_one(
			{
				'_id' :ObjectId(data["id"])
			},
			{
				'$push' : {'comments' : data['comments']}
			}
		)
		db.history.update_one(
			{
				"id" : data["id"]
			},
			{
				"$push" : {"dataArray" : data}
			}
			)
		return "Comment Successful"
	except Exception as e:
		print e
		return "Failed to Comment"

def get_history(ticketId):
	result =[]
	try:
		c = db.history.find({"_id":ObjectId(ticketId)})
	except Exception as e:
		print e
	result = list(c)
	return result


def post(url,data,headers):
    ''' HTTP POST REQUEST. Returns response object '''
    logger.debug('Post Request')
    logger.debug(data)
    req = requests.post(url, headers=headers, data=(data))
    logger.debug( req.text)
    return req.text

def get(url):
    ''' HTTP GET REQUEST. Returns response object '''
    req = requests.get(url);
    return req.text;