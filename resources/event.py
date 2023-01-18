from flask_restful import Resource
from flask import request


class Event(Resource):
    @classmethod
    def get(cls, id_: int) -> any:
        event = {
            'id': id_,
            'name': 'test event',
            'description': 'any test description of test event'
        }

        return event

    @classmethod
    def post(cls, id_: int) -> any:
        event_json = request.get_json()
        event_json['id'] = id_

        return event_json, 201


class EventList(Resource):
    @classmethod
    def get(cls) -> any:
        return {
            'events': [
                {
                    'id': 0,
                    'name': 'test 1',
                    'description': 'test description 1',
                },
                {
                    'id': 1,
                    'name': 'test 2',
                    'description': 'test description 2',
                },
            ],
        }
