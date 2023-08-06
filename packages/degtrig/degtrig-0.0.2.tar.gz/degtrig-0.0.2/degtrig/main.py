
import math
pi = math.pi

def sin(deg: float) -> float:
    return math.sin(deg * math.pi / 180)

def cos(deg: float) -> float:
    return math.cos(deg * math.pi / 180)

def tan(deg: float) -> float:
    return math.tan(deg * math.pi / 180)

def asin(ratio: float) -> float:
    return math.degrees(math.asin(ratio))

def acos(ratio: float) -> float:
    return math.degrees(math.acos(ratio))

def atan(ratio: float) -> float:
    return math.degrees(math.atan(ratio))

def sinh(deg: float) -> float:
    return math.sinh(deg)

def cosh(deg: float) -> float:
    return math.cosh(deg)

def tanh(deg: float) -> float:
    return math.tanh(deg)

def asinh(ratio: float) -> float:
    return math.asinh(ratio)

def acosh(ratio: float) -> float:
    return math.acosh(ratio)

def atanh(ratio: float) -> float:
    return math.atanh(ratio)

def cot(deg: float) -> float:
    return 1 / tan(deg)

def sec(deg: float) -> float:
    return 1 / cos(deg)

def cosec(deg: float) -> float:
    return 1 / sin(deg)