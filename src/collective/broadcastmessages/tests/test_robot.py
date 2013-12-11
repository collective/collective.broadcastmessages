from collective.broadcastmessages.testing import (
    COLLECTIVE_BROADCASTMESSAGES_ROBOT_TESTING
)
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("broadcastmessages.robot"),
                layer=COLLECTIVE_BROADCASTMESSAGES_ROBOT_TESTING)
    ])
    return suite
