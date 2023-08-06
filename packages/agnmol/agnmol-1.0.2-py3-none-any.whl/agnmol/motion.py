import math


def acceleration(v_delta=math.inf, t=math.inf, vf=math.inf, vi=math.inf):
    if v_delta != math.inf and t != math.inf:
        return v_delta / t
    elif vi != math.inf and vf != math.inf and t != math.inf:
        return (vf - vi) / t
    else:
        return 0

def v_average(x_delta=math.inf, t=math.inf, vf=math.inf, vi=math.inf):
    if x_delta != math.inf and t != math.inf:
        return x_delta / t
    elif vi != math.inf and vf != math.inf:
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
    return vi * t + 0.5 * a * (t ** 2)

def displacement(t, vf, vi):
    return 0.5 * (vi + vf) * t