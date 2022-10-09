import fuzzy.membership as ms

def fuzzification(aqi: float, flowrate: float):
    '''return fuzzification of inputs'''
    aqi_dict = {}
    flowrate_dict = {}
    aqi_dict['GOOD'] = ms.aqi_good(aqi)
    aqi_dict['MODERATE'] = ms.aqi_moderate(aqi)
    aqi_dict['UNHEALTHY_SENSITIVE'] = ms.aqi_unhealthy_sensitive(aqi)
    aqi_dict['UNHEALTHY'] = ms.aqi_unhealthy(aqi)
    aqi_dict['VERY_UNHEALTHY'] = ms.aqi_very_unhealthy(aqi)
    aqi_dict['HAZARDOUS'] = ms.aqi_hazardous(aqi)
    flowrate_dict['LOW'] = ms.filter_low(flowrate)
    flowrate_dict['MEDIUM'] = ms.filter_medium(flowrate)
    flowrate_dict['HIGH'] = ms.filter_high(flowrate)
    return aqi_dict, flowrate_dict

def gen_output_membership():
    '''generate fanspeed membership function from universe for union output from rules'''
    mem_fan_low = {}
    mem_fan_medium = {}
    mem_fan_high = {}
    for x in ms.x_fanspeed:
        mem_fan_low[x] = ms.fan_low(x)
        mem_fan_medium[x] = ms.fan_medium(x)
        mem_fan_high[x] = ms.fan_high(x)
    return mem_fan_low, mem_fan_medium, mem_fan_high