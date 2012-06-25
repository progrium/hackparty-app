# Loosely generic API for working with Google Apps domains.
# Pulled from my work on hackerdojo/hd-domain on GitHub.
# Eventually could be a generic library

import gdata.apps.client
import gdata.apps.emailsettings.client
import gdata.apps.groups.client

def _user(self, user):
    return {
        'last_name': user.name.family_name,
        'first_name': user.name.given_name,
        'username': user.login.user_name,
        'suspended': user.login.suspended == 'true',
        'admin': user.login.admin == 'true'}

def flatten(l):
    """ This takes a hierarchy of lists/tuples and flattens them into one """
    out = []
    for item in l:
        if isinstance(item, (list, tuple)):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

class Domain(object):
    def __init__(self, name, username, password):
        self.name = name
        self.source = 'hackparty'
        self.username = username
        self.password = password
        self.users = DomainUsers(self)
        self.groups = DomainGroups(self)
        self.email = DomainEmail(self)

class DomainEmail(object):
    def __init__(self, domain):
        self.domain = domain
        self.client = gdata.apps.emailsettings.client.EmailSettingsClient(domain=domain.name)
        self.client.ClientLogin(domain.username, domain.password, domain.source)

    def get_forwarding(self, username):
        return self.client.RetrieveForwarding(username)

class DomainGroups(object):
    def __init__(self, domain):
        self.domain = domain
        self.client = gdata.apps.groups.client.GroupsProvisioningClient(domain=domain.name)
        #self.groups_client.SetClientLoginToken(token)
        self.client.ClientLogin(domain.username, domain.password, domain.source)

    def all(self):
        return [g['groupId'].split('@')[0] for g in self.client.RetrieveAllGroups()]

    def get(self, group_id):
        return [m['memberId'].split('@')[0] for m in
                self.client.RetrieveAllMembers(group_id)
                if m['memberId'].split('@')[1] == self.domain.name]

class DomainUsers(object):
    def __init__(self, domain):
        self.domain = domain
        self.client = gdata.apps.client.AppsClient(domain=domain.name)
        self.client.ClientLogin(domain.username, domain.password, domain.source)
        #self.apps_client.SetClientLoginToken(token)

    def all(self, include_suspended=False):
        return [e.title.text for e in
            flatten([u.entry for u in
                self.client.GetGeneratorForAllUsers()])
            if include_suspended or e.login.suspended == 'false']

    def get(self, username):
        return _user(self.client.RetrieveUser(username))

    def create(self, username, password, first_name, last_name):
        return _user(self.client.CreateUser(
            user_name   = username,
            password    = password,
            given_name  = first_name,
            family_name = last_name))

    def suspend(self, username):
        return _user(self.apps_client.SuspendUser(user_name=username))

    def restore(self, username):
        return _user(self.apps_client.RestoreUser(user_name=username))

