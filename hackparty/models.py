from google.appengine.ext import db

class Profile(db.Model):
    user = db.UserProperty()
    email = db.EmailProperty()
    created = db.DateTimeProperty(auto_now_add=True)

class EventSeries(db.Model):
    """ An EventSeries is a collection of events. For example: /Twilio Hack Party [0-9]+"""
    organizer = db.UserProperty()
    name = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    # provides QR code to use on event pages

class Event(db.Model):
    """A single event. For example: /Twilio Hack Party 0/"""
    organizer = db.UserProperty()
    series = db.ReferenceProperty(EventSeries)
    created = db.DateTimeProperty(auto_now_add=True)

class Authorization(db.Model):
    """Record of an Authorization to run an EventSeries."""
    from_ = db.UserProperty()
    to = db.UserProperty()
    event = db.ReferenceProperty(Event)
    created = db.DateTimeProperty(auto_now_add=True)

class Endorsement(db.Model):
    from_ = db.UserProperty()
    to = db.UserProperty()
    event = db.ReferenceProperty(Event)
    created = db.DateTimeProperty(auto_now_add=True)
