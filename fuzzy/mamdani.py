from fuzzy.fuzzifier import fuzzification
from fuzzy.inference import inference
from dataclasses import dataclass

class AirPurifier_Mamdani:
    '''Mamdani'''
    
    @dataclass
    class Result:
        output_graph: dict
        crisp_value_output: float
        
        def __init__(self):
            self.output_graph = {}
            self.crisp_value_output = 0.0
    
    def __init__ (self, aqi: float, flowrate: float):
        self.aqi = aqi
        self.flowrate = flowrate
        self.result = self.Result()
    
    def set_input(self, new_aqi: float, new_flowrate: float):
        self.aqi = new_aqi
        self.flowrate = new_flowrate
    
    def get_crisp_value_output(self):
        return self.crisp_value_output
        
    def run(self):
        self.fuzzificated_aqi, self.fuzzificated_flowrate = fuzzification(self.aqi, self.flowrate)
        self.result.crisp_value_output, self.result.output_graph = inference(self.fuzzificated_aqi, self.fuzzificated_flowrate)
        return self.result