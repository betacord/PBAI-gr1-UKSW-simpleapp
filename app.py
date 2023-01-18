from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from secrets import token_hex

from resources.event import Event, EventList
from resources.user import UserLogin

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = token_hex(32)
app.config['SECRET_KEY'] = token_hex(32)
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
jwt = JWTManager(app)

api.add_resource(Event, '/event/<int:id_>')
api.add_resource(EventList, '/events')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    app.run(port=5000)
