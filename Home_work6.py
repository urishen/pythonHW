dist_a = 2
dist_b = 3
prc_v = 10
finish_d = 1
while dist_a <= dist_b:
    dist_a = (dist_a/100*prc_v) + dist_a
    finish_d += 1
print(finish_d)