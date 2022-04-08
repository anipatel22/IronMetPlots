import matplotlib.pyplot as plt

# Sirjan
Ni = 82000
Ge = 53.328
Ga = 24.722
# Ir = 2.981
# Re = 0.272
# Ru = 5.365
Rh = 1.019
# Pd = 4.075
# Pt = 8.385
Au = 1.483
# Os = 3.01
W = 0.906
Co = 2000
Cr = 0
Cu = 0
As = 9.167
Mo = 0
Fe = 0
P = 0
Zn = 0

# Isotope Dilution HSE
Re = 0.189
Os = 1.423
Ir = 2.019
Ru = 5.223
Pt = 7.055
Pd = 4.079

Sirj = [Os, Re, W, Ir, Ru, Mo, Pt, Rh, Ni, Co, Fe, Pd, Cr, P, As, Cu, Ga, Au, Ge]
# Nedagolla
Ni2 = 61000
Ge2 = .005
Ga2 = 0.765
Ir2 = 4.474
Re2 = 0.424
Ru2 = 5.798
Rh2 = 0.944
Pd2 = 1.753
Pt2 = 7.952
Au2 = 0.22
Os2 = 5.827
W2 = 0.594
Co2 = 3600
Cr2 = 2600
Cu2 = 1.5
Mo2 = 2.455
Fe2 = 935000
P2 = 2000
As2 = 0
Zn2 = 3

# elem = ['Os', 'Re', 'W', 'Ir', 'Ru', 'Mo', 'Pt', 'Rh', 'Ni', 'Co', 'Fe', 'Pd', 'Cr', 'P', 'As', 'Cu', 'Ga', 'Au', 'Ge']
# Sirj = [Os, Re, W, Ir, Ru, Mo, Pt, Rh, Ni, Co, Fe, Pd, Cr, P, As, Cu, Ga, Au, Ge]
# Ned = [Os2, Re2, W2, Ir2, Ru2, Mo2, Pt2, Rh2, Ni2, Co2, Fe2, Pd2, Cr2, P2, As2, Cu2, Ga2, Au2, Ge2]
# IAB = [1.715169082, 0.215530785, 0.9808571429, 2.197632647,	4.122054521,	0,	6,	0,	91899.13545,	4936.423358,	0,	4.862041096,	76.0295203,	0,	15.96043956,	239.5128205,	65.54201465,	1.654332117,	271.714876]
# IIIAB = [2.888531668,	0.2690842129,	0.695,	3.275882759,	8.7574,	0,	8.566418182,	0,	87002.12766,	5275.416667,	0,	3.1512,	56.33333333,	0,	11.25333333,	154.25,	19.23333333,	1.339083333,	37.19130435]
# IIIF = [6.091886505,	0.496171148,	1.578333333,	4.93688916,	6.845047619,	8.441,	8.8606,	1.354,	75666.66667,	3870,	91.78,	3.543529412,	192.7333333,	2654,	5.835555556,	125.2777778,	10.67388889,	0.8798333333,	23.77011111]
# IVA = [1.592107033,	0.2054651932,	0.5339310345,	1.824164205,	3.006233333,	0,	5.185467066,	0,	85293.75,	3982.945205,	0,	5.604166667,	182.5616438,	0,	7.038482759,	137.8896552,	2.135241379,	1.451150685, 0.6013521127]
# Orgueil = [0.495,	0.04,	0.096,	0.469,	0.69,	0.961,	0.925,	0.132,	10910,	513,	186600,	0.56,	2623,	985,	1.74,	133,	9.62,	0.148,	32.6,	309]

# without Mo, Fe, Cr, P, Cu
elem = ['Os', 'Re', 'W', 'Ir', 'Ru', 'Pt', 'Rh', 'Ni', 'Co', 'Pd', 'As', 'Ga', 'Au', 'Ge']
Sirj = [Os, Re, W, Ir, Ru, Pt, Rh, Ni, Co, Pd, As, Ga, Au, Ge]
Ned = [Os2, Re2, W2, Ir2, Ru2, Pt2, Rh2, Ni2, Co2, Pd2, As2, Ga2, Au2, Ge2]
IAB = [1.715169082, 0.215530785, 0.9808571429, 2.197632647,	4.122054521, 6,	0,	91899.13545,	4936.423358,	4.862041096,	15.96043956,	65.54201465,	1.654332117,	271.714876]
IIIAB = [2.888531668,	0.2690842129,	0.695,	3.275882759,	8.7574,	8.566418182,	0,	87002.12766,	5275.416667,	3.1512,	11.25333333,	19.23333333,	1.339083333,	37.19130435]
IIIF = [6.091886505,	0.496171148,	1.578333333,	4.93688916,	6.845047619,	8.8606,	1.354,	75666.66667,	3870,	3.543529412,	5.835555556,	10.67388889,	0.8798333333,	23.77011111]
IVA = [1.592107033,	0.2054651932,	0.5339310345,	1.824164205,	3.006233333,	5.185467066,	0,	85293.75,	3982.945205,	5.604166667,	7.038482759,	2.135241379,	1.451150685, 0.6013521127]
Orgueil = [0.495,	0.04,	0.096,	0.469,	0.69,	0.925,	0.132,	10910,	513,	0.56,	1.74,	9.62,	0.148,	32.6,	309]

SirjN = [i / j for i, j in zip(Sirj, Orgueil)]
NedN = [i / j for i, j in zip(Ned, Orgueil)]
IABN = [i / j for i, j in zip(IAB, Orgueil)]
IIIABN = [i / j for i, j in zip(IIIAB, Orgueil)]
IIIFN = [i / j for i, j in zip(IIIF, Orgueil)]
IVAN = [i / j for i, j in zip(IVA, Orgueil)]

for i in range(len(SirjN)):
    if SirjN[i] == 0.0: SirjN[i] = None


for i in range(len(NedN)):
    if NedN[i] == 0.0:
        NedN[i] = None

for i in range(len(IABN)):
    if IABN[i] == 0.0:
        IABN[i] = None

for i in range(len(IIIABN)):
    if IIIABN[i] == 0.0:
        IIIABN[i] = None

for i in range(len(IIIFN)):
    if IIIFN[i] == 0.0:
        IIIFN[i] = None

for i in range(len(IVAN)):
    if IVAN[i] == 0.0:
        IVAN[i] = None

plt.rc('axes', labelsize=15)
plt.rc('xtick', labelsize= 15)
plt.rc('ytick', labelsize= 13)
plt.rc('legend', fontsize= 13)

fig = plt.figure(figsize=(6,5))
plt.style.use('classic')
ax = fig.add_subplot()

# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.set_title('') 
ax.set_ylabel('Normalized to Orgueil (CI)')


ax.plot(elem, NedN, color = 'green', marker = 'D', lw = 0.8, alpha =0.8, markeredgewidth = 1., markeredgecolor = 'black', label = 'Nedagolla (UG)')
ax.plot(elem, IABN, color = 'b', marker = 'o', lw = 0.8, alpha =0.8, markeredgewidth = 1., markeredgecolor = 'black', label = 'IAB')
ax.plot(elem, IIIABN, color = 'y', marker = 'v', lw = 0.8, alpha =0.8, markeredgewidth = 1., markeredgecolor = 'black', label = 'IIIAB')
# ax.plot(elem, IIIFN, color = 'peru', marker = 'v', lw = 0.8, alpha =0.8, markeredgewidth = 1., markeredgecolor = 'black', label = 'IIIF')
ax.plot(elem, IVAN, color = 'aquamarine', marker = 's', lw = 0.8, alpha =0.8, markeredgewidth = 1., markeredgecolor = 'black', label = 'IVA')
ax.plot(elem, SirjN, color = 'darkorange', marker = '^', lw = 0.8, markersize = 10, markeredgewidth = 1., markeredgecolor = 'black', label = 'Sirjan')
ax.legend(numpoints = 1, loc = 'best',fontsize = 10, markerscale =0.8, frameon=False)

plt.savefig("spider.pdf",format='pdf')
plt.show()
