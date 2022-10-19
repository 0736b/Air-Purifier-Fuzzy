import numpy as np
from fuzzy.membership import fan_low, fan_medium, fan_high

rules_str = {'1': 'if AQI is GOOD and FILTER is LOW then FAN is LOW',
                       '2': 'if AQI is GOOD and FILTER is MEDIUM then FAN is LOW',
                       '3': 'if AQI is GOOD and FILTER is HIGH then FAN is LOW',
                       '4': 'if AQI is MODERATE and FILTER is LOW then FAN is MEDIUM',
                       '5': 'if AQI is MODERATE and FILTER is MEDIUM then FAN is LOW',
                       '6': 'if AQI is MODERATE and FILTER is HIGH then FAN is LOW',
                       '7': 'if AQI is UNHEALTHY_SENSITIVE and FILTER is LOW then FAN is MEDIUM',
                       '8': 'if AQI is UNHEALTHY_SENSITIVE and FILTER is MEDIUM then FAN is MEDIUM',
                       '9': 'if AQI is UNHEALTHY_SENSITIVE and FILTER is HIGH then FAN is MEDIUM',
                       '10': 'if AQI is UNHEALTHY and FILTER is LOW then FAN is HIGH',
                       '11': 'if AQI is UNHEALTHY and FILTER is MEDIUM then FAN is MEDIUM',
                       '12': 'if AQI is UNHEALTHY and FILTER is HIGH then FAN is MEDIUM',
                       '13': 'if AQI is VERY_UNHEALTHY and FILTER is LOW then FAN is HIGH',
                       '14': 'if AQI is VERY_UNHEALTHY and FILTER is MEDIUM then FAN is HIGH',
                       '15': 'if AQI is VERY_UNHEALTHY and FILTER is HIGH then FAN is MEDIUM',
                       '16': 'if AQI is HAZARDOUS and FILTER is LOW then FAN is HIGH',
                       '17': 'if AQI is HAZARDOUS and FILTER is MEDIUM then FAN is HIGH',
                       '18': 'if AQI is HAZARDOUS and FILTER is HIGH then FAN is HIGH'}

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
        else:
            return '0.85'
    elif var == 'flowrate':
        if (r_num % 3 == 1) and pos == 1:
            return 'r'
        elif (r_num % 3 == 2) and pos == 2:
            return 'r'
        elif (r_num % 3 == 0) and pos == 3:
            return 'r'
        else:
            return '0.85'
    elif var == 'fan':
        if (r_num in FAN_LOW) and pos == 1:
            return 'r'
        elif (r_num in FAN_MEDIUM) and pos == 2:
            return 'r'
        elif (r_num in FAN_HIGH) and pos == 3:
            return 'r'
        else:
            return '0.85'
    else:
        return '0.85'
    
def get_z(var: str, r_num: int, pos: int):
    if var == 'aqi':
        if r_num >= 1 and r_num <= 3 and pos == 1:
            return 10
        elif r_num >= 4 and r_num <= 6 and pos == 2:
            return 10
        elif r_num >= 7 and r_num <= 9 and pos == 3:
            return 10
        elif r_num >= 10 and r_num <= 12 and pos == 4:
            return 10
        elif r_num >= 13 and r_num <= 15 and pos == 5:
            return 10
        elif r_num >= 16 and r_num <= 18 and pos == 6:
            return 10
        else:
            return 0
    elif var == 'flowrate':
        if (r_num % 3 == 1) and pos == 1:
            return 10
        elif (r_num % 3 == 2) and pos == 2:
            return 10
        elif (r_num % 3 == 0) and pos == 3:
            return 10
        else:
            return 0
    elif var == 'fan':
        if (r_num in FAN_LOW) and pos == 1:
            return 10
        elif (r_num in FAN_MEDIUM) and pos == 2:
            return 10
        elif (r_num in FAN_HIGH) and pos == 3:
            return 10
        else:
            return 0
    else:
        return 0
    
def fill_fan(r_num: int, alpha: float):
    x = [int(i) for i in range (0,101)]
    y = []
    if r_num in FAN_LOW:
        for _x in x:
            temp = fan_low(_x)
            if temp >= alpha:
                temp = alpha
            y.append(temp)
    elif r_num in FAN_MEDIUM:
        for _x in x:
            temp = fan_medium(_x)
            if temp >= alpha:
                temp = alpha
            y.append(temp)
    if r_num in FAN_HIGH:
        for _x in x:
            temp = fan_high(_x)
            if temp >= alpha:
                temp = alpha
            y.append(temp)
    x = np.array(x)
    y = np.array(y)
    return x, y