from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from blueprints import admin_dashboard
from blueprints import main
import ext
from models import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ljd829SSS4372398h###sdasdasudh%$^$123123asuidahsd'

ext.db.init_app(app)
migrate = Migrate(app, ext.db)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

app.register_blueprint(admin_dashboard.app, url_prefix='/admin')
app.register_blueprint(main.app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
