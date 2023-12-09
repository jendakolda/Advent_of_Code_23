from math import sqrt

time_A = (48, 98, 90, 83)
distance_A = (390, 1103, 1112, 1360)
win_product = 1

time_B = 48989083
distance_B = 390110311121360


def is_winning(duration, time, distance):
    return duration * (time - duration) > distance


for t, d in zip(time_A, distance_A):
    win_count = 0
    for duration in range(t):
        if is_winning(duration, t, d):
            win_count += 1
    win_product *= win_count
print(f'Part A: {win_product}')

lo = (time_B - sqrt((- time_B) ** 2 - 4 * distance_B)) / 2
hi = (time_B + sqrt((-time_B) ** 2 - 4 * distance_B)) / 2
print(f'Part B: {int(hi)-int(lo)}')
