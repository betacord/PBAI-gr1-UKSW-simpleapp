from flask_restful import Resource


class Event(Resource):
    @classmethod
    def get(cls, id_: int) -> any:
        event = {
            'id': id_,
            'name': 'test event',
            'description': 'any test description of test event'
        }

        return event
