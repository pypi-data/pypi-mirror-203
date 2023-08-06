from ..parse_config_file import parse_config
from . import battery_ngi, battery_itech_control, battery_gmc_control, battery_korad_control, battery_chroma_control, \
    read_curr_vol_module_control, bin_set_module_control


def set_battery_ngi_by_serial(config: parse_config.ConfigHandler):
    vbat_config = config.get_config_by_inst('power_supply_NGI')
    baud = config.get_baud_rate('power_supply_NGI')
    com = config.get_com('power_supply_NGI')

    return battery_ngi.BatControlNGIBySerial(baud, com, vbat_config)


def set_battery_itech_by_visa(config: parse_config.ConfigHandler):
    vbat_config = config.get_config_by_inst('power_supply_IT6512')
    resource = vbat_config['visa_resource']

    return battery_itech_control.BatIT6512ControlByVisa(resource, vbat_config)


def set_battery_gmc_by_serial(config: parse_config.ConfigHandler):
    vbat_config = config.get_config_by_inst('power_supply_gmc')
    baud = config.get_baud_rate('power_supply_gmc')
    com = config.get_com('power_supply_gmc')

    return battery_gmc_control.BatGMCControlBySerial(baud, com, vbat_config)


def set_battery_korad_by_serial(config: parse_config.ConfigHandler):
    vbat_config = config.get_config_by_inst('power_supply_korad')
    baud = config.get_baud_rate('power_supply_korad')
    com = config.get_com('power_supply_korad')

    return battery_korad_control.BatKoradControlBySerial(baud, com, vbat_config)


def set_battery_chroma_by_visa(config: parse_config.ConfigHandler):
    vbat_config = config.get_config_by_inst('power_supply_chroma')
    resource = vbat_config['visa_resource']

    return battery_chroma_control.BatChromaControlByVisa(resource, vbat_config)


def set_battery_chroma_by_serial(config: parse_config.ConfigHandler):
    vbat_config = config.get_config_by_inst('power_supply_chroma')
    baud = config.get_baud_rate('power_supply_chroma')
    com = config.get_com('power_supply_chroma')

    return battery_chroma_control.BatChromaControlBySerial(baud, com, vbat_config)


def set_curr_vol_module(config: parse_config.ConfigHandler):
    baud = config.get_baud_rate('read_current_voltage_module')
    com = config.get_com('read_current_voltage_module')

    return read_curr_vol_module_control.ReadCurrVolModuleControl(baud=baud, com=com)


def set_bin_module(config: parse_config.ConfigHandler):
    baud = config.get_baud_rate('bin_set_module')
    com = config.get_com('bin_set_module')

    return bin_set_module_control.BinSetModuleControl(baud=baud, com=com)
