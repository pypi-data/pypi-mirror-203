from flask import request, jsonify
from functools import wraps
from flask_jwt_extended import get_current_user
from enum import Enum
import SIOTC.Operations as op
import re

# Checks what type of data is being sent and returns correct object
def CheckContentType():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        print('Json Message received')
        return request.json
    elif 'text/' in content_type:
        print('Text Message received')
        return request.data.decode('utf-8')
    else:
        return 'Content-Type not supported', 415
 

# Verifies that the json payload contains correct data, CHANGE ACCORDING TO DECIDED MESSAGE 
def VerifyJsonContent(content): 
    if(content['mac-adress']):
        print('Message verified')
        return True
    else:
        print('Content not abled to be verified or it does not match the intended format')
        return False
    
# Verifies that the string payload contains correct data, CHANGE ACCORDING TO DECIDED MESSAGE    
def VerifyStringContent(content):
    if("sys" in content):
        print('String Message Verified')
        return True
    else:
        print('Content not abled to be verified or it does not match the intended format')
        return False
    
def VerifyMacContent(content):
    regex_pattern = '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.match(regex_pattern, content))

def admin_required(current_user):
    @wraps(current_user)
    def wrapper(current_user):
        user = current_user.id
        roleId = user.role_id

        if roleId != op.GetTable('roles').query.filter_by(name='System Administrator').first():
            return jsonify({'message': 'You do not have permission to access this endpoint.'}), 403
        return current_user
    return wrapper

def ownership_required(current_user, table):
    @wraps(current_user, table)
    def wrapper(current_user, table):
        user = current_user.id
        deviceID = op.GetTable(table).query.filter_by(id=current_user.id).first()

        if user != deviceID.user_id:
            return jsonify({'message': 'User does not own device.'}), 403
        return current_user
    return wrapper