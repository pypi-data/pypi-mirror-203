from karrio.core.utils import DP, request as http, Serializable, Deserializable
from karrio.api.proxy import Proxy as BaseProxy
from karrio.mappers.sf_express.settings import Settings


class Proxy(BaseProxy):
    settings: Settings

    """ Proxy Methods """

    def get_tracking(self, request: Serializable) -> Deserializable:
        data = self.settings.parse(request.serialize(), "EXP_RECE_SEARCH_ROUTES")
        response = http(
            url=self.settings.server_url,
            data=data,
            trace=self.trace_as("json"),
            method="POST",
        )

        return Deserializable(response, DP.to_dict)
