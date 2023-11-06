import pandas as pd
import numpy as np
import random




import pandas as pd

url='https://drive.google.com/uc?id=1-crPzL6qMinByPzsrEHhGn1EJ1MfD3GX'
df = pd.read_csv(url, names=list(range(0, 100, 1)))
city_map_list = df.values.tolist()

city_map_list = np.array(city_map_list)


####

# ###Обрезанная версия - возвращается на базу после каждого заказа

#### 

courier_location = (17, 99)
orders_location = [(42, 76), (27, 80), (43, 52), (26, 75)]

courier_value_map = np.zeros((city_map_list.shape[0]+2, city_map_list.shape[1]+2))
courier_value_map[1:-1,1:-1] = city_map_list[:,:]
courier_value_map[courier_location[1]+1][courier_location[0]+1] = -1



# Функция вычисления стоимости, работает с условием того, что до любой проходимой точки можно добраться

def build_values(map):
    while 1 in map:
        for i in range(1,map.shape[0]-1):
            for j in range(1,map.shape[1]-1):
                if map[i,j] < 1:
                    continue
                
                adjacent = list(filter(lambda x: x != 0 and x != 1,[map[i,j+1], map[i,j-1], map[i+1,j], map[i-1,j]]))
                if adjacent:
                    map[i,j] = min(adjacent) +10
                    
                    
# Вычисляем для курьера

build_values(courier_value_map)




arbitrary_order = [i for i in range(len(orders_location))] ## По порядку


def build_root(courier_location, courier_value_map, orders_location):
    route = []
    optimal_order = [i for i in range(len(orders_location))]
    
    for i in range(-1,len(optimal_order)-1):
        temp = []
        curr = orders_location[optimal_order[i+1]]
        while(curr != courier_location):
            adjacent = list(filter( lambda x : courier_value_map[x[1]+1,x[0]+1] != 0, [(curr[0],curr[1]+1), (curr[0]+1,curr[1]), (curr[0],curr[1]-1), (curr[0]-1,curr[1])]))
            curr = min(adjacent, key = (lambda x: courier_value_map[x[1]+1,x[0]+1]))
            temp.append(curr)
        route.extend(temp[::-1])
        route.append(orders_location[optimal_order[i+1]])
        route.extend(temp)
    return route
            
            
route = build_root(courier_location,courier_value_map,orders_location)