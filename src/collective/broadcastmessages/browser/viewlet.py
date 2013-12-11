from plone.app.layout.viewlets.common import ViewletBase


class BroadcastMessageViewlet(ViewletBase):

    def update(self):
        self.messages = ["broadcast", ]
