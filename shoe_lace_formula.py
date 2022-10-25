points = [(2, 5), (4, 9), (1, 8), (6, 2), (2, 6)]


xs , ys = zip(*points)

left = 0
right = 0

for i in range(len(points)):
    left += xs[i] * ys[(i+1) % len(points)]
    left += ys[i] * xs[(i + 1) % len(points)]

area = 0.5 * (left - right)
print(area)