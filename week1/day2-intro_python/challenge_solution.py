for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        if ((a + (b - c) * d - e) * f == 75) & \
                           (len(set([a, b, c, d, e, f])) == 6):
                           print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")
