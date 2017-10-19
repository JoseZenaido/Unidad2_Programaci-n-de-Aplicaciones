from math import pi

def cono_area(R: float, g: float) -> float:
    """Method to obtain cone area"""
    return pi * R * (g + R)

def cono_volumen(R: float, h: float) -> float:
    """Method to obtain the cone volume"""
    return 1 / 3 * pi * R ** 2 * h
