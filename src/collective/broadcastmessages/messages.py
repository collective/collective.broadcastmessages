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
            for portal in app.objectValues(spec="Plone Site"):
                registerBroadcastMessages(portal)
            transaction.commit()
        except:
            transaction.abort()
            raise
    finally:
        conn.close()


def registerBroadcastMessages(portal, messages):
    sm = getSiteManager(portal)
    sm.registerUtility(
        component=messages,
        provided=IBroadcastMessages,
        )
