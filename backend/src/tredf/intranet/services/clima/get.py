from plone import api
from plone.restapi.services import Service
from tredf.intranet import logger
from tredf.intranet.services.clima import openmeteo


class ClimaGet(Service):
    """Serviço para obter dados climáticos do TRE-DF."""

    @property
    def coordinates(self) -> tuple:
        """Retorna latitude e longitude do TRE-DF."""
        return (-15.786673953148663, -47.912418829076856)

    @property
    def timezone(self) -> str:
        return api.portal.get_registry_record("plone.portal_timezone")

    def reply(self):
        portal = api.portal.get()
        portal_url = portal.absolute_url()
        latitude, longitude = self.coordinates
        timezone = self.timezone
        logger.info("Acessa dados do clima")
        dados = openmeteo.dados_clima(latitude, longitude, timezone)
        dados["@id"] = f"{portal_url}/@clima"
        logger.info("Retorna dados do clima")
        return dados
