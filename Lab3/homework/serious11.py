def is_inside(l1,l2):
    x1 = l1[0]
    y1 = l1[1]
    x2 = l2[0]
    y2 = l2[1]
    x2w = l2[0] + l2[2]
    y2h = l2[1] + l2[3]
    if (x2 <= x1 <= x2w) and (y2 <= y1 <= y2h):
        inside = True
    else:
        inside = False
    return (inside)