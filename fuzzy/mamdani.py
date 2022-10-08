from fuzzy.fuzzifier import fuzzification
from fuzzy.inference import inference

class AirPurifier_Mamdani:

    def __init__ (self, aqi: float, flowrate: float):
        self.aqi = aqi
        self.flowrate = flowrate
        self.crisp_value = 0
    
    def set_input(self, new_aqi: float, new_flowrate: float):
        self.aqi = new_aqi
        self.flowrate = new_flowrate
    
    def get_crisp_value(self):
        return self.crisp_value
        
    def run(self):
        self.fuzzificated_aqi, self.fuzzificated_flowrate = fuzzification(self.aqi, self.flowrate)
        self.crisp_value = inference(self.fuzzificated_aqi, self.fuzzificated_flowrate)
    