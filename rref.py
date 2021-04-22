import numpy as np

def rref(m, p):
    pivots = []
    ir = 0
    for ic in range(m.shape[1]):
        if ir >= m.shape[0]:
            return m, pivots
        if m[ir,ic] == 0:
            j = -1
            for x in range(ir+1, m.shape[0]):
                if m[x,ic] != 0:
                    j = x
                    break
            if j > 0:
                m[ir], m[j] = m[j], m[ir]
            if j == -1:
                continue
        a = pow(int(m[ir, ic]), p-2, p)
        m[ir] = a*m[ir]%p
        pivots.append((ir, ic))
        assert m[ir, ic] == 1
        col = m[:,ic]
        for i, x in enumerate(col):
            if i == ir or x == 0:
                continue
            m[i] = (m[i]- m[i,ic]*m[ir]) % p
        ir += 1
    return m, pivots

def nullspace(m, p):
    m, pivots = rref(m, p)
    pivot_d = {}
    for k,v in pivots:
        pivot_d[k] = v
    pivot_c = set(pivot_d.values())
    
    r = []
    for ic in range(m.shape[1]):
        if ic in pivot_c:
            continue
        print('c', ic, m[:,ic])
        v = np.zeros((m.shape[1], 1), dtype=m.dtype)
        v[ic, 0] = 1
        for ir, x in enumerate(m[:,ic]):
            if x == 0:
                continue
            v[pivot_d[ir], 0] = -x
        r.append(v)
    return r
