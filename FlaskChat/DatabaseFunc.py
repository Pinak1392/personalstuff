#Adds stuff to a table
def addTo(session, c, **VarVal):
    new = c()
    for k, v in VarVal.items():
        exec(f"new.{k} = '{v}'")
    
    session.add(new)
    session.commit()

#Removes from a table
def removeFrom(session, row):
    session.delete(row)
    session.commit()

#Removes from a table
def updateTab(session, obj, attr, nVal):
    a = obj
    exec(f"a.{attr} = '{nVal}'")
    session.commit()
