from fuzzy.mamdani import AirPurifier_Mamdani
from plot import plot_output_graph, plot_rules

if __name__ == "__main__":
    # fis = AirPurifier_Mamdani(80.0,25.0)
    # result = fis.run()
    # plot_rules(result.log_rules, result.aqi, result.flowrate)
    # plot_output_graph(result.output_graph, result.crisp_value_output, 80.0, 25.0)
    aqi_test = [97.0, 196.0, 130.0, 52.0, 203.0, 245.0, 317.0, 22.0]
    flow_test = [47.0, 39.0, 47.0, 49.0, 79.0, 84.0, 75.0, 94.0]
    fis = AirPurifier_Mamdani(0,0)
    for i in range(len(aqi_test)):
        print('AQI:', aqi_test[i], ' Flowrate:', flow_test[i])
        fis.set_input(aqi_test[i], flow_test[i])
        result = fis.run()
        plot_rules(result.log_rules, result.aqi, result.flowrate)
        plot_output_graph(result.output_graph, result.crisp_value_output, aqi_test[i], flow_test[i])