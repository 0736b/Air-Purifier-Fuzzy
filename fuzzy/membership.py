import numpy as np
import warnings
warnings.filterwarnings("ignore")

'''universe'''
x_aqi = np.arange(0,501,1)
x_flowrate = np.arange(0,101,1)
x_fanspeed = np.arange(0,101,1)

def trapmf(x: float, params: list[int]) -> float:
    '''returns fuzzy membership values computed using the following trapezoidal membership function f(x;a,b,c,d) = max(min((x-a/b-a),1,(d-x/d-c)),0)'''
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    return max(min(((x-a) / (b-a)), 1, ((d-x) / (d-c))), 0)

def trimf(x: float, params: list[int]) -> float:
    '''returns fuzzy membership values computed using the following triangular membership function f(x;a,b,c) = max(min((x-a / b-a), (c-x / c-b)),0)'''
    a = params[0]
    b = params[1]
    c = params[2]
    return max(min(((x-a) / (b-a)), ((c-x) / (c-b))), 0)    

'''Input 1 : Air Quality Index Membership'''
# Good
def aqi_good(air: float) -> float:
    return trapmf(air, [-1,0,30,60])
    # return trimf(air, [-999999999,30,60])
# Moderate
def aqi_moderate(air: float) -> float:
    return trimf(air, [35,65,100])
# Unhealthy for Sensitive Groups
def aqi_unhealthy_sensitive(air: float) -> float:
    return trimf(air, [75,110,150])
# Unhealthy
def aqi_unhealthy(air: float) -> float:
    return trimf(air, [100, 150, 200])
# Very Unhealthy
def aqi_very_unhealthy(air: float) -> float:
    return trimf(air, [150, 225, 300])
# Hazardous
def aqi_hazardous(air: float) -> float:
    return trapmf(air,[200,325,500,501])
    # return trimf(air, [200, 325, 500])

'''Input 2 : Air Filter flow-rate Membership'''
# Low
def filter_low(flowrate: float) -> float:
    return trapmf(flowrate, [-1,0,20,40])
    # return trimf(flowrate, [0,20,40])
# Medium
def filter_medium(flowrate: float) -> float:
    return trimf(flowrate, [20,50,70])
# High
def filter_high(flowrate: float) -> float:
    return trimf(flowrate, [60,100,101])

'''Output : Fan speed percentage'''
# Low
def fan_low(fan: float) -> float:
    return trapmf(fan, [-1,0,10,50])
    # return trimf(fan, [-20,25,50])
# Medium
def fan_medium(fan: float) -> float:
    return trimf(fan, [25,70,100])
# High
def fan_high(fan: float) -> float:
    return trimf(fan, [75,100,101])