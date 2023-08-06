import math


def acceleration(v_delta, t, vf, vi):
    if v_delta and t:
        return v_delta / t
    elif vi and vf and t:
        return (vf - vi) / t
    else:
        return 0

def v_average(x_delta, t, vf, vi):
    if x_delta and t:
        return x_delta / t
    elif vi and vf:
        return (vf - vi) / 2
    else:
        return 0

def v_final(vi, a, t=math.inf, x_delta=math.inf):
    if not vi or not a:
        return 0

    if t != math.inf:
        return vi + a * t

    if x_delta != math.inf:
        return vi ** 2 + 2 * a * x_delta

    return 0

def change_in_position(vi, t, a):
    if vi and t and a:
        return vi * t + 0.5 * a * (t ** 2)
    return 0

def displacement(t, vf, vi):
    if vi and vf and t:
        return 0.5 * (vi + vf) * t
    return 0