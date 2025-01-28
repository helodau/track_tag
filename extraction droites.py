import math

def calculate_geometry(x1, y1, x2, y2, x3, y3, x4, y4):
    def line_equation(x1, y1, x2, y2):
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        return a, b, c

    def intersection(a1, b1, c1, a2, b2, c2):
        det = a1 * b2 - a2 * b1
        if det == 0:
            return None
        x = (b2 * (-c1) - b1 * (-c2)) / det
        y = (a1 * (-c2) - a2 * (-c1)) / det
        return x, y

    a_t, b_t, c_t = line_equation(x1, y1, x2, y2)
    a_o, b_o, c_o = line_equation(x3, y3, x4, y4)

    intersection_point = intersection(a_t, b_t, c_t, a_o, b_o, c_o)

    def is_on_segment(x, y, x1, y1, x2, y2):
        return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

    angle = None
    if intersection_point:
        x_int, y_int = intersection_point
        if is_on_segment(x_int, y_int, x1, y1, x2, y2):
            slope_t = -a_t / b_t if b_t != 0 else float('inf')
            slope_o = -a_o / b_o if b_o != 0 else float('inf')
            if slope_t != float('inf') and slope_o != float('inf'):
                tan_theta = abs((slope_o - slope_t) / (1 + slope_o * slope_t))
                angle = math.degrees(math.atan(tan_theta))
            else:
                angle = 90.0

    if a_t != 0:
        a_m = -b_t
        b_m = a_t
        c_m = -(a_m * x3 + b_m * y3)
    else:
        a_m = 1
        b_m = 0
        c_m = -x3

    intersection_m_t = intersection(a_t, b_t, c_t, a_m, b_m, c_m)

    x_j = (x1 + x2) / 2
    y_j = (y1 + y2) / 2

    distance_i_j = None
    if intersection_m_t:
        x_i, y_i = intersection_m_t
        distance_i_j = math.sqrt((x_i - x_j) ** 2 + (y_i - y_j) ** 2)

    return {
        "intersection_T_O": intersection_point,
        "angle": angle,
        "intersection_M_T": intersection_m_t,
        "distance_I_J": distance_i_j
    }

result = calculate_geometry(-0.41, -2.98, 4, -3.05, 2.15, 1.70, 2.04, -1.63)
print(result)

