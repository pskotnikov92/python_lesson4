#1 Не пойму как работает второй агрумент в функции
from random import *

def F(list_name, len_list):
    return choices(list_name, k=len_list)

list_100_name = F(["name_1", "name_2", "name_3", "name_4", "name_5", "name_6", "name_7", "name_8", "name_9", "name_10", "name_11", "name_12", "name_13", "name_14", "name_15", "name_16", "name_17", "name_18", "name_19", "name_20"], len_list=3)
print(list_100_name)

