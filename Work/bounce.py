# bounce.py
#
# Exercise 1.5
height = 100 # 100 meters

for i in range(10):
    height = height * 3/5
    print(f'[{i+1}]: {round(height, ndigits=4)}m')
