from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import collective.broadcastmessages
from collective.broadcastmessages.messages import registerBroadcastMessages


COLLECTIVE_BROADCASTMESSAGES_FIXTURE = PloneWithPackageLayer(
    zcml_package=collective.broadcastmessages,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.broadcastmessages:default',
    name='COLLECTIVE_BROADCASTMESSAGES_FIXTURE'
)
COLLECTIVE_BROADCASTMESSAGES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BROADCASTMESSAGES_FIXTURE,),
    name="COLLECTIVE_BROADCASTMESSAGES_INTEGRATION_TESTING"
)
COLLECTIVE_BROADCASTMESSAGES_FUNCTIONAL_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BROADCASTMESSAGES_FIXTURE,),
    name="COLLECTIVE_BROADCASTMESSAGES_FUNCTIONAL_TESTING"
)
COLLECTIVE_BROADCASTMESSAGES_TESTING_PROFILE = PloneWithPackageLayer(
    zcml_package=collective.broadcastmessages,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.broadcastmessages:testing',
    name='COLLECTIVE_BROADCASTMESSAGES_FIXTURE'
)
COLLECTIVE_BROADCASTMESSAGES_ROBOT_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_BROADCASTMESSAGES_TESTING_PROFILE,
        AUTOLOGIN_LIBRARY_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="COLLECTIVE_BROADCASTMESSAGES_ROBOT_TESTING"
)


def testSetup(portal_setup):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if portal_setup.readDataFile(
            'collective_broadcastmessages_testing.txt') is None:
        return
    portal = portal_setup.getSite()
    registerBroadcastMessages(portal, ['maintenance', 'tuesday'])
