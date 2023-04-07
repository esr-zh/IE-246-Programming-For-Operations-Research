'''

IE 246 Homework - 1 Question - 1 Solutions by Esrah Zahid (S020289)

'''

################ QUESTION 1 a ################

f = {1: 5, 2: 1, 3: 4, 4: 2, 5: 3}
g = {1: 3, 2: 1, 3: 5, 4: 2, 5: 4}
h = {1: 2, 2: 1, 3: 5, 4: 3, 5: 4}


fgh = {1:f[g[h[1]]], 2:f[g[h[2]]], 3:f[g[h[3]]], 4:f[g[h[4]]], 5:f[g[h[5]]]}

print(f'Answer to 1a) fgh = {fgh}')

################ QUESTION 1 b ################

f = {1: 5, 2: 3, 3: 1, 4: 2, 5: 4}
g = {1: 4, 2: 1, 3: 5, 4: 3, 5: 2}
fgh = {1: 5, 2: 3, 3: 1, 4: 4, 5: 2}

f_inverse = dict(zip(f.values(), f.keys()))
g_inverse = dict(zip(g.values(), g.keys()))

h = {1:g_inverse[f_inverse[fgh[1]]], 2:g_inverse[f_inverse[fgh[2]]], 3:g_inverse[f_inverse[fgh[3]]], 4:g_inverse[f_inverse[fgh[4]]], 5:g_inverse[f_inverse[fgh[5]]]}

print(f'Answer to 1b) h = {h}')

################ QUESTION 1 c ################

f = {1: 4, 2: 5, 3: 1, 4: 2, 5: 3}
h = {1: 3, 2: 1, 3: 4, 4: 5, 5: 2}
fgh = {1: 1, 2: 3, 3: 5, 4: 4, 5: 2}

f_inverse = dict(zip(f.values(), f.keys()))
h_inverse = dict(zip(g.values(), g.keys()))

g = {h[1]:f_inverse[fgh[1]], h[2]:f_inverse[fgh[2]], h[3]:f_inverse[fgh[3]], h[4]:f_inverse[fgh[4]], h[5]:f_inverse[fgh[5]]}  
g_sorted = dict(sorted(g.items()))

print(f'Answer to 1c) g = {g_sorted}')
