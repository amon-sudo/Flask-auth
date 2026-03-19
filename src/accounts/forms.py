from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.accounts.models import User
