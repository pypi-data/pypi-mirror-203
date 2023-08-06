"""Karrio Yanwen settings."""

import attr
from karrio.providers.yanwen.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """Yanwen connection settings."""

    # Carrier specific properties
    customer_number: str
    license_key: str

    # Base properties
    id: str = None
    test_mode: bool = False
    carrier_id: str = "yanwen"
    account_country_code: str = None
    metadata: dict = {}
    config: dict = {}
