import urllib.parse
from karrio.core.utils import DP, request as http, Serializable, Deserializable
from karrio.api.proxy import Proxy as BaseProxy
from karrio.mappers.yanwen.settings import Settings


class Proxy(BaseProxy):
    settings: Settings

    """ Proxy Methods """

    def get_tracking(self, request: Serializable) -> Deserializable:
        query = urllib.parse.urlencode(request.serialize())
        response = http(
            url=f"http://trackapi.yanwentech.com/api/tracking?{query}",
            trace=self.trace_as("json"),
            method="GET",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": self.settings.customer_number,
            },
        )

        return Deserializable(response, DP.to_dict)
