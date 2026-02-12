# Author : ysh
# 2025/11/17 Mon 17:37:07
from core.general import *
from lib.general import *

from flask import Blueprint, send_file, make_response, redirect, abort, request

app = Blueprint('test', __name__)

@app.route('/echo', methods = ['GET'])
def echo():
    log.debug('TEST/echo')(dict(request.values))
    print(request.values)
    return request.values

@app.route('/beat', methods = ['GET', 'POST'])
def heart_beat():
    return ok()