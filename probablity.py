import math
import pandas

def probablity (total,part):
    return 1 - math.comb(total-part,4)/math.comb(total,4)
dicts = dict()
for total in range(20,31):
    
    lists =[]
    for parts in range(0,13):
        lists.append(probablity(total,parts))
    dicts[total] = lists
datas = pandas.DataFrame(dicts)
print(datas)

while(True):
    totalinput =int(input("input total :"))
    partsinput =int(input("input parts : "))
    print ("probablity = {}".format(datas[totalinput][partsinput]))
    
    

