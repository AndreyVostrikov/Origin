def smart_water_calculation(time_in_the_shower):
    if time_in_the_shower < 0:
        return ('Enter positive number!!!')
    else:
        number_of_bottles = time_in_the_shower * 12
        return number_of_bottles


print(smart_water_calculation(10))