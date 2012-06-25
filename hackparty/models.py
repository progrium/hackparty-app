from google.appengine.ext import db

class Profile(db.Model):
    user = db.UserProperty()
    email = db.EmailProperty()
    created = db.DateTimeProperty(auto_now_add=True)

class EventSeries(db.Model):
    organizer = db.UserProperty()
    name = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    # provides QR code to use on event pages

class Event(db.Model):
    organizer = db.UserProperty()
    series = db.ReferenceProperty(EventSeries)
    created = db.DateTimeProperty(auto_now_add=True)

class Authorization(db.Model):
    from_ = db.UserProperty()
    to = db.UserProperty()
    event = db.ReferenceProperty(Event)
    created = db.DateTimeProperty(auto_now_add=True)

class Endorsement(db.Model):
    from_ = db.UserProperty()
    to = db.UserProperty()
    event = db.ReferenceProperty(Event)
    created = db.DateTimeProperty(auto_now_add=True)
