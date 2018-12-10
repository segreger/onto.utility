# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from onto.utility.testing import ONTO_UTILITY_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that onto.utility is properly installed."""

    layer = ONTO_UTILITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if onto.utility is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'onto.utility'))

    def test_browserlayer(self):
        """Test that IOntoUtilityLayer is registered."""
        from onto.utility.interfaces import (
            IOntoUtilityLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IOntoUtilityLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ONTO_UTILITY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['onto.utility'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if onto.utility is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'onto.utility'))

    def test_browserlayer_removed(self):
        """Test that IOntoUtilityLayer is removed."""
        from onto.utility.interfaces import \
            IOntoUtilityLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IOntoUtilityLayer,
            utils.registered_layers())
