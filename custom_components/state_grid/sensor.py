from homeassistant.components.sensor import (
    DOMAIN as SENSOR_DOMAIN,
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfEnergy
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

import datetime

from .const import DOMAIN, VERSION
from .data_client import StateGridDataClient
from .coordinator import StateGridCoordinator

CURRENCY_YUAN = "元"

ENTITY_ID_SENSOR_FORMAT = SENSOR_DOMAIN + ".state_grid_"

SENSOR_TYPES = (
    SensorEntityDescription(
        key="balance",
        translation_key="balance",
        native_unit_of_measurement=CURRENCY_YUAN,
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="year_ele_num",
        translation_key="year_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="year_ele_cost",
        translation_key="year_ele_cost",
        native_unit_of_measurement=CURRENCY_YUAN,
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="last_month_ele_num",
        translation_key="last_month_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="last_month_ele_cost",
        translation_key="last_month_ele_cost",
        native_unit_of_measurement=CURRENCY_YUAN,
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="month_ele_num",
        translation_key="month_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="month_p_ele_num",
        translation_key="month_p_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="month_v_ele_num",
        translation_key="month_v_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="month_n_ele_num",
        translation_key="month_n_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="month_t_ele_num",
        translation_key="month_t_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="daily_ele_num",
        translation_key="daily_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="daily_p_ele_num",
        translation_key="daily_p_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="daily_v_ele_num",
        translation_key="daily_v_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="daily_n_ele_num",
        translation_key="daily_n_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="daily_t_ele_num",
        translation_key="daily_t_ele_num",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SensorEntityDescription(
        key="daily_lasted_date",
        translation_key="daily_lasted_date"
    ),
    SensorEntityDescription(
        key="refresh_time",
        translation_key="refresh_time"
    )
)

SENSOR_TYPES_FOR_LADDER = (
    SensorEntityDescription(
        key="ladder_level",
        translation_key="ladder_level"
    ),
)

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator = StateGridCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()
    data_client: StateGridDataClient = hass.data[DOMAIN]
    door_account_list = await data_client.get_door_account_list()
    for door_account in door_account_list:
        async_add_entities(
            [StateGridSensor(door_account, description, entry.entry_id, coordinator) for description in SENSOR_TYPES]
        )
        # if door_account["ladder_flag"] == 1:
        #     async_add_entities(
        #         StateGridSensor(door_account, description, entry.entry_id)
        #         for description in SENSOR_TYPES_FOR_LADDER
        #     )

class StateGridSensor(CoordinatorEntity[StateGridCoordinator], SensorEntity):

    _attr_has_entity_name = True
    entity_description: SensorEntityDescription

    def __init__(
        self, door_account, entity_description: SensorEntityDescription, entry_id: str, coordinator: StateGridCoordinator,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = entity_description
        self.door_account = door_account
        self.entity_id = SENSOR_DOMAIN + ".state_grid" + "_" + door_account["consNo_dst"] + "_" + entity_description.key
        self._attr_translation_key = entity_description.key
        self._attr_unique_id = entry_id + "-" + door_account["consNo_dst"] + "-" + entity_description.key
        self._attr_device_info = {
            "name": door_account["elecAddr_dst"],
            "identifiers": {(DOMAIN, door_account["consNo_dst"])},
            "sw_version": VERSION,
            "manufacturer": "HassBox",
            "model": "户号：" + door_account["consName_dst"] + " - " + door_account["consNo_dst"],
            "entry_type": DeviceEntryType.SERVICE,
        }

    @property
    def native_value(self):
        data = self.coordinator.data[self.door_account["consNo_dst"]]
        return data[self.entity_description.key]
        