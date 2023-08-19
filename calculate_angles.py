import numpy as np


def calculate_angle(first_point, mid_point, end_point):
    a = np.array(first_point) # First
    b = np.array(mid_point) # Mid
    c = np.array(end_point) # End

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle >180.0:
        angle = 360-angle

    return angle