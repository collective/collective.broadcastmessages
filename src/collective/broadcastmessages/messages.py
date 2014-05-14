import transaction
import os.path

from App.config import getConfiguration
from zope.component import getSiteManager

from collective.broadcastmessages.interfaces import IBroadcastMessages


DIRECTORYNAME = 'broadcastmessages'


def initializeFromFileSystem(event):
    cfg = getConfiguration()
    messages_filename = os.path.join(cfg.clienthome, MESSAGES_FILENAME)
    if not os.path.exists(messages_filename):
        return
    file = open(messages_filename)
    try:
        all_messages = parseMessageFile(file)
    finally:
        file.close()
    db = event.database
    conn = db.open()
    try:
        root = conn.root()
        app = root['Application']
        try:
            for portal in app.objectValues(spec="Plone Site"):
                registerBroadcastMessages(portal, messages)
            transaction.commit()
        except:
            transaction.abort()
            raise
    finally:
        conn.close()


def parseMessageFile(file):
    import ConfigParser, os

    config = ConfigParser.SafeConfigParser()
    config.readfp(file)
    result = dict()
    for section in config.sections():
        result[section] = config.options(section)
    return result


def registerBroadcastMessages(portal, messages):
    sm = getSiteManager(portal)
    sm.registerUtility(
        component=messages,
        provided=IBroadcastMessages,
        )
