from fuzzy.mamdani import AirPurifier_Mamdani
from plot import plot_output_graph

if __name__ == "__main__":
    fis = AirPurifier_Mamdani(80.0,25.0)
    result = fis.run()
    print(result.crisp_value_output)
    plot_output_graph(result.output_graph, result.crisp_value_output)