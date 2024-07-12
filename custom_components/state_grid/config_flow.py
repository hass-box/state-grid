import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.selector import selector


from .utils.logger import LOGGER
from .const import DOMAIN

from .data_client import StateGridDataClient

class StateGridConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        if self.hass.data.get(DOMAIN):
            return self.async_abort(reason="single_instance_allowed")
        
        self.data_client = StateGridDataClient(hass=self.hass)

        options = {
            "scan_login": "网上国网 App 扫码登录",
            "code_login": "手机短信验证码登录",
        }

        return self.async_show_menu(
            step_id="user",
            menu_options=options
        )

    async def async_step_scan_login(self, user_input=None):
        result = await self.data_client.get_qr_code()
        if result['errcode'] != 0:
            return self.async_abort(
                reason="get_qr_code_error", 
                description_placeholders={'errmsg': result["errmsg"]}
            )
        
        return self.async_show_form(
            step_id="check_qr_code",
            description_placeholders={
                "qr_image": '<img style="width: 200px;" src="data:image/png;base64,' + result["data"] + '"/>'
            }
        )

    async def async_step_check_qr_code(self, user_input=None):
        result = await self.data_client.check_qr_code()

        if result['errcode'] != 0:
            return self.async_abort(
                reason="check_qr_code_error", 
                description_placeholders={'errmsg': result["errmsg"]}
            )

        return self.async_create_entry(
            title="国家电网",
            data={}
        )
        
    async def async_step_code_login(self, user_input=None):
        errors = {}
        if user_input is None:
            user_input = {}
        else:
            phone = user_input['phone']
            result = await self.data_client.send_phone_code(phone)
            if result['errcode'] == 0:
                return await self.async_step_verfiy_code()
            else:
                errors["phone"] = result["errmsg"]
        
        data_schema = {
            vol.Required("phone") : selector({
                "text": {
                    "type": "number"
                }
            })
        }
        
        return self.async_show_form(
            step_id="code_login",
            data_schema=vol.Schema(data_schema),
            errors=errors
        )
    
    async def async_step_verfiy_code(self, user_input=None):
        errors = {}
        if user_input is None:
            user_input = {}
        else:
            code = user_input['code']
            result = await self.data_client.verfiy_phone_code(code)
            if result['errcode'] == 0:
                return self.async_create_entry(
                    title="国家电网",
                    data={}
                )
            
            errors["code"] = result["errmsg"]    

        data_schema = {
            vol.Required("code") : selector({
                "text": {
                    "type": "number"
                }
            })
        }
        
        return self.async_show_form(
            step_id="verfiy_code",
            data_schema=vol.Schema(data_schema),
            errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(entry: config_entries.ConfigEntry):
        return OptionsFlowHandler(entry)

class OptionsFlowHandler(config_entries.OptionsFlow):

    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry
        
    async def async_step_init(self, user_input=None):
        self.data_client: StateGridDataClient = self.hass.data[DOMAIN]
        if self.data_client.need_login is True:
            return await self.async_step_user()
        else:
            return await self.async_step_debug()
        
    async def async_step_debug(self, user_input=None):
        if user_input is None:
            user_input = {}
        else:
            self.data_client.refresh_interval = int(user_input['refresh_interval'])
            self.data_client.is_debug = user_input['is_debug']
            await self.data_client.save_data()
            return self.async_create_entry(
                title="国家电网",
                data={}
            )

        data_schema = {
            vol.Required("refresh_interval", default=str(self.data_client.refresh_interval)) : selector({
                "select": {
                    "options": [
                        {"label":"每1小时", "value": "1"},
                        {"label":"每2小时", "value": "2"},
                        {"label":"每3小时", "value": "3"},
                        {"label":"每4小时", "value": "4"},
                        {"label":"每5小时", "value": "5"},
                        {"label":"每6小时", "value": "6"},
                        {"label":"每7小时", "value": "7"},
                        {"label":"每8小时", "value": "8"},
                        {"label":"每9小时", "value": "9"},
                        {"label":"每10小时", "value": "10"},
                        {"label":"每11小时", "value": "11"},
                        {"label":"每12小时", "value": "12"}
                    ]
                }
            }),
            vol.Required("is_debug", default=self.data_client.is_debug): selector({
                "boolean": {}
            })
        }
        
        return self.async_show_form(
            step_id="debug",
            data_schema=vol.Schema(data_schema)
        )

    async def async_step_user(self, user_input=None):
        options = {
            "scan_login": "网上国网 App 扫码登录",
            "code_login": "手机短信验证码登录",
        }

        return self.async_show_menu(
            step_id="user",
            menu_options=options
        )

    async def async_step_scan_login(self, user_input=None):
        result = await self.data_client.get_qr_code()
        if result['errcode'] != 0:
            return self.async_abort(
                reason="get_qr_code_error", 
                description_placeholders={'errmsg': result["errmsg"]}
            )
        
        return self.async_show_form(
            step_id="check_qr_code",
            description_placeholders={
                "qr_image": '<img style="width: 200px;" src="data:image/png;base64,' + result["data"] + '"/>'
            }
        )

    async def async_step_check_qr_code(self, user_input=None):
        result = await self.data_client.check_qr_code()
        if result['errcode'] != 0:
            return self.async_abort(
                reason="check_qr_code_error", 
                description_placeholders={'errmsg': result["errmsg"]}
            )
        await self.data_client.refresh_data(force_refresh=True)
        return self.async_create_entry(
            title="国家电网",
            data={}
        )
        
    async def async_step_code_login(self, user_input=None):
        errors = {}
        if user_input is None:
            user_input = {}
        else:
            phone = user_input['phone']
            result = await self.data_client.send_phone_code(phone)
            if result['errcode'] == 0:
                return await self.async_step_verfiy_code()
            else:
                errors["phone"] = result["errmsg"]
        
        data_schema = {
            vol.Required("phone") : selector({
                "text": {
                    "type": "number"
                }
            })
        }
        
        return self.async_show_form(
            step_id="code_login",
            data_schema=vol.Schema(data_schema),
            errors=errors
        )
    
    async def async_step_verfiy_code(self, user_input=None):
        errors = {}
        if user_input is None:
            user_input = {}
        else:
            code = user_input['code']
            result = await self.data_client.verfiy_phone_code(code)
            if result['errcode'] == 0:
                await self.data_client.refresh_data(force_refresh=True)
                return self.async_create_entry(
                    title="国家电网",
                    data={}
                )
            
            errors["code"] = result["errmsg"]    

        data_schema = {
            vol.Required("code") : selector({
                "text": {
                    "type": "number"
                }
            })
        }
        
        return self.async_show_form(
            step_id="verfiy_code",
            data_schema=vol.Schema(data_schema),
            errors=errors
        )
