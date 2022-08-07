from flask import Flask, Response, render_template, request
import requests

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True

root_uri="http://api-v3.mbta.com/"


def subway_routes(path='routes'):
    resp = requests.get(root_uri + path)
    #NOTE: type == 1 filters the data to subway routes only
    return [x for x in resp.json()['data'] if x['attributes']['type'] == 1] if resp.ok else []


def stops(route_id):
    if not route_id: return []
    stops = requests.get(root_uri + f'stops?filter[route]={route_id}')
    return [(stop['attributes']['name'],stop['attributes']['address']) for stop in stops.json()['data']] if stops.ok else []


def validate(routes, route):
    '''validates that the route returned to us from the page is one of the avaliable routes'''
    return route if route in routes else None


@app.route('/',methods=['GET','POST'])
def home():
    return render_template(
        'home.html',
        data=subway_routes() if request.method == 'GET' else [],
        line=request.values.get('line',''),
        stops=stops(validate([x['id'] for x in subway_routes()],request.values.get('line')))
    )
