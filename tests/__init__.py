import os 

from flask_testing import TestCase

from src.accounts.models import User


class BaseTetsCase(TestCase):
    def __init__(self):
        app.config.from_object("config.TestingConfig")
        return app
    def setUp(self):
        db.create_all()
       
        