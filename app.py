from flask import Flask
from flask_restful import Api

from resources.event import Event, EventList

app = Flask(__name__)
api = Api(app)

# GET: 127.0.0.1:5000/event/1
api.add_resource(Event, '/event/<int:id_>')
api.add_resource(EventList, '/events')  # 127.0.0.1:5000/events

if __name__ == '__main__':
    app.run(port=5000)
