#The three main flask imports
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

#This just lets python process json
import json

#Threads are very import and I use it to create async
#I am fairly sure that this form of async will only work locally
#But that is the scope so it is fine
import threading

#This is imported incase I want to use it. I mainly used it for testing async.
import time

#Imports config file for setup use
from config import *
start = True
flask_app = Flask(__name__)
#This sets up the flask for the sql
flask_app.config.from_object(Config)

#This initialises the database
db = SQLAlchemy(flask_app)

#A bool which states whether the app is giving a role or not, cause otherwise two people can get same role
givingRole = False

#I save notes here
class savedNotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=True)
    text = db.Column(db.String(500))

#I save whether a role is taken or not here
class roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=True)
    taken = db.Column(db.Integer)

#I save library info here
class library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), index=True, unique=True)
    title = db.Column(db.String(24))
    stance = db.Column(db.String(24))
    creature = db.Column(db.String(24))
    templatetext = db.Column(db.String(200))
    persontext = db.Column(db.String(200))

#Creates database
db.create_all()

#A list of roles, so that when people connect the roles get dished out to you.
#It's first come first serve.
#Though if you force your buddy off from a role you may get that one when you reload.
rolesList = ['admin','command','operations','helm','science','tactics']

#A counter
rolesMod = 0

#Creates roles if they dont exist in database
for i in rolesList:
    if not roles.query.filter_by(name=i).all():
        u = roles(name = i, taken = 1)
        db.session.add(u)
        db.session.commit()

#Adds the borg to the library, \n in the text sections start a new paragraph.
if not library.query.filter_by(name='borg').all():
    u = library(name='borg',
                title='The Borg',
                stance='Hostile',
                creature='Alien',
                templatetext='The Borg are cyborgs, having outward appearances showing both mechanical and biological body parts. Individual Borg are referred to as drones and move in a robotic, purposeful style ignoring most of their environment, including beings they do not consider an immediate threat. Borg commonly have one eye replaced with a sophisticated ocular implant. Borg usually have one arm replaced with a prosthesis, bearing one of a variety of multipurpose tools in place of a humanoid hand. Since different drones have different roles, the arm may be specialized for myriad purposes such as medical devices, scanners, and weapons. Borg have flat, white skin, giving them an almost zombie-like appearance.\nSome Borg have been shown to be far stronger than humans, able to easily overpower most humans and similar species. Typical Borg have never been seen to run, instead moving in a deliberate fashion, never retreating. Borg are highly resistant to energy-based weapons, having personal shielding that instantly adapts to it. In various episodes, phasers and other energy weapons tend to quickly become ineffective as the Borg are able to adapt to specific frequencies once a ship or an individual drone is struck down. Later attempts to modulate phaser and other weapon frequencies have had limited success. Borg shields have, however, proven to be ineffective protection against projectile or melee weapons, but this could prove problematic, given the fact of space travel, specifically puncturing the hull with an errant shot.',
                persontext="Nanoprobes are microscopic machines that inhabit a Borg's body, bloodstream, and many cybernetic implants. The probes perform the function of maintaining the Borg cybernetic systems, as well as repairing damage to the organic parts of a Borg. They generate new technology inside a Borg when needed, as well as protecting them from many forms of disease. Borg nanoprobes, each about the size of a human red blood cell, travel through the victim's bloodstream and latch on to individual cells. The nanoprobes rewrite the cellular DNA, altering the victim's biochemistry, and eventually form larger, more complicated structures and networks within the body such as electrical pathways, processing and data-storage nodes, and ultimately prosthetic devices that spring forth from the skin. In \"Mortal Coil\", Seven of Nine states that the Borg assimilated the nanoprobe technology from \"Species 149\". In addition, the nanoprobes work to maintain and repair their host's mechanical and biological components on a microscopic level, allowing regenerative capabilities.\nThough used by the Borg to exert control over another being, reprogrammed nanoprobes were used by the crew of the starship Voyager in many instances as medical aids.\nThe capability of nanoprobes to absorb improved technologies they find into the Borg collective is shown in the Voyager episode \"Drone\", where Seven of Nine's nanoprobes are fused with the Doctor's mobile emitter that uses technology from the 29th century, creating a 29th-century drone existing outside the Collective, with capabilities far surpassing that of the 24th-century drones.\nThe Borg do not try to immediately assimilate any being with which they come to contact; in fact, Borg drones tend to completely ignore individuals that are identified as too weak to be an imminent threat or too inferior to be worth assimilating. Captain Picard and his team walk safely past a group of Borg drones in a scene from the film Star Trek: First Contact while the drones fulfill a programmed mission. In the Star Trek: Voyager episode \"Mortal Coil\", Seven of Nine told Neelix that the Kazon were \"unworthy\" of assimilation and would only serve to detract from the Borg's quest for perceived perfection.")
    db.session.add(u)
    db.session.commit()

#This is initialising the socket,
#the async mode section is probably not important but I put it in just incase
#socketio dislikes threading.
socketio = SocketIO(flask_app, async_mode='threading')

#This is the async function,
#I have made it so that it can make another function async
#by decorating it. It has two parameters, the first is whether it is infinite.
#If that is true, it will constantly run in the background giving outputs.
def asyncify(inf):
    def asyncWrap(func):
        def func_wrapper(*args, **kwargs):
            if inf:
                #Creates an infinite version of the function
                def nfunc():        
                    while True:
                        func(*args, *kwargs)

                #Puts function in new thread to run
                task1 = threading.Thread(target=nfunc, daemon=True)
                task1.start()

            else:
                #Puts function in to new thread to run
                task1 = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
                task1.start()
        return func_wrapper
    return asyncWrap

@asyncify(False)
#This pushes a val to recipients
def push(broadcast, val):
    #Socketio is what allows it to be asyncified.
    #If you want an out val, you need to broadcast with socket.
    #For our purpose we send the result straight to the clients.
    socketio.emit(broadcast, val)

#This is a background task, made with my async, that is constantly asking for notes section for saving purposes it runs every 0.2 secs
@asyncify(True)
def background():
    while True:
        push('getNotes', '')
        time.sleep(0.5)

#This is a background task, made with my async, that updates screen surveilance every 5 seconds.
@asyncify(True)
def background2():
    while True:
        push('screenreq', '')
        time.sleep(5)

#This part sends a role back on connect, it is unreliable for the second connect and will usually send back a duplicate role. But, otherwise its fine.
@socketio.on('connect')
def pong():
    global givingRole
    while givingRole:
        time.sleep(0.1)
    #holds others waiting for role while it figures out what to give current guy asking
    givingRole = True
    for i in roles.query.all():
        i.taken = 0
    db.session.commit()
    global rolesMod
    rolesMod = 0
    push('roleCheck','')
    #Keeps waiting while seeing what roles are taken
    rmod = 0
    while rmod <= rolesMod:
        time.sleep(0.5)
        rmod += 1
    #Sends back role
    push('handshake', json.dumps(roles.query.filter_by(taken=0).first().name))
    #Stops stalling everyone else waiting for a role
    givingRole = False

#The page everything runs off, the template running also holds the functional js which runs the entire client
@flask_app.route("/")
def index():
    #Runs background tasks on first connect
    global start
    if start:
        background()
        background2()
        start = False
    return render_template('index.html')

#Loads library
@flask_app.route("/libraryLoad")
def libload():
    lib = library.query.all()
    return json.dumps(render_template('library.html', db=lib))

#Gets dropdown text
@flask_app.route("/dropdown")
def dropdown():
    val = request.args.get('q')
    entry = library.query.filter_by(name=val).first()
    return json.dumps(render_template('dropdown.html',title=entry.title,templatetext=entry.templatetext.split('\n'),persontext=entry.persontext.split('\n'),name=entry.name))

#adds to global chat
@socketio.on("chatadd")
def addchat(val):
    push('chat', val)

#adds to a privat chat channel like admin to command or helm to admin and etc.
@socketio.on("chatpriv")
def privatechat(val):
    push('chatpriv', val)

#This pushes the screen a person is viewing
@socketio.on("screen")
def giveScreen(val):
    push('screenVal', val)

#This changes alert
@socketio.on("sendAlert")
def alerts(val):
    push('alert', val)

#This is the role verifier. If it gets response it checks of that role as taken.
@socketio.on("roleSend")
def resetRoleList(val):
    global rolesMod
    rolesMod += 1
    rem = roles.query.filter_by(name=val).first()
    if rem:
        rem.taken = 1
    else:
        print(val)
    db.session.commit()

#This saves notes.  If the note section doesn't exist in database it makes an entry for it.
@socketio.on("saveNotes")
def saveNote(val):
    value = json.loads(val)
    print(value)
    if not savedNotes.query.filter_by(name=value[0]).all():
        u = savedNotes(name=value[0],text=value[1])
        db.session.add(u)
    else:
        u = savedNotes.query.filter_by(name=value[0]).first()
        u.text = value[1]
    db.session.commit()

#On a request for notes it sends back notes with syncNote which syncs up database notes on to the client notes
@socketio.on("reqNotes")
def reqNote(val):
    push('syncNote', json.dumps([val,savedNotes.query.filter_by(name=val).first().text]))

if __name__ == "__main__":
    #runs app
    socketio.run(flask_app, host='0.0.0.0', port=5000)