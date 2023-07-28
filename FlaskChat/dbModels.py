from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from DatabaseFunc import *

user_group_assoc = db.Table(
    'User Groups',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uName = db.Column(db.String(18), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    passHash = db.Column(db.String(128), nullable=False)
    groups = db.relationship('Group', secondary=user_group_assoc, backref='users')

    def link(self, obj):
        self.groups.append(obj)

    def unlink(self, obj):
        self.groups.remove(obj)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(18), nullable=False)
    joinPass = db.Column(db.String(8), unique=True, nullable=False)
    chatqueues = db.relationship('Chat', backref='parent')


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    groupId = db.Column(db.Integer, db.ForeignKey('group.id'))
    posts = db.relationship('Post', backref='chatarea')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(50), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
