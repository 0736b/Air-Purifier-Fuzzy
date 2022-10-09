def centroid(output_g: dict):
    '''defuzzification with centroid'''
    centroid = 0
    y = 0
    yx = 0
    for x, mem_val in output_g.items():
        y += x * mem_val
        yx += mem_val
    centroid = y / yx
    return centroid