from __future__ import annotations

from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .data_client import StateGridDataClient

from .const import DOMAIN
from .utils.logger import LOGGER

class StateGridCoordinator(DataUpdateCoordinator):

    def __init__(self, hass: HomeAssistant) -> None:
        super().__init__(
            hass,
            LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=300)
        )
        self.first_setup = True
        self.data_client: StateGridDataClient = hass.data[DOMAIN]

    async def _async_update_data(self):
        await self.data_client.refresh_data(setup=self.first_setup)
        self.first_setup = False
        return self.data_client.get_door_account()