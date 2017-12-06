import config
from dash_auth import FlaskLoginAuth
from app.server import server
from app.app import app

auth = FlaskLoginAuth(app, use_default_views=True, users=config.DATABASE_PATH, auto_hash=True)

if __name__ == '__main__':
	server.run(port=8050, debug=True)
