points2D = [(1, 2), (15, 25), (30, 15), (3, 4), (4, 5)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])     # sorted using x-axis values.
print('Original list: {}'.format(points2D))
print('Sorted list using x-axis variables: {}'.format(points2D_sorted))
print('Sorted list using y-axis variables: {}'.format(sorted(points2D)))     # sorted using y-axis values.
print('Sorted list using sum of x and y values: {}'.format(sorted(points2D, key=lambda x: x[0] + x[1])))