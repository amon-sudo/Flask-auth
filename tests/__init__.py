import os 

from flask_testing import TestCase

from src.accounts.models import User


class BaseTetsCase(TestCase):
    def __init__(self):
        app.config.from_object("config.TestingConfig")
        return app
    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        
        db.session.commit()
        
       
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        testdb_path = 