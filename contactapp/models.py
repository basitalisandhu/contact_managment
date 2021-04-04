from contactapp import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin



class Contacts(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20),index=True)
    last_name = db.Column(db.String(64),  index=True)
    username = db.Column(db.String(64),  index=True)
    
    def __init__(self, first_name,last_name, username):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        
    def __repr__(self):
        return f"UserName: {self.username}"

class Email(db.Model):
    # Setup the relationship to the User table
    contacts = db.relationship(Contacts)
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)
    email = db.Column(db.String(140), nullable=False)
    
    def __init__(self, email,user_id):
        self.email = email
        self.user_id =user_id
