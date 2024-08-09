from homeassistant.components.sensor import (
    DOMAIN as SENSOR_DOMAIN,
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfEnergy
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

import datetime

from .const import DOMAIN, VERSION
from .data_client import StateGridDataClient
from .coordinator import StateGridCoordinator

UNIT_YUAN = "元"

ENTITY_ID_SENSOR_FORMAT = SENSOR_DOMAIN + ".state_grid_"

SENSOR_TYPES = [
    {
        "key":"balance",
        "name": "账户余额",
        "native_unit_of_measurement": UNIT_YUAN,
        "device_class": SensorDeviceClass.MONETARY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "year_ele_num",
        "name": "年度累计用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "year_p_ele_num",
        "name": "年度累计峰用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "year_v_ele_num",
        "name": "年度累计谷用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "year_n_ele_num",
        "name": "年度累计平用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "year_t_ele_num",
        "name": "年度累计尖用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "year_ele_cost",
        "name": "年度累计电费",
        "native_unit_of_measurement": UNIT_YUAN,
        "device_class": SensorDeviceClass.MONETARY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "last_month_ele_num",
        "name": "上个月用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "last_month_ele_cost",
        "name": "上个月电费",
        "native_unit_of_measurement": UNIT_YUAN,
        "device_class": SensorDeviceClass.MONETARY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "last_month_meter_num",
        "name": "上个月抄表"
    },
    {
        "key": "month_ele_num",
        "name": "当月累计用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "month_p_ele_num",
        "name": "当月累计峰用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "month_v_ele_num",
        "name": "当月累计谷用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "month_n_ele_num",
        "name": "当月累计平用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "month_t_ele_num",
        "name": "当月累计尖用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "daily_ele_num",
        "name": "日总用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "daily_p_ele_num",
        "name": "日峰用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "daily_v_ele_num",
        "name": "日谷用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "daily_n_ele_num",
        "name": "日平用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "daily_t_ele_num",
        "name": "日尖用电",
        "native_unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL
    },
    {
        "key": "daily_lasted_date",
        "name": "最新日用电日期"
    },
    {
        "key": "refresh_time",
        "name": "最近刷新时间"
    }
]

SENSOR_TYPES_FOR_LADDER = [
    {
        "key": "ladder_level",
        "name": "当前阶梯"
    },
]

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    data_client: StateGridDataClient = hass.data[DOMAIN]
    coordinator = StateGridCoordinator(hass)
    data_client.coordinator = coordinator
    await coordinator.async_config_entry_first_refresh()
    door_account_list = data_client.get_door_account_list()
    for door_account in door_account_list:
        async_add_entities(
            [StateGridSensor(door_account, sensor_type, entry.entry_id, coordinator) for sensor_type in SENSOR_TYPES]
        )
        # if door_account["ladder_flag"] == 1:
        #     async_add_entities(
        #         StateGridSensor(door_account, sensor_type, entry.entry_id)
        #         for sensor_type in SENSOR_TYPES_FOR_LADDER
        #     )

class StateGridSensor(CoordinatorEntity[StateGridCoordinator], SensorEntity):

    _attr_has_entity_name = True

    def __init__(
        self, door_account, sensor_type, entry_id: str, coordinator: StateGridCoordinator,
    ) -> None:
        super().__init__(coordinator)
        self.door_account = door_account
        self.sensor_type = sensor_type
        self.entity_id = SENSOR_DOMAIN + ".state_grid" + "_" + door_account["consNo_dst"] + "_" + sensor_type["key"]
        self._attr_name = sensor_type["name"]
        self._attr_unique_id = entry_id + "-" + door_account["consNo_dst"] + "-" + sensor_type["key"]


        if "device_class" in sensor_type:
            self._attr_device_class = sensor_type["device_class"]

        if "state_class" in sensor_type:
            self._attr_state_class = sensor_type["state_class"]

        if "native_unit_of_measurement" in sensor_type:
            self._attr_native_unit_of_measurement = sensor_type["native_unit_of_measurement"]

        self._attr_device_info = {
            "name": door_account["elecAddr_dst"],
            "identifiers": {(DOMAIN, door_account["consNo_dst"])},
            "sw_version": VERSION,
            "manufacturer": "HassBox",
            "model": "户号：" + door_account["consName_dst"] + " - " + door_account["consNo_dst"]
        }

    @property
    def native_value(self):
        data = self.coordinator.data[self.door_account["consNo_dst"]]
        return data[self.sensor_type["key"]]
    
