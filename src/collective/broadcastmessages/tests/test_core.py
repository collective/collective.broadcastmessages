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
        view = self.portal.restrictedTraverse('index_html')
        from collective.broadcastmessages.browser.interfaces import (
            IBroadcastMessagesLayer,
            )
        alsoProvides(view.REQUEST, IBroadcastMessagesLayer)
        self.assertTrue('broadcast-messages' in view())

    def test_viewlet_not_shown_to_anonymous(self):
        logout()
        view = self.portal.restrictedTraverse('index_html')
        from collective.broadcastmessages.browser.interfaces import (
            IBroadcastMessagesLayer,
            )
        alsoProvides(view.REQUEST, IBroadcastMessagesLayer)
        self.assertFalse('broadcast-messages' in view())
