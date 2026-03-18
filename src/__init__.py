from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# blueprints
from src.accounts.views import accounts_bp
from src.cores.views import core_bp
# registering them
app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
