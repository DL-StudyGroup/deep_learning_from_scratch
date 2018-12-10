from gate_and import AND
from gate_or import OR
from gate_nand import NAND
def XOR(x1, x2):
    y = AND(OR(x1, x2), NAND(x1, x2))
    print("XOR gate for ", x1, ",", x2, "OUT:", y)
    return y
