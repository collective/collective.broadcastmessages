from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

import collective.broadcastmessages


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
COLLECTIVE_BROADCASTMESSAGES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_BROADCASTMESSAGES_FIXTURE, z2.ZSERVER_FIXTURE),
    name="COLLECTIVE_BROADCASTMESSAGES_FUNCTIONAL_TESTING"
)
