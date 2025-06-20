from enum import Enum
from utils.message_codes import *
from flask import Response
import json

class StatusCode():
# Successful Status codes
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206
    # Client Error Status Codes
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    CONFLICT = 409
    UNSUPPORTED_MEDIA_TYPE = 415
    UNPROCESSABLE_ENTITY = 422
    # Server Error Status Codes
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 5001
    BAD_GATEWAY = 502
    TIMEOUT = 503
    
class ServerResponse(object):   
    """Handle server responses
    
    Keyword arguments:
    data -- values returned
    message -- description of the response
    message_code -- multilanguage code 
    status -- integer http status code
    """
    def __new__(cls, data=None, message=None, message_code=None, status=StatusCode.OK):
        cls.data = data
        cls.message = message
        cls.message_code = message_code
        cls.status = status
        return cls.__server_response(cls)


    def __server_response(self):
        self.__get_default_msg(self)
        body = {
            'data': self.data,
            'message': self.message,
            'message_code': self.message_code
        }
        return Response(json.dumps(body), mimetype='application/json', status=int(self.status))

    
    def __get_default_msg(self):
        status = self.status
        if not self.message:
            if  status == StatusCode.OK:
                self.message = 'Successfully requested'
                self.message_code = OK_MSG
            elif status == StatusCode.CREATED:
                self.message = 'Successfully created'
                self.message_code = CREATED_MSG
            elif status == StatusCode.NOT_FOUND:
                self.message = 'Record not found'
                self.message_code = NOT_FOUND_MSG
            elif status == StatusCode.CONFLICT:
                self.message = 'Conflict error with the request'
                self.message_code = CONFLICT_MSG
            elif status == StatusCode.UNPROCESSABLE_ENTITY:
                self.message = 'Unprocessable entity'
                self.message_code = UNPROCESSABLE_ENTITY_MSG
            elif status == StatusCode.INTERNAL_SERVER_ERROR:
                self.message = 'Internal server error'
                self.message_code = INTERNAL_SERVER_ERROR_MSG
            elif status == StatusCode.TIMEOUT:
                self.message = 'Server timeout' 
                self.message_code = SERVER_TIMEOUT_MSG