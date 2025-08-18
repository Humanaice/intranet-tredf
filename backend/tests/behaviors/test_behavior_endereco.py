from tredf.intranet import PACKAGE_NAME

import pytest


@pytest.fixture
def payload() -> dict:
    """Retorna os dados de exemplo para o behavior de endereço."""
    return {
        "endereco": "R. João Parolin, 224",
        "complemento": "",
        "cidade": "Brasília",
        "estado": "DF",
        "cep": "80220-902",
    }


class TestBehaviorEndereco:
    """Testa o behavior de endereço."""

    name: str = f"{PACKAGE_NAME}.behavior.endereco"  # Nome do behavior

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
