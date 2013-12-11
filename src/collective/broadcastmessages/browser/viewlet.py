from zope.component import queryUtility

from plone.app.layout.viewlets.common import ViewletBase

from collective.broadcastmessages.interfaces import IBroadcastMessages


class BroadcastMessageViewlet(ViewletBase):

    def update(self):
        self.messages = queryUtility(
            IBroadcastMessages,
            context=self.context,
            default=[],
            )
