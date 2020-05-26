import json
import os
from datetime import timedelta
from functools import update_wrapper

from flask import Flask, make_response, request, current_app
from flask import Flask, request, Response
import sqlalchemy as sa
from shapely import wkb
from sqlalchemy.orm import sessionmaker

from models import Base
from api.issues import IssueWrapper
from api.events import EventWrapper
from api.users import UserWrapper
from api.map import MapWrapper

from api.views.UserView import user_api as user_blueprint
from api.views.IssueView import issue_api as issue_blueprint
from api.views.EventView import event_api as event_blueprint


def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    # use str instead of basestring if using Python 3.x
    if headers is not None and not isinstance(headers, list):
        headers = ', '.join(x.upper() for x in headers)
    # use str instead of basestring if using Python 3.x
    if not isinstance(origin, list):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """

        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/api/user/')
app.register_blueprint(issue_blueprint,url_prefix='/api/issue/')
app.register_blueprint(event_blueprint,url_prefix='/api/event/')


@app.route('/api/event/<int:id>', methods=['GET'])
@crossdomain(origin='*')
def event_info(id):
    valid_fields = [
        'id', 'issue', 'creator', 'datetime', 'comments', 'participants',
        'photos'
    ]

    fields = request.args.get('fields', None)
    if fields:
        fields = [i for i in fields.split(',') if i in valid_fields]
    else:
        fields = valid_fields

    event = EventWrapper().info(id, fields)
    response = json.dumps(event)

    return response


@app.route('/api/event/<int:id>/comments', methods=['GET'])
@crossdomain(origin='*')
def event_get_comments(id):
    valid_fields = ['id', 'text', 'datetime', 'author', 'origin', 'rating']

    offset = int(request.args.get('offset', 0))
    offset = max(offset, 0)
    limit = int(request.args.get('limit', 25))
    limit = min(25, limit)

    fields = request.args.get('fields', None)
    if fields:
        fields = [i for i in fields.split(',') if i in valid_fields]
    else:
        fields = valid_fields

    comments = EventWrapper().comments(id, fields, offset, limit)

    response = json.dumps(comments)
    return response


@app.route('/api/issue/<int:id>', methods=['GET'])
@crossdomain(origin='*')
def issue_info(id):
    valid_fields = [
        'id', 'title', 'description', 'state', 'date', 'creator',
        'approver', 'pollution_category', 'pollution_rating', 'budget',
        'comments', 'location', 'photos'
    ]

    fields = request.args.get('fields', None)
    if fields:
        fields = [i for i in fields.split(',') if i in valid_fields]
    else:
        fields = valid_fields

    issue = IssueWrapper().info(id, fields)
    response = json.dumps(issue)

    return response


@app.route('/api/issue/<int:id>/comments', methods=['GET'])
@crossdomain(origin='*')
def issue_get_comments(id):
    valid_fields = ['id', 'text', 'datetime', 'author', 'origin', 'rating']

    offset = int(request.args.get('offset', 0))
    offset = max(offset, 0)
    limit = int(request.args.get('limit', 25))
    limit = min(25, limit)

    fields = request.args.get('fields', None)
    if fields:
        fields = [i for i in fields.split(',') if i in valid_fields]
    else:
        fields = valid_fields

    comments = IssueWrapper().comments(id, fields, offset, limit)

    response = json.dumps(comments)
    return response


@app.route('/api/events', methods=['GET'])
def get_events():
    valid_fields = [
        'id', 'issue', 'datetime', 'comments', 'participants',
        'photos'
    ]

    fields = request.args.get('fields', None)
    if fields:
        fields = [i for i in fields.split(',') if i in valid_fields]
    else:
        fields = valid_fields

    events = EventWrapper().events_info(fields)

    response = json.dumps(events)
    return response


@app.route('/api/fixed', methods=['GET'])
def get_fixed():
    valid_fields = [
        'id', 'title', 'description', 'state', 'date', 'pollution_category', 'pollution_rating', 'budget',
        'comments', 'location', 'photos'
    ]

    fields = request.args.get('fields', None)
    if fields:
        fields = [i for i in fields.split(',') if i in valid_fields]
    else:
        fields = valid_fields

    fixed_issues = IssueWrapper().fixed_issues_info(fields)
    response = json.dumps(fixed_issues)
    return response


@app.route('/api/create-event', methods=['POST'])
def create_event():
    if not request.json:
        return Response(mimetype="application/json",
                        response=json.dumps({'Error': "Bad request."}),
                        status=400)

    response, result = EventWrapper().create_event(request.json)

    if not response:
        return Response(mimetype="application/json",
                        response=json.dumps(response),
                        status=500)

    return Response(mimetype="application/json",
                    response=json.dumps(response),
                    status=200)


@app.route('/api/getStateFilters', methods=['GET'])
@crossdomain(origin='*')
def get_state_type_filters():
    filters = MapWrapper().get_issue_state_filters()
    return json.dumps({i.id: i.state for i in iter(filters)}, separators=(',', ':'))


@app.route('/api/getFilters', methods=['GET'])
@crossdomain(origin='*')
def get_pollution_type_filters():
    filters = MapWrapper().get_pollution_types()
    return json.dumps({i.id: i.category for i in iter(filters)}, separators=(',', ':'))


@app.route('/api/getIssuesShort', methods=['GET'])
@crossdomain(origin='*')
def get_issues_short():
    pollution_types = request.args.get('pollution_type', '')
    if pollution_types:
        pollution_types = list(map(int, pollution_types.split(',')))
    state_types = request.args.get('state_type', '')
    if state_types:
        state_types = list(map(int, state_types.split(',')))
    count = min(int(request.args.get('count', 10)), 1000)
    bbox = request.args.get('bbox', '')
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))
    distance = float(request.args.get('distance', 1_000.0))
    issues = MapWrapper().get_issues_short(bbox, count, distance, lat, lon, pollution_types, state_types)
    return json.dumps({i.id: {'type': i.pollution_category.category,
                              'state': i.state.state,
                              'lon': (point := wkb.loads(bytes(i.location.data))).x,
                              'lat': point.y} for i in iter(issues)}, separators=(',', ':'))


@app.route('/api/getIssues', methods=['GET'])
@crossdomain(origin='*')
def get_issues():
    ids = request.args.get('ids', '')
    if ids:
        ids = list(map(int, ids.split(',')))
    issues = MapWrapper().get_issues(ids)
    return json.dumps({i.id: {'title': i.title,
                              'type': i.pollution_category.category,
                              'date': str(i.date),
                              'rating': i.pollution_rating,
                              'text': i.description,
                              'state': i.state.state,
                              'lon': (point := wkb.loads(bytes(i.location.data))).x,
                              'lat': point.y} for i in iter(issues)}, separators=(',', ':'))


if __name__ == '__main__':
    connstring = os.getenv('POSTGRES_URL')
    if connstring is None:
        print('Setup the POSTGRES_URL variable')
        exit(1)

    db = sa.create_engine(connstring, echo=True)
    Session = sessionmaker(bind=db)
    Base.metadata.create_all(db)

    IssueWrapper(Session)
    EventWrapper(Session)
    UserWrapper(Session)
    MapWrapper(Session)

    app.run()
