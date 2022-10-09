import matplotlib.pyplot as plt
from fuzzy.membership import *

def aqi_fuzzy():
    good = []
    moderate = []
    unhealthy_sens = []
    unhealthy = []
    very_unhealthy = []
    hazardous = []
    for x in x_aqi:
        good.append(aqi_good(x))
        moderate.append(aqi_moderate(x))
        unhealthy_sens.append(aqi_unhealthy_sensitive(x))
        unhealthy.append(aqi_unhealthy(x))
        very_unhealthy.append(aqi_very_unhealthy(x))
        hazardous.append(aqi_hazardous(x))
    return good, moderate, unhealthy_sens, unhealthy, very_unhealthy, hazardous

def flowrate_fuzzy():
    low_fr = []
    medium_fr = []
    high_fr = []
    for x in x_flowrate:
        low_fr.append(filter_low(x))
        medium_fr.append(filter_medium(x))
        high_fr.append(filter_high(x))
    return low_fr, medium_fr, high_fr

def fan_fuzzy():
    low_fan = []
    medium_fan = []
    high_fan = []
    for x in x_fanspeed:
        low_fan.append(fan_low(x))
        medium_fan.append(fan_medium(x))
        high_fan.append(fan_high(x))
    return low_fan, medium_fan, high_fan
    

def plot_membershipfn():
    # data preparing
    good, moderate, unhealthy_sens, unhealthy, very_unhealthy, hazardous = aqi_fuzzy()
    low_fr, medium_fr, high_fr = flowrate_fuzzy()
    low_fan, medium_fan, high_fan = fan_fuzzy()
    
    # setup
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8,9))
    # ax0 is aqi plot
    ax0.plot(x_aqi, good, linewidth=1.5, label='Good')
    ax0.plot(x_aqi, moderate, linewidth=1.5, label='Moderate')
    ax0.plot(x_aqi, unhealthy_sens, linewidth=1.5, label='Unhealthy for sensitive group')
    ax0.plot(x_aqi, unhealthy, linewidth=1.5, label='Unhealthy')
    ax0.plot(x_aqi, very_unhealthy, linewidth=1.5, label='Very unhealthy')
    ax0.plot(x_aqi, hazardous, linewidth=1.5, label='Hazardous')
    ax0.set_title('Air Quality Index (AQI)')
    ax0.legend()
    # ax1 is flowrate plot
    ax1.plot(x_flowrate, low_fr, linewidth=1.5, label='Low')
    ax1.plot(x_flowrate, medium_fr, linewidth=1.5, label='Medium')
    ax1.plot(x_flowrate, high_fr, linewidth=1.5, label='High')
    ax1.set_title('Air filter flowrate')
    ax1.legend()
    # ax2 is fanspeed plot
    ax2.plot(x_fanspeed, low_fan, linewidth=1.5, label='Low')
    ax2.plot(x_fanspeed, medium_fan, linewidth=1.5, label='Medium')
    ax2.plot(x_fanspeed, high_fan, linewidth=1.5, label='High')
    ax2.set_title('Fan speed percentage')
    ax2.legend()
    plt.subplots_adjust(left=0.245,bottom=0.036,right=0.755,top=0.97,wspace=0.229,hspace=0.27)
    plt.show()



if __name__ == '__main__':
    plot_membershipfn()