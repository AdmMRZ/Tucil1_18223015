import util
import os
iter = 0
res = None

def permutate(qpos, idx, cb, count):
    global iter, res
    if idx== len(qpos):
        iter+= 1
        n = len(cb)
        if count > 0 and iter% count == 0:
            util.printboard(cb, qpos)
            print(f"Iterasi: {iter}")
        if valid(cb, qpos):
            res = qpos.copy()
            return True
        return False
    for i in range(idx, len(qpos)):
        qpos[idx],qpos[i] = qpos[i], qpos[idx]
        if permutate(qpos, idx+ 1, cb, count):
            return True
        qpos[idx],qpos[i] = qpos[i],qpos[idx]
    return False

def getsolution(cb, qpos, count=0):
    global iter, res
    iter,res =0,None
    permutate(qpos, 0, cb, count)
    return res, iter

def valid(cb, qpos):
    area = set()
    for i in range(len(qpos)):
        c = qpos[i]
        temp = cb[i][c]
        if temp in area:
            return False
        area.add(temp)
    for i in range(1,len(qpos)):
        c = qpos[i]
        prev = qpos[i- 1]
        if abs(c -prev)<= 1:
            return False
    return True
