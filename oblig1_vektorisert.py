import numpy as np
import matplotlib.pyplot as plt

x = np.arange(72)
qx = (np.loadtxt(
        'https://www.uio.no/studier/emner/matnat/math/STK1100/v20/dodssannsynlighet-felles.txt', 
        skiprows=1, 
        delimiter='\t', 
        unpack=False)
    )[35:,-1] / 1000

Fx = 1 - np.cumprod(1-qx)

temp = np.zeros(len(Fx))
temp[1:] = Fx[:-1]
px = Fx - temp

Ex_h = np.sum(np.where(
            x > 31, 
            (1e5/1.03**32)*((1-(1/1.03)**(x-31))/(1-(1/1.03))), 
            0) * px
        )

Ex_g = np.sum(np.where(
            x < 31, 
            (1-(1/1.03)**(x+1))/(1-(1/1.03)), 
            (1-(1/1.03)**(32))/(1-(1/1.03))
            ) * px
        )

K = Ex_h / Ex_g

plt.bar(x, px, width=1, edgecolor='black')
plt.xlabel('Gjentående levetid')
plt.ylabel('Punktsannsynlighet')
plt.savefig('punktsannsynlighet.pdf')

print(f'Forventet nåverdi av pensjonsutbetalinger E[h(X)]: {Ex_h:.0f} kr.')
print(f'E[g(X)]: {Ex_g:.2f}.')
print(f'Årlig premie K: {K:.0f} kr.')