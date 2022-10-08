import fuzzy.membership as ms

def fuzzification(aqi: float, flowrate: float):
    '''return fuzzification of input'''
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