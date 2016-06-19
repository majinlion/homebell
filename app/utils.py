from bson.objectid import ObjectId

def get_match_query(req_params):
	match_query = {}
	if '$and' not in match_query:
	    match_query['$and'] = []

	if '$or' not in match_query:
	    match_query['$or'] = []

	if'user' in req_params:
		match_query['$or'].append({'reporter':str(req_params['user'])})
		match_query['$or'].append({'assignedto':str(req_params['user'])})

	if 'title' in req_params and req_params['title']:
		match_query['$and'].append({'title':req_params['title']})
		#match_query["title"] = req_params['title']

	if '_id' in req_params and req_params['_id']:
		match_query['$and'].append({'_id':ObjectId(req_params['_id'])})

	if 'category' in req_params and req_params['category']:
		match_query['$and'].append({'category':req_params['category']})
		#match_query["category"] = req_params['category']

	if 'priority' in req_params and req_params['priority']:
		match_query['$and'].append({'priority':req_params['priority']})
		#match_query["priority"] = req_params['priority']

	if 'status' in req_params and req_params['status']:
		match_query['$and'].append({'status':req_params['status']})
		#match_query["status"] = req_params['status']

	if 'resolutions' in req_params and req_params['resolutions']:
		match_query['$and'].append({'resolutions':req_params['resolutions']})
		#match_query["resolutions"] = req_params['resolutions']


	if 'start' in req_params and req_params['start'] != "":
	    date_from = {'start': {"$gte": req_params['start']}}
	    match_query['$and'].append(date_from)

	if 'end' in req_params and req_params['end'] != "":
	    date_to = {'end': {"$lte": req_params['end']}}
	    match_query['$and'].append(date_to)

	if not len(match_query['$or']):
		match_query.pop(['$or'])

	if not len(match_query['$and']):
	    match_query.pop("$and")

	print match_query
	return match_query
