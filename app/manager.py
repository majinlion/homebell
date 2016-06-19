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

#TODO1 : filtering options wrt different fields -> #DONE
#TODO2 : pagination options from frontentd

def get_tickets(input):
	try:
		data = json.loads(input)
	except Exception as e:
		print e
	result =[]
	match_str = {}
	match_str = utils.get_match_query(data)

	'''
	user = data["user"]
	match_str={"$match": {"$or":  [{"reporter": user},{"assignedto" : user} ] }}
	'''
	
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
	print "here"
	x = db.tickets.aggregate(pipeline=pipe)
	print x
	print "2"
	result = list(x)
	print "3"
	return result
	#return json.dumps(x)
	#return json.dumps(result)

def get_ticket_info(input):
	result =[]
	try:
		print "123"
		c = db.tickets.find({"_id":ObjectId(input['_id'])})
		print "234"
	except Exception as e:
		print "error"
		print e
	print c[0]
	print "sadfsdf"
	result = list(c)
	return result
	#return json.dumps(c[0])

#todo : add tests
def create_ticket(input):
	data = json.loads(input)
	try:
		db.tickets.insert_one(data)
		return "Ticket Created"
	except Exception as e:
		print e
		return ""


def update_ticket(input):
	data = json.loads(input)
	print "in update ticket"
	print data["id"]
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
		return "Ticket Updated"
	except Exception as e:
		print e
		return "Failed To Update"

'''
def change_status(input):
	data = json.loads(input)
	try:
		db.tickets.update_one(
			{
				"_id" : data["_id"]
			},
			{
				"$set":
				{
					"status" : data["status"]
				}
			}
			)
		return "Status Updated"
	except Exception as e:
		print e
		return ""


def change_resolution(input):
	data = json.loads(input)
	try:
		db.tickets.update_one(
			{
				"_id" : data["_id"]
			},
			{
				"$set":
				{
					"resolutions" : data["resolutions"]
				}
			}
			)
		return "Resolution Updated"
	except Exception as e:
		print e
		return ""

'''

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