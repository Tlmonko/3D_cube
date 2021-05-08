def in_polygon(x, y, x_polygon, y_polygon):
    result = False
    for i in range(len(y_polygon)):
        if (((y_polygon[i] <= y < y_polygon[i - 1]) or (y_polygon[i - 1] <= y < y_polygon[i])) and
                (x > (x_polygon[i - 1] - x_polygon[i]) * (y - y_polygon[i]) / (y_polygon[i - 1] - y_polygon[i]) +
                 x_polygon[i])): result = not result
    return result
