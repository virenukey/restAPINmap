#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import socket
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
import json
import xmltodict

app = Flask(__name__)

# start a new nmap scan on localhost with some specific options
def do_scan(targets, options, **kwagrs):
    nmproc = NmapProcess(targets, options, event_callback=None, safe_mode=True, fqp=None)
    rc = nmproc.run()
    if nmproc.rc == 0:
	jsonString = json.dumps(xmltodict.parse(nmproc.stdout), indent=4)
    	return jsonString
    else:
	return nm.stderr

@app.route('/todo/api/nmap', methods=['GET'])
def run_scan():
    target = str(request.args['target'])
    options = str(request.args['options'])
    report = do_scan(target, options)
    return report

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'bad request'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'bad request'}), 404)

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

if __name__ == '__main__':
    app.run(host=host_ip, port=5002, debug=True)

