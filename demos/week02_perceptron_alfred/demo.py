from gate_xor import XOR
for xs in [(0,0), (1,0),(0,1), (1,1)]:
    y = XOR(xs[0], xs[1])
    print("==================================", xs, "->", y)
