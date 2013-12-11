import transaction

from zope.component import getSiteManager

from collective.broadcastmessages.interfaces import IBroadcastMessages


def initializeFromFileSystem(event):
    db = event.database
    conn = db.open()
    try:
        root = conn.root()
        app = root['Application']
        try:
            registerUtilities(app)
            transaction.commit()
        except:
            transaction.abort()
            raise
    finally:
        conn.close()


def registerUtilities(app):
    for portal in app.objectValues(spec="Plone Site"):
        sm = getSiteManager(portal)
        sm.registerUtility(
            component=['message1', 'message2'],
            provided=IBroadcastMessages,
            )
