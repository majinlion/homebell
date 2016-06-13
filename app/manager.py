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


def get_tickets():

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

def get_tickets(user):
	output = {}
	result =[]
	try:
		output = db.tickets.find({"reporter" : user})
		for i in output:
			result.append(i)
	return result