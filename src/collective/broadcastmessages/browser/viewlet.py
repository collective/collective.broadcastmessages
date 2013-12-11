from plone.app.layout.viewlets.common import ViewletBase


class BroadcastMessageViewlet(ViewletBase):

    def update(self):
        self.message_html = "broadcast"
