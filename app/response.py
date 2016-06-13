'''
This will create the response for client
'''
from json import dumps
from flask import Response
from jsonencoder import JSONEncoder

class CustomResponse():

    def __init__(self, status_code, status_msg, result):
        self.status_code = status_code
        self.status_msg = status_msg
        self.result = result

    def get_success_message(self):
        response = {}
        response["status"] = {}
        response["status"]["statusType"] = "SUCCESS"
        response["status"]["statusMessage"] = self.status_msg
        response["status"]["statusCode"] = self.status_code

        response["data"] = self.result
        return Response(dumps(response,sort_keys=False, indent=4,cls =JSONEncoder),mimetype="application/json")

    def get_failed_message(self):
        response = {}
        response["status"] = {}
        response["status"]["statusType"] = "FAILURE"
        response["status"]["statusMessage"] = self.status_msg
        response["status"]["statusCode"] = self.status_code

        response["data"] = self.result
        return Response(dumps(response),mimetype="application/json")
