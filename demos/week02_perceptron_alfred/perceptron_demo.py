# -*- coding:utf8 -*-

def gate_and( x1, x2):
    w1, w2,threshold = 0.5, 0.5, 1
    y = (x1 * w1) + (x2 * w2)
    out = 1 if y >= threshold else 0
    print("AND gate for ", x1, "," , x2, "OUT:", out)
    return out

def gate_or(x1, x2):
    w1, w2,threshold = 0.5, 0.5, 0.5
    y = (x1 * w1) + (x2 * w2)
    out = 1 if y >= threshold else 0
    print("OR gate for ", x1, ",", x2, "OUT:", out)
    return out

def gate_nand(x1, x2):
    w1, w2,threshold = 0.5, 0.5, 1
    y = (x1 * w1) + (x2 * w2)
    out = 1 if y < threshold else 0
    print("NAND gate for ", x1, ",", x2, "OUT:", out)
    return out

def gate_xor(x1, x2):
    y = gate_and(gate_or(x1, x2), gate_nand(x1, x2))
    print("XOR gate for ", x1, ",", x2, "OUT:", y)
    return y

# print(gate_and(1,1))
# print(gate_or(1,0))
# print(gate_nand(0,0))
# print(gate_nand(1,0))
# print(gate_nand(0,1))
# print(gate_nand(1,1))

for xs in [(0,0), (1,0),(0,1), (1,1)]:
    y = gate_xor(xs[0], xs[1])
    print(xs, "->", y)