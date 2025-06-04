from flask import Flask
from blueprints import admin_dashboard

app = Flask(__name__)


app.register_blueprint(admin_dashboard.app, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
