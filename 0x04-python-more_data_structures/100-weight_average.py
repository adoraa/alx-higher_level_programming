#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weighted_sum = 0
    sum_of_weights = 0

    for score, weight in my_list:
        weighted_sum += score * weight
        sum_of_weights += weight

    if sum_of_weights == 0:
        return 0
    else:
        return weighted_sum / sum_of_weights
