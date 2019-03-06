import time

""" 
    time.clock() - в Unix, возвращает текущее время. В Windows, возвращает время, 
прошедшее с момента первого вызова данной функции. 
    time.time() - время, выраженное в секундах с начала эпохи.
"""

start = time.clock()
u = 10 * 10
elapsed = (time.clock() - start)
print('Результат 1-го теста:', elapsed)


start = time.time()
z = 10 * 10
elapsed2 = (time.time() - start)
print('Результат 2-го теста:', elapsed2)



