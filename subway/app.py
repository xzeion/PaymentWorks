#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response, render_template, request
import logging, os, requests, pdb

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True

logging.basicConfig(
    level=logging.DEBUG,
    format = f'%(levelname)s: %(message)s' )
log = app.logger.debug

root_uri="http://api-v3.mbta.com/"

def subway_routes():
    resp = requests.get(root_uri + 'routes')
    return [x for x in resp.json()['data'] if x['attributes']['type'] == 1] if resp.ok else []

def stops(route_id):
    if not route_id:
        return []
    stops = requests.get(root_uri + f'stops?filter[route]={route_id}')
    return [stop['attributes']['name'] for stop in stops.json()['data']] if stops.ok else []

def validate(routes,route):
    return route if route in routes else None

@app.route('/',methods=['GET','POST'])
def home():
    routes = subway_routes()
    st = stops(validate([x['id'] for x in routes],request.values.get('line')))

    return render_template(
        'home.html',
        data=routes,
        line=request.values.get('line',''),
        stops=st or [],
    )
    


'''
given more time I would:
* build out key tables so data like id=1 would be better 
represented as meaning 'subway lines' for example

'''
