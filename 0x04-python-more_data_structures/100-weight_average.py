# #!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = []
    res2 = []
    for x in my_list:
        # print(f"({x[0]},{x[1]}) = {x[0] * x[1]}")  
        res.append(x[0] * x[1])  
        res2.append(x[1])  

    result = sum(res)/sum(res2)
    return (result)