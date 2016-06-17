def get_match_query(req_params):
	match_query = {}
	if 'title' in req_params:
		match_query["title"] = req_params['title']
	if 'category' in req_params:
		match_query["category"] = req_params['category']
	if 'priority' in req_params:
		match_query["priority"] = req_params['priority']
	if 'status' in req_params:
		match_query["status"] = req_params['status']
	if 'title' in req_params:
		match_query["title"] = req_params['title']
	if 'resolutions' in req_params:
		match_query["resolutions"] = req_params['resolutions']

	if '$and' not in match_query:
	    match_query['$and'] = []

	if 'start' in req_params and req_params['start'] != "":
	    date_from = {'start': {"$gte": req_params['start']}}
	    match_query['$and'].append(date_from)

	if 'end' in req_params and req_params['end'] != "":
	    date_to = {'end': {"$lte": req_params['end']}}
	    match_query['$and'].append(date_to)

	if not len(match_query['$and']):
	    match_query.pop("$and")

	return match_query
