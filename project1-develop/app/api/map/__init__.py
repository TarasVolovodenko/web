from geoalchemy2 import Geometry
from sqlalchemy import func, cast

from api.util import Singleton
from models import PollutionCategory, IssueState, Issue


class MapWrapper(metaclass=Singleton):
    def __init__(self, session_maker):
        self.session_maker = session_maker

    def get_pollution_types(self):
        session = self.session_maker()
        filters = session.query(PollutionCategory).all()
        return filters

    def get_issue_state_filters(self):
        session = self.session_maker()
        filters = session.query(IssueState).all()
        return filters

    def get_issues_short(self, bbox, count, distance, lat, lon, pollution_types, state_types):
        session = self.session_maker()
        if bbox and len(bbox := bbox.split('),(')) > 1:
            bbox = [list(map(float, i.strip('()').split(','))) for i in bbox]
            if len(bbox) == 2:
                bbox = [bbox[0], (bbox[1][0], bbox[0][1]), bbox[1], (bbox[0][0], bbox[1][1])]
            bbox.append(bbox[0])
        else:
            bbox = None
        query_location = Issue.location
        if bbox:
            user_location = f'POLYGON(({", ".join(" ".join(map(str, i)) for i in bbox)}))'
            user_location = func.ST_GeomFromEWKT(f'SRID=4326;{user_location}')
            _filter = func.ST_Within(cast(Issue.location, Geometry), user_location)
        else:

            user_location = f'POINT({lat} {lon})'
            _filter = func.ST_DWithin(query_location, user_location, distance)
        filtered = session.query(Issue).filter(_filter)
        if pollution_types:
            filtered = filtered.filter(Issue.pollution_category_id.in_(pollution_types))
        if state_types:
            filtered = filtered.filter(Issue.state_id.in_(state_types))
        issues = filtered.order_by(Issue.pollution_rating.desc()).limit(count).all()
        return issues

    def get_issues(self, ids):
        session = self.session_maker()
        issues = session.query(Issue).filter(Issue.id.in_(ids)).all()
        return issues
