import math as m
import matplotlib.pyplot as plt
import matplotlib.patches as p
from matplotlib.colors import Normalize

#berechnung der l function mit chi_1 mod 5
def L_unger():
    return m.pi/10*(m.tan(m.pi/5)**(-1)+complex(0,1)*m.tan(2*m.pi/5)**(-1)-complex(0,1)*m.tan(3*m.pi/5)**(-1)-m.tan(4*m.pi/5)**(-1))
#berechnung des anderen charakters
def L_chi2():
    return 2/m.sqrt(5)*m.log((1+m.sqrt(5))/2)
#einfach für latex auflösung im DIagramm
def L1(limit):
    chi = 0
    liste = list()
    for i in range(4):
        liste.append(list())
    
    for n in range(1,limit):
        match n%5:
            case 1:
                chi=1
                liste[0].append(chi/n)
            case 2:
                chi = complex(0,1)
                liste[1].append(chi/n)
            case 3:
                chi = complex(0,-1)
                liste[2].append(chi/n)
            case 4:
                chi = -1
                liste[3].append(chi/n)
    return liste


def L2(limit):
    chi = 0
    liste = list()
    for i in range(4):
        liste.append(list())
    
    for n in range(1,limit):
        match n%5:
            case 1:
                chi=1
                liste[0].append(chi/n)
            case 2:
                chi = -1
                liste[1].append(chi/n)
            case 3:
                chi = -1
                liste[2].append(chi/n)
            case 4:
                chi = 1
                liste[3].append(chi/n)
    return liste

def L3(limit):
    chi = 0
    liste = list()
    for i in range(4):
        liste.append(list())
    
    for n in range(1,limit):
        match n%5:
            case 1:
                chi=1
                liste[0].append(chi/n)
            case 2:
                chi = complex(0,-1)
                liste[1].append(chi/n)
            case 3:
                chi = complex(0,1)
                liste[2].append(chi/n)
            case 4:
                chi = 1
                liste[3].append(chi/n)
    return liste
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})
WerteL1 = L1(10000)
WerteL2 = L2(10000)
WerteL3 = L3(10000)
figur, axis = plt.subplots(2,2,sharex=True, sharey=True)
l = [[1,0.2],[0.2,1],[0.2,-1],[-1,0.2],'1 mod 5','2 mod 5','3 mod 5','4 mod 5']
l2 = [[1,0.2],[-1,0.2],[-1,-0.2],[1,-0.2],'1 mod 5','2 mod 5','3 mod 5','4 mod 5']
l3 = [[1,0.2],[0.2,-1],[0.2,1],[1,-0.2],'1 mod 5','2 mod 5','3 mod 5','4 mod 5']
skala = Normalize(vmin=0, vmax=2000, clip=True)
farbkarte = plt.get_cmap("viridis")
axis[0, 0].set(xlim=(-2.5, 2.5), ylim=(-2.5, 2.5))
for i in range(4):
    axis[0,0].text(l[i][0], l[i][1], f'({l[4+i]})', fontsize=8)
    axis[0,0].set_title(r'$L(1,\chi_1)$')
for i in range(4):
    axis[1,0].text(l2[i][0], l2[i][1], f'({l2[4+i]})', fontsize=8)
    axis[1,0].set_title(r'$L(1,\chi_2)$')

for i in range(4):
    axis[0,1].text(l3[i][0], l3[i][1], f'({l3[4+i]})', fontsize=8)
    axis[0,1].set_title(r'$L(1,\chi_3)$')

for i in range(4):
    for j in range(len(WerteL1[i])):
        X = WerteL1[i][j].real
        Y= WerteL1[i][j].imag
        axis[0,0].plot(sum(WerteL1[i][:j]).real,sum(WerteL1[i][:j]).imag,'o', color=farbkarte(skala(j)))
        axis[0,0].grid()
for i in range(4):
    for j in range(len(WerteL2[i])):
        X = WerteL2[i][j].real
        Y= WerteL2[i][j].imag
        axis[1,0].plot(sum(WerteL2[i][:j]).real,sum(WerteL2[i][:j]).imag,'o', color=farbkarte(skala(j)))
        axis[1,0].grid()
for i in range(4):
    for j in range(len(WerteL3[i])):
        X = WerteL3[i][j].real
        Y= WerteL3[i][j].imag
        axis[0,1].plot(sum(WerteL3[i][:j]).real,sum(WerteL3[i][:j]).imag,'o', color=farbkarte(skala(j)))
        axis[0,1].grid()

plt.show()
'''
x=L_unger().real
y=L_unger().imag
fig = plt.figure()
ax = fig.add_subplot(111)
charakter1 = plt.plot(x,y, 'o')
charakter3 = plt.plot(x,-y, 'o')
charakter2 = plt.plot(L_chi2(),0,'o')
circ = p.Circle((0,0),1)
ax.add_patch(circ)
ax.text(x, y, r'L(1,$\chi_1$)', fontsize=8)
ax.text(x, -y, r'L(1,$\chi_3$)', fontsize=8)
plt.grid()
'''

