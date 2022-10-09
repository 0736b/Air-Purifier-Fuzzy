import numpy as np
from fuzzy.defuzzifier import centroid
from fuzzy.fuzzifier import gen_output_membership

'''
DEFINE RULES
1 - if AQI is GOOD and FILTER is LOW then FAN is LOW
2 - if AQI is GOOD and FILTER is MEDIUM then FAN is LOW
3 - if AQI is GOOD and FILTER is HIGH then FAN is LOW
4 - if AQI is MODERATE and FILTER is LOW then FAN is MEDIUM
5 - if AQI is MODERATE and FILTER is MEDIUM then FAN is LOW
6 - if AQI is MODERATE and FILTER is HIGH then FAN is LOW
7 - if AQI is UNHEALTHY_SENSITIVE and FILTER is LOW then FAN is MEDIUM
8 - if AQI is UNHEALTHY_SENSITIVE and FILTER is MEDIUM then FAN is MEDIUM
9 - if AQI is UNHEALTHY_SENSITIVE and FILTER is HIGH then FAN is MEDIUM
10 - if AQI is UNHEALTHY and FILTER is LOW then FAN is HIGH
11 - if AQI is UNHEALTHY and FILTER is MEDIUM then FAN is MEDIUM
12 - if AQI is UNHEALTHY and FILTER is HIGH then FAN is MEDIUM
13 - if AQI is VERY_UNHEALTHY and FILTER is LOW then FAN is HIGH
14 - if AQI is VERY_UNHEALTHY and FILTER is MEDIUM then FAN is HIGH
15 - if AQI is VERY_UNHEALTHY and FILTER is HIGH then FAN is MEDIUM
16 - if AQI is HAZARDOUS and FILTER is LOW then FAN is HIGH
17 - if AQI is HAZARDOUS and FILTER is MEDIUM then FAN is HIGH
18 - if AQI is HAZARDOUS and FILTER is HIGH then FAN is HIGH
'''

FAN_LOW = [1,2,3,5,6]               # Numbers of rule that output FAN is LOW
FAN_MEDIUM = [4,7,8,9,11,12,15]     # Numbers of rule that output FAN is MEDIUM
FAN_HIGH = [10,13,14,16,17,18]      # Numbers of rule that output FAN is HIGH

def find_alphacut_from_inputs(fc_aqi: dict, fc_flowrate: dict):
    '''evaluate all rules from inputs'''
    rules_alphacut = {}
    rules_alphacut['1'] = np.fmin(fc_aqi['GOOD'], fc_flowrate['LOW'])
    rules_alphacut['2'] = np.fmin(fc_aqi['GOOD'], fc_flowrate['MEDIUM'])
    rules_alphacut['3'] = np.fmin(fc_aqi['GOOD'], fc_flowrate['HIGH'])
    rules_alphacut['4'] = np.fmin(fc_aqi['MODERATE'], fc_flowrate['LOW'])
    rules_alphacut['5'] = np.fmin(fc_aqi['MODERATE'], fc_flowrate['MEDIUM'])
    rules_alphacut['6'] = np.fmin(fc_aqi['MODERATE'], fc_flowrate['HIGH'])
    rules_alphacut['7'] = np.fmin(fc_aqi['UNHEALTHY_SENSITIVE'], fc_flowrate['LOW'])
    rules_alphacut['8'] = np.fmin(fc_aqi['UNHEALTHY_SENSITIVE'], fc_flowrate['MEDIUM'])
    rules_alphacut['9'] = np.fmin(fc_aqi['UNHEALTHY_SENSITIVE'], fc_flowrate['HIGH'])
    rules_alphacut['10'] = np.fmin(fc_aqi['UNHEALTHY'], fc_flowrate['LOW'])
    rules_alphacut['11'] = np.fmin(fc_aqi['UNHEALTHY'], fc_flowrate['MEDIUM'])
    rules_alphacut['12'] = np.fmin(fc_aqi['UNHEALTHY'], fc_flowrate['HIGH'])
    rules_alphacut['13'] = np.fmin(fc_aqi['VERY_UNHEALTHY'], fc_flowrate['LOW'])
    rules_alphacut['14'] = np.fmin(fc_aqi['VERY_UNHEALTHY'], fc_flowrate['MEDIUM'])
    rules_alphacut['15'] = np.fmin(fc_aqi['VERY_UNHEALTHY'], fc_flowrate['HIGH'])
    rules_alphacut['16'] = np.fmin(fc_aqi['HAZARDOUS'], fc_flowrate['LOW'])
    rules_alphacut['17'] = np.fmin(fc_aqi['HAZARDOUS'], fc_flowrate['MEDIUM'])
    rules_alphacut['18'] = np.fmin(fc_aqi['HAZARDOUS'], fc_flowrate['HIGH'])
    return rules_alphacut

def alphacut_for_output(rules):
    '''find alphacut from union graph in same Output fuzzy set'''
    low_alpha = float('-inf')
    med_alpha = float('-inf')
    high_alpha = float('-inf')
    # union ( max(alphacut from all rules that output FAN is LOW ) )
    for low in FAN_LOW:
        low_alpha = np.fmax(rules[str(low)], low_alpha)
    # union ( max(alphacut from all rules that output FAN is MEDIUM ) )
    for med in FAN_MEDIUM:
        med_alpha = np.fmax(rules[str(med)], med_alpha)
    # union ( max(alphacut from all rules that output FAN is HIGH ) )
    for high in FAN_HIGH:
        high_alpha = np.fmax(rules[str(high)], high_alpha)
    return low_alpha, med_alpha, high_alpha
        
def union_graph_alphacut(low_alpha, medium_alpha, high_alpha):
    '''union output graph from all rules'''
    output_graph = {}
    output_low_g, output_medium_g, output_high_g = gen_output_membership()
    # active alphacut on graph
    act_low_g = {}
    act_medium_g = {}
    act_high_g = {}
    for x, mem_val in output_low_g.items():
        if mem_val <= low_alpha:
            act_low_g[x] = mem_val
        else:
            act_low_g[x] = 0.0
    for x, mem_val in output_medium_g.items():
        if mem_val <= medium_alpha:
            act_medium_g[x] = mem_val
        else:
            act_medium_g[x] = 0.0
    for x, mem_val in output_high_g.items():
        if mem_val <= high_alpha:
            act_high_g[x] = mem_val
        else:
            act_high_g[x] = 0.0
    # union output graph
    for i in range (0,101,1):
        output_graph[i] = np.fmax(act_low_g.get(i), (np.fmax(act_medium_g.get(i), act_high_g.get(i))))
    return output_graph
        
def inference(fc_aqi: dict, fc_flowrate: dict) -> list[float]:
    '''fuzzy inference'''
    alpha_from_inputs = find_alphacut_from_inputs(fc_aqi, fc_flowrate)
    output_low_alphacut, output_medium_alphacut, output_high_alphacut = alphacut_for_output(alpha_from_inputs)
    output_graph = union_graph_alphacut(output_low_alphacut, output_medium_alphacut, output_high_alphacut)
    output_val = centroid(output_graph)
    return output_val