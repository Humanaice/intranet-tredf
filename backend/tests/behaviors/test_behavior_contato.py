from tredf.intranet import PACKAGE_NAME

import pytest


@pytest.fixture
def payload() -> dict:
    """Retorna os dados de exemplo para o behavior de contato."""
    return {
        "email": "foo@tre-df.jus.br",
        "telefone": "61999528312",
    }


class TestBehaviorContato:
    """Testa o behavior de contato."""

    name: str = f"{PACKAGE_NAME}.behavior.contato"  # Nome do behavior

    @pytest.fixture(autouse=True)
    def _setup(self, portal_factory, dummy_type_schema):
        """Configura o portal e o schema para os testes."""
        self.portal = portal_factory(behavior=self.name)
        self.schema = dummy_type_schema()

    def test_behavior_schema(self, payload):
        """Verifica se os campos do payload estão no schema do behavior."""
        for key in payload:
            assert key in self.schema["properties"]

    def test_behavior_data(self, payload, create_dummy_content):
        """Testa a criação de conteúdo com os dados do behavior."""
        response = create_dummy_content(payload)
        assert response.status_code == 201
