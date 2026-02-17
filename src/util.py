def printboard(cb, qpos):
    lines = []
    for i in range(len(cb)):
        line = ""
        for c in range(len(cb[i])):
            if qpos[i] == c:
                line+= "#"
            else:
                line+= cb[i][c]
        print(line)
        lines.append(line)
    return lines