# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import onto.utility


class OntoUtilityLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=onto.utility)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'onto.utility:default')


ONTO_UTILITY_FIXTURE = OntoUtilityLayer()


ONTO_UTILITY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ONTO_UTILITY_FIXTURE,),
    name='OntoUtilityLayer:IntegrationTesting',
)


ONTO_UTILITY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ONTO_UTILITY_FIXTURE,),
    name='OntoUtilityLayer:FunctionalTesting',
)


ONTO_UTILITY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ONTO_UTILITY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='OntoUtilityLayer:AcceptanceTesting',
)
