def OR(x1, x2):
    w1, w2,threshold = 0.5, 0.5, 0.5
    y = (x1 * w1) + (x2 * w2)
    out = 1 if y >= threshold else 0
    print("OR gate for ", x1, ",", x2, "OUT:", out)
    return out