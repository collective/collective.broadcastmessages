import unittest2 as unittest

from zope.interface import alsoProvides

from plone.app.testing import logout

from Products.CMFCore.utils import getToolByName

from collective.broadcastmessages.testing import \
    COLLECTIVE_BROADCASTMESSAGES_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = COLLECTIVE_BROADCASTMESSAGES_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'collective.broadcastmessages'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_viewlet_shown_to_authenticated(self):
        """
        check that viewlet is included by main template
        when rendered for logged-in user
        """
        from collective.broadcastmessages.messages import (
            registerBroadcastMessages
            )
        registerBroadcastMessages(self.portal, ['message1', 'message2'])
        from collective.broadcastmessages.browser.interfaces import (
            IBroadcastMessagesLayer,
            )
        alsoProvides(self.portal.REQUEST, IBroadcastMessagesLayer)
        self.assertTrue('broadcast-messages' in self.portal())
        self.assertTrue('message1' in self.portal())
        self.assertTrue('message2' in self.portal())

    def test_viewlet_not_shown_to_anonymous(self):
        """
        check that viewlet is not included by main template
        when rendered for anonymous user
        """
        from collective.broadcastmessages.messages import (
            registerBroadcastMessages
            )
        registerBroadcastMessages(self.portal, ['maintenance'])
        logout()
        from collective.broadcastmessages.browser.interfaces import (
            IBroadcastMessagesLayer,
            )
        alsoProvides(self.portal.REQUEST, IBroadcastMessagesLayer)
        self.assertFalse('broadcast-messages' in self.portal())

    def test_viewlet_not_shown_when_no_messages(self):
        from collective.broadcastmessages.messages import (
            registerBroadcastMessages
            )
        registerBroadcastMessages(self.portal, [])
        from collective.broadcastmessages.browser.interfaces import (
            IBroadcastMessagesLayer,
            )
        alsoProvides(self.portal.REQUEST, IBroadcastMessagesLayer)
        self.assertFalse('broadcast-messages' in self.portal())

    def test_viewlet_not_shown_when_no_utility(self):
        from collective.broadcastmessages.browser.interfaces import (
            IBroadcastMessagesLayer,
            )
        alsoProvides(self.portal.REQUEST, IBroadcastMessagesLayer)
        self.assertFalse('broadcast-messages' in self.portal())

    def test_viewlet_when_utility_registered_at_startup(self):
        from collective.broadcastmessages.browser.interfaces import (
            IBroadcastMessagesLayer,
            )
        from collective.broadcastmessages.messages import (
            registerBroadcastMessages
            )
        alsoProvides(self.portal.REQUEST, IBroadcastMessagesLayer)
        registerBroadcastMessages(self.portal, ['maintenance', 'tuesday'])
        self.assertTrue('broadcast-messages' in self.portal())
        self.assertTrue('maintenance' in self.portal())
