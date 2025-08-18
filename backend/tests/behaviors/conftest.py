from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.dexterity.fti import DexterityFTI
from plone.restapi.testing import RelativeSession
from zope.component.hooks import setSite

import pytest
import transaction


# Importa módulos necessários para configurar fixtures de teste no Plone


@pytest.fixture()
def request_factory(portal):
    """Cria uma fábrica de requisições para interagir com a API REST do Plone."""

    def factory():
        url = portal.absolute_url()
        api_session = RelativeSession(url)
        api_session.headers.update({"Accept": "application/json"})
        return api_session

    return factory


@pytest.fixture()
def anon_request(request_factory):
    """Cria uma requisição anônima para testes."""
    return request_factory()


@pytest.fixture()
def manager_request(request_factory):
    """Cria uma requisição autenticada como administrador para testes."""
    request = request_factory()
    request.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
    yield request
    request.auth = ()


@pytest.fixture
def portal(functional):
    """Retorna o portal configurado para testes funcionais."""
    return functional["portal"]


@pytest.fixture
def portal_integration(integration):
    return integration["portal"]


@pytest.fixture
def portal_factory(functional):
    """Cria um portal com um tipo de conteúdo dummy e behaviors configurados."""

    def func(behavior: str):
        portal = functional["portal"]
        setRoles(portal, TEST_USER_ID, ["Manager"])
        fti = DexterityFTI("DummyType")
        fti.behaviors = (behavior,)
        portal.portal_types._setObject("DummyType", fti)
        setSite(portal)
        transaction.commit()
        return portal

    return func


@pytest.fixture
def dummy_type_schema(manager_request):
    """Obtém o schema do tipo de conteúdo dummy configurado."""

    def func():
        url = "/@types/DummyType"
        response = manager_request.get(url)
        data = response.json()
        return data

    return func


@pytest.fixture
def create_dummy_content(manager_request):
    """Cria conteúdo dummy para testes com os behaviors configurados."""

    def func(payload: dict):
        payload["@type"] = "DummyType"
        response = manager_request.post("/", json=payload)
        return response

    return func
