from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy_utils import database_exists
#from sqlalchemy.orm import relationships

#creo la variable que se va a conectar a la base de datos
db = SQLAlchemy()

# modelos de tablas de mi base de datos
class Animal(db.Model):
    __tablename__ = "animals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    cientific_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, nullable=False) 

    def __str__(self):
        return f'name: (self.name)'


    

