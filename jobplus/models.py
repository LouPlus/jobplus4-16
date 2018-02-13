from flask_sqlalchemy import SQLAlechmey
from datetime import datetime

db=SQLAlchemy()

class User(db.Model):
    __tablename__='user'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=True,index=True,nullable=False)
    #other attributes need to be added here
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
