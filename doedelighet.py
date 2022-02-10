import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

doed = pd.read_csv('https://www.uio.no/studier/emner/matnat/math/STK1100/v20/doedelighet.txt',sep='\t')
alder = doed['alder'].values
menn = doed['menn'].values
kvinner = doed['kvinner'].values

# 1a.
qx_menn = menn/1000
qx_kvinner = kvinner/1000

plt.semilogy(alder, qx_menn, alder, qx_kvinner)
plt.legend(['Menn', 'Kvinner'])
plt.xlabel('Alder')
plt.ylabel('Dødssannsynlighet qx')
plt.title('Ettårige dødssannsynligheter for menn og kvinner')
plt.show()

# 1b.
Sx_menn = np.cumprod(1-qx_menn)
Sx_kvinner = np.cumprod(1-qx_kvinner)

Fx_menn = 1 - Sx_menn
Fx_kvinner = 1 - Sx_kvinner

plt.step(alder, Fx_menn, alder, Fx_kvinner, where='post')
plt.legend(['Menn', 'Kvinner'])
plt.xlabel('Alder')
plt.ylabel('F(x)')
plt.title('Kumulatid fordelingsfunsjon for levealder')
plt.show()

# 1c.
for age in (60, 70, 80, 90):
    # Fx er kumulativ fordelingsfunksjon for dødelighet
    print(f'Sannsynligheten for at en mann blir minst {age} år er {1-Fx_menn[age]:.3f}')
    print(f'Sannsynligheten for at en kvinne blir minst {age} år er {1-Fx_kvinner[age]:.3f}')

# 2a.
for age in alder:
    if Fx_menn[age] >= 0.50:
        mu_x = age
        break

for age in alder:
    if Fx_kvinner[age] >= 0.50:
        mu_y = age
        break

print(f'Medianalder menn: {mu_x} \nMedianalder kvinner: {mu_y}')

# 2b.
tmp = Fx_menn.copy()
tmp[1:-1] = tmp[0:-2]
tmp[0] = 0
px_menn = Fx_menn - tmp

plt.bar(alder, px_menn, width=1, edgecolor='blue', fill=False, linewidth=.9)
plt.legend(['Menn'])
plt.xlabel('Alder')
plt.ylabel('p(x)') 
plt.title('Punktsannsynlighet menn')
plt.show()

tmp = Fx_kvinner.copy()
tmp[1:-1] = tmp[0:-2]
tmp[0] = 0
px_kvinner = Fx_kvinner - tmp

plt.bar(alder, px_kvinner, width=1, edgecolor='red', fill=False, linewidth=.9)
plt.legend(['Kvinner'])
plt.xlabel('Alder')
plt.ylabel('p(x)') 
plt.title('Punktsannsynlighet kvinner')
plt.show()

# 2c.
ex_menn = np.sum(alder*px_menn)
ex_kvinner = np.sum(alder*px_kvinner)

print(f'Forventet levealder menn: {ex_menn:.2f} \nForventet levealder kvinne: {ex_kvinner:.2f}')
