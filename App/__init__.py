from flask import Flask, session, Blueprint
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///storage.db"
db= SQLAlchemy(app)

from App.controller import default