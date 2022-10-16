import matplotlib.pyplot as plt
from fuzzy.membership import *
from utils.plot_util import get_label, get_color

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
    ax0.plot(x_aqi, good, linewidth=2.5, label='Good')
    ax0.plot(x_aqi, moderate, linewidth=2.5, label='Moderate')
    ax0.plot(x_aqi, unhealthy_sens, linewidth=2.5, label='Unhealthy for sensitive group')
    ax0.plot(x_aqi, unhealthy, linewidth=2.5, label='Unhealthy')
    ax0.plot(x_aqi, very_unhealthy, linewidth=2.5, label='Very unhealthy')
    ax0.plot(x_aqi, hazardous, linewidth=2.5, label='Hazardous')
    ax0.set_title('Air Quality Index (AQI)')
    ax0.legend()
    # ax1 is flowrate plot
    ax1.plot(x_flowrate, low_fr, linewidth=2.5, label='Low')
    ax1.plot(x_flowrate, medium_fr, linewidth=2.5, label='Medium')
    ax1.plot(x_flowrate, high_fr, linewidth=2.5, label='High')
    ax1.set_title('Air Filter Flowrate')
    ax1.legend()
    # ax2 is fanspeed plot
    ax2.plot(x_fanspeed, low_fan, linewidth=2.5, label='Low')
    ax2.plot(x_fanspeed, medium_fan, linewidth=2.5, label='Medium')
    ax2.plot(x_fanspeed, high_fan, linewidth=2.5, label='High')
    ax2.set_title('Fan Speed Percentage')
    ax2.legend()
    # adjust graph position
    plt.subplots_adjust(left=0.245,bottom=0.036,right=0.755,top=0.97,wspace=0.229,hspace=0.27)
    plt.show()

def plot_output_graph(output_graph: dict, centroid: float):
    low_fan, medium_fan, high_fan = fan_fuzzy()
    centroid_label = 'Centroid = ' + str(round(centroid,4))
    text_offset = len(centroid_label) / 3.5
    x = []
    y = []
    for _x, mem_val in output_graph.items():
        x.append(float(_x))
        y.append(float(mem_val))
    x = np.array(x)
    y = np.array(y)
    plt.plot(x_fanspeed, low_fan, linewidth=3, label='Low', zorder=10)
    plt.plot(x_fanspeed, medium_fan, linewidth=3, label='Medium', zorder=10)
    plt.plot(x_fanspeed, high_fan, linewidth=3, label='High', zorder=10)
    plt.fill_between(x, 0, y, where=y>0, interpolate=True, color='0.35', zorder=5)
    plt.plot([centroid, centroid], [-0.05,1.05], 'r--', lw=3, zorder=15, label='Centroid', clip_on=False)
    props = dict(boxstyle='round', facecolor='white', alpha=1)
    plt.text((centroid - text_offset),-0.05, centroid_label, bbox=props ,zorder=20)
    plt.suptitle('Fan Speed Percentage')
    plt.legend()
    plt.show()
        
def plot_rules(log_rules: dict, aqi: float, flowrate: float):
    good, moderate, unhealthy_sens, unhealthy, very_unhealthy, hazardous = aqi_fuzzy()
    low_fr, medium_fr, high_fr = flowrate_fuzzy()
    low_fan, medium_fan, high_fan = fan_fuzzy()
    x = [i for i in range(0,100)]
    y = [aqi for i in range(0,100)]
    # create subplots
    fig, axs = plt.subplots(nrows=6, ncols=3)
    plt.subplots_adjust(hspace=0.5)
    fig.suptitle("Rules inference")
    # graph settings
    col = 0
    r_num = 1
    # loop
    for ax in axs.reshape(-1):
        if col == 0:
            ax.plot(x_aqi, good, color=get_color('aqi', r_num, 1), linewidth=2.5, label=get_label('aqi',r_num,1))
            ax.plot(x_aqi, moderate, color=get_color('aqi',r_num,2), linewidth=2.5, label=get_label('aqi',r_num,2))
            ax.plot(x_aqi, unhealthy_sens, color=get_color('aqi',r_num,3), linewidth=2.5, label=get_label('aqi',r_num,3))
            ax.plot(x_aqi, unhealthy, color=get_color('aqi',r_num,4), linewidth=2.5, label=get_label('aqi',r_num,4))
            ax.plot(x_aqi, very_unhealthy, color=get_color('aqi',r_num,5), linewidth=2.5, label=get_label('aqi',r_num,5))
            ax.plot(x_aqi, hazardous, color=get_color('aqi',r_num,6), linewidth=2.5, label=get_label('aqi',r_num,6))
            ax.axvline(x = aqi, ymax=log_rules[str(r_num)][0], color='b', linewidth=2.5)
            ax.axhline(y = log_rules[str(r_num)][0], color = 'b', linewidth=2.5, xmin=0, xmax=aqi/500.0)
            ax.axhline(y = log_rules[str(r_num)][0], color = 'b', linewidth=2.5, xmin=aqi/500.0, linestyle='--')
            ax.set_title('Air Quality Index (AQI)')
            ax.legend()
            col += 1
        elif col == 1:
            ax.plot(x_flowrate, low_fr, color=get_color('flowrate',r_num,1), linewidth=2.5, label=get_label('flowrate', r_num, 1))
            ax.plot(x_flowrate, medium_fr, color=get_color('flowrate',r_num,2), linewidth=2.5, label=get_label('flowrate', r_num, 2))
            ax.plot(x_flowrate, high_fr, color=get_color('flowrate',r_num,3), linewidth=2.5, label=get_label('flowrate', r_num, 3))
            ax.axvline(x = flowrate, ymax=log_rules[str(r_num)][1], color = 'b', linewidth=2.5)
            ax.axhline(y = log_rules[str(r_num)][1], color = 'b', xmin=0, xmax=flowrate/60.0, linewidth=2.5)
            ax.axhline(y = log_rules[str(r_num)][1], color = 'b', xmin=flowrate/60.0, linewidth=2.5, linestyle='--')
            ax.set_title('Air Filter Flowrate')
            ax.legend()
            col += 1
        elif col == 2:
            ax.plot(x_fanspeed, low_fan, color=get_color('fan', r_num, 1), linewidth=2.5, label=get_label('fan', r_num, 1))
            ax.plot(x_fanspeed, medium_fan, color=get_color('fan', r_num, 2), linewidth=2.5, label=get_label('fan', r_num, 2))
            ax.plot(x_fanspeed, high_fan, color=get_color('fan', r_num, 3), linewidth=2.5, label=get_label('fan', r_num, 3))
            ax.axhline(y = min(log_rules[str(r_num)][0], log_rules[str(r_num)][1]), color = 'b', linewidth=2.5, linestyle='--')
            ax.set_title('Fan Speed Percentage')
            ax.legend()
            r_num += 1
            col = 0 
    plt.show()        
    
    


if __name__ == '__main__':
    plot_membershipfn()
    # plot_rules()