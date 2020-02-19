def Theadder(addvalue):
    def tempFunc(x):
        return x+addvalue
    return tempFunc

def get_sum_metrics(predictions, metrics=[]):
    for i in range(3):
        metrics.append(Theadder(i))
    
        

print(get_sum_metrics(0))
print(get_sum_metrics(1))
print(get_sum_metrics(2))
print(get_sum_metrics(3))