dict_rules_variable = {'1': ['GOOD', 'LOW', 'LOW'],
                       '2': ['GOOD', 'MEDIUM', 'LOW'],
                       '3': ['GOOD', 'HIGH', 'LOW'],
                       '4': ['MODERATE', 'LOW', 'MEDIUM'],
                       '5': ['MODERATE', 'MEDIUM', 'LOW'],
                       '6': ['MODERATE', 'HIGH', 'LOW'],
                       '7': ['UNHEALTHY_SENSITIVE', 'LOW', 'MEDIUM'],
                       '8': ['UNHEALTHY_SENSITIVE', 'MEDIUM', 'MEDIUM'],
                       '9': ['UNHEALTHY_SENSITIVE', 'HIGH', 'MEDIUM'],
                       '10': ['UNHEALTHY', 'LOW', 'HIGH'],
                       '11': ['UNHEALTHY', 'MEDIUM', 'MEDIUM'],
                       '12': ['UNHEALTHY', 'HIGH', 'MEDIUM'],
                       '13': ['VERY_UNHEALTHY', 'LOW', 'HIGH'],
                       '14': ['VERY_UNHEALTHY', 'MEDIUM', 'HIGH'],
                       '15': ['VERY_UNHEALTHY', 'HIGH', 'MEDIUM'],
                       '16': ['HAZARDOUS', 'LOW', 'HIGH'],
                       '17': ['HAZARDOUS', 'MEDIUM', 'HIGH'],
                       '18': ['HAZARDOUS', 'HIGH', 'HIGH']}

FAN_LOW = [1,2,3,5,6]               # Numbers of rule that output FAN is LOW
FAN_MEDIUM = [4,7,8,9,11,12,15]     # Numbers of rule that output FAN is MEDIUM
FAN_HIGH = [10,13,14,16,17,18]      # Numbers of rule that output FAN is HIGH

def get_label(var: str, r_num: int, pos: int):
    if var == 'aqi':
        if r_num >= 1 and r_num <= 3 and pos == 1:
            return 'GOOD'
        elif r_num >= 4 and r_num <= 6 and pos == 2:
            return 'MODERATE'
        elif r_num >= 7 and r_num <= 9 and pos == 3:
            return 'UNHEALTHY_SENSITIVE'
        elif r_num >= 10 and r_num <= 12 and pos == 4:
            return 'UNHEALTHY'
        elif r_num >= 13 and r_num <= 15 and pos == 5:
            return 'VERY_UNHEALTHY'
        elif r_num >= 16 and r_num <= 18 and pos == 6:
            return 'HAZARDOUS'
    elif var == 'flowrate':
        if (r_num % 3 == 1) and pos == 1:
            return 'LOW'
        elif (r_num % 3 == 2) and pos == 2:
            return 'MEDIUM'
        elif (r_num % 3 == 0) and pos == 3:
            return 'HIGH'
    elif var == 'fan':
        if (r_num in FAN_LOW) and pos == 1:
            return 'LOW'
        elif (r_num in FAN_MEDIUM) and pos == 2:
            return 'MEDIUM'
        elif (r_num in FAN_HIGH) and pos == 3:
            return 'HIGH'
    else:
        return ''
    
def get_color(var: str, r_num: int, pos: int):
    if var == 'aqi':
        if r_num >= 1 and r_num <= 3 and pos == 1:
            return 'r'
        elif r_num >= 4 and r_num <= 6 and pos == 2:
            return 'r'
        elif r_num >= 7 and r_num <= 9 and pos == 3:
            return 'r'
        elif r_num >= 10 and r_num <= 12 and pos == 4:
            return 'r'
        elif r_num >= 13 and r_num <= 15 and pos == 5:
            return 'r'
        elif r_num >= 16 and r_num <= 18 and pos == 6:
            return 'r'
    elif var == 'flowrate':
        if (r_num % 3 == 1) and pos == 1:
            return 'r'
        elif (r_num % 3 == 2) and pos == 2:
            return 'r'
        elif (r_num % 3 == 0) and pos == 3:
            return 'r'
    elif var == 'fan':
        if (r_num in FAN_LOW) and pos == 1:
            return 'r'
        elif (r_num in FAN_MEDIUM) and pos == 2:
            return 'r'
        elif (r_num in FAN_HIGH) and pos == 3:
            return 'r'
    else:
        return 'black'
    
# def plot_rules_prototype(log_rules: dict, aqi: float, flowrate: float):
#     good, moderate, unhealthy_sens, unhealthy, very_unhealthy, hazardous = aqi_fuzzy()
#     low_fr, medium_fr, high_fr = flowrate_fuzzy()
#     low_fan, medium_fan, high_fan = fan_fuzzy()
#     x = [i for i in range(0,100)]
#     y = [aqi for i in range(0,100)]
#     fig, (ax0, ax1, ax2) = plt.subplots(1,3)
#     fig.suptitle('Inference')
#  # ax0 is aqi plot
#     ax0.plot(x_aqi, good, 'r', linewidth=2.5, label='Good', zorder=0)
#     ax0.plot(x_aqi, moderate, color='0.75', linewidth=2.5)
#     ax0.plot(x_aqi, unhealthy_sens, color='0.75', linewidth=2.5)
#     ax0.plot(x_aqi, unhealthy, color='0.75', linewidth=2.5)
#     ax0.plot(x_aqi, very_unhealthy, color='0.75', linewidth=2.5)
#     ax0.plot(x_aqi, hazardous, color='0.75', linewidth=2.5)
#     ax0.axvline(x = aqi, ymax=log_rules['1'][0], color='b', linewidth=2.5)
#     ax0.axhline(y = log_rules['1'][0], color = 'b', linewidth=2.5, xmin=0, xmax=aqi/500.0)
#     ax0.axhline(y = log_rules['1'][0], color = 'b', linewidth=2.5, xmin=aqi/500.0, linestyle='--')
#     ax0.set_title('Air Quality Index (AQI)')
#     ax0.legend()
#     # ax1 is flowrate plot
#     ax1.plot(x_flowrate, low_fr, 'r', linewidth=2.5, label='Low', zorder=0)
#     ax1.plot(x_flowrate, medium_fr, color='0.75', linewidth=2.5)
#     ax1.plot(x_flowrate, high_fr, color='0.75', linewidth=2.5)
#     ax1.axvline(x = flowrate, ymax=log_rules['1'][1], color = 'b', linewidth=2.5)
#     ax1.axhline(y = log_rules['1'][1], color = 'b', xmin=0, xmax=flowrate/60.0, linewidth=2.5)
#     ax1.axhline(y = log_rules['1'][1], color = 'b', xmin=flowrate/60.0, linewidth=2.5, linestyle='--')
#     ax1.set_title('Air Filter Flowrate')
#     ax1.legend()
#     # ax2 is fanspeed plot
#     ax2.plot(x_fanspeed, low_fan, 'r', linewidth=2.5, label='Low', zorder=0)
#     ax2.plot(x_fanspeed, medium_fan, color='0.75', linewidth=2.5)
#     ax2.plot(x_fanspeed, high_fan, color='0.75', linewidth=2.5)
#     ax2.axhline(y = min(log_rules['1'][0], log_rules['1'][1]), color = 'b', linewidth=2.5)
#     ax2.set_title('Fan Speed Percentage')
#     ax2.legend()
#     plt.show()