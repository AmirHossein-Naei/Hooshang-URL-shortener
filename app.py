from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from blueprints import admin_dashboard
import ext

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ext.db.init_app(app)
migrate = Migrate(app, ext.db)

app.register_blueprint(admin_dashboard.app, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
