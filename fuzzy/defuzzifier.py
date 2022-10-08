from fuzzy.membership import x_fanspeed, fan_low, fan_medium, fan_high

def gen_output_membership():
    mem_fan_low = {}
    mem_fan_medium = {}
    mem_fan_high = {}
    for x in x_fanspeed:
        mem_fan_low[x] = fan_low(x)
        mem_fan_medium[x] = fan_medium(x)
        mem_fan_high[x] = fan_high(x)
    return mem_fan_low, mem_fan_medium, mem_fan_high

def centroid(output_g: dict):
    centroid = 0
    y = 0
    yx = 0
    for x, mem_val in output_g.items():
        y += x * mem_val
        yx += mem_val
    centroid = y / yx
    return centroid