from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)

from flask import render_template, flash, redirect, request, jsonify
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import HiddenField, validators, TextAreaField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    body = TextAreaField('body', [validators.required(), validators.length(max=200)])
    choices = HiddenField('choices', [validators.required()])

class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256), nullable=False)
    choices = db.relationship("Choice", backref='parent')
    choiceLink = db.relationship("LinkToNext", backref='nScene', uselist=False)

    def __init__(self, **kwargs):
        for i in kwargs:
            exec(f"self.{i}='{kwargs[i]}'")
        
        db.session.add(self)
        db.session.commit()

    def link(self, obj):
        self.choices.append(obj)
        db.session.commit()

    def linkChoice(self, obj):
        link = obj.sceneLink
        self.choiceLink = link
        db.session.commit()

    @property
    def prevChoice(self):
        if self.choiceLink:
            return self.choiceLink.pChoice
        else:
            return self.choiceLink

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(18), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('scene.id'))
    sceneLink = db.relationship("LinkToNext", backref='pChoice', uselist=False)

    def __init__(self, **kwargs):
        for i in kwargs:
            exec(f"self.{i}='{kwargs[i]}'")
        
        db.session.add(self)
        self.createLink()

    def createLink(self):
        newLink = LinkToNext()
        db.session.add(newLink)
        self.sceneLink = newLink
        db.session.commit()

    @property
    def nextScene(self):
        if self.sceneLink:
            return self.sceneLink.nScene
        else:
            return self.sceneLink
    
class LinkToNext(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    choiceTo_id = db.Column(db.Integer, db.ForeignKey('choice.id'))
    nextScene_id = db.Column(db.Integer, db.ForeignKey('scene.id'))
    

db.create_all()
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/story', methods=['POST', 'GET'])
def story():
    scene = int(request.values.get('q'))
    a = Scene.query.filter_by(id=scene).first()

    return render_template('story.html', scene=a, choices=a.choices)
    
@app.route('/newScene', methods=['POST', 'GET'])
def newscene():
    q = int(request.values.get('q'))
    choice = Choice.query.filter_by(id = q).first()
    if not choice.nextScene:
        form = MyForm()
        if form.validate_on_submit():
            choices = form.choices.data.split('-*#*-')
            s = Scene(body=form.body.data)
            s.linkChoice(choice)
            for i in choices:
                s.link(Choice(text=i))

            return redirect('/index')

        return render_template('newScene.html', choice=choice, form=form)
    else:
        redirect('/index')