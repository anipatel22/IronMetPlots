import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np    
from pylab import cm
from matplotlib import rcParams
import pandas as pd
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


# READING IN DATA FROM EXCEL FILE AND STORING IT IN PYTHON LISTS
xls = pd.ExcelFile('IronMeteoriteData.xlsx')

dfIAB = pd.read_excel(xls,'IAB')
NiIab = dfIAB['Ni (%)']
GeIab = dfIAB['Ge']
GaIab = dfIAB['Ga']
IrIab = dfIAB['Ir']
ReIab = dfIAB['Re']
RuIab = dfIAB['Ru']
RhIab = dfIAB['Rh']
PdIab = dfIAB['Pd']
PtIab = dfIAB['Pt']
AuIab = dfIAB['Au']
OsIab = dfIAB['Os']
WIab = dfIAB['W']
CoIab = dfIAB['Co (mg/g)']
CrIab = dfIAB['Cr']
CuIab = dfIAB['Cu']
SbIab = dfIAB['Sb (ng/g)']
AsIab = dfIAB['As']
# SIab = dfIAB['S (mg/g)']
# MoIab = dfIAB['Mo']
# PIab = dfIAB['P']
# VIab = dfIAB['V']

dfIC = pd.read_excel(xls,'IC')
NiIc = dfIC['Ni (%)']
GeIc = dfIC['Ge']
GaIc = dfIC['Ga']
IrIc = dfIC['Ir']
ReIc = dfIC['Re']
RuIc = dfIC['Ru']
RhIc = dfIC['Rh']
PdIc = dfIC['Pd']
PtIc = dfIC['Pt']
AuIc = dfIC['Au']
OsIc = dfIC['Os']
WIc = dfIC['W']
CoIc = dfIC['Co (mg/g)']
CrIc = dfIC['Cr']
CuIc = dfIC['Cu']
SbIc = dfIC['Sb (ng/g)']
AsIc = dfIC['As']
# SIc = dfIC['S (mg/g) modeled']
# MoIc = dfIC['Mo']
# PIc = dfIC['P (mg/g) modeled']
# VIc = dfIC['V']

dfIIAB = pd.read_excel(xls,'IIAB')
NiIIab = dfIIAB['Ni (%)']
GeIIab = dfIIAB['Ge']
GaIIab = dfIIAB['Ga']
IrIIab = dfIIAB['Ir']
ReIIab = dfIIAB['Re']
RuIIab = dfIIAB['Ru']
RhIIab = dfIIAB['Rh']
PdIIab = dfIIAB['Pd']
PtIIab = dfIIAB['Pt']
AuIIab = dfIIAB['Au']
OsIIab = dfIIAB['Os']
WIIab = dfIIAB['W']
CoIIab = dfIIAB['Co (mg/g)']
CrIIab = dfIIAB['Cr']
CuIIab = dfIIAB['Cu']
SbIIab = dfIIAB['Sb (ng/g)']
AsIIab = dfIIAB['As']
SIIab = dfIIAB['S (mg/g)']
# MoIIab = dfIIAB['Mo']
PIIab = dfIIAB['P (mg/g)']
# VIIab = dfIIAB['V']

dfIIC = pd.read_excel(xls,'IIC')
NiIIc = dfIIC['Ni (%)']
GeIIc = dfIIC['Ge']
GaIIc = dfIIC['Ga']
IrIIc = dfIIC['Ir']
ReIIc = dfIIC['Re']
RuIIc = dfIIC['Ru']
RhIIc = dfIIC['Rh']
PdIIc = dfIIC['Pd']
PtIIc = dfIIC['Pt']
AuIIc = dfIIC['Au']
OsIIc = dfIIC['Os']
WIIc = dfIIC['W']
CoIIc = dfIIC['Co (mg/g)']
CrIIc = dfIIC['Cr']
CuIIc = dfIIC['Cu']
SbIIc = dfIIC['Sb (ng/g)']
AsIIc = dfIIC['As']
# SIIc = dfIIC['S (mg/g) modeled']
# MoIIc = dfIIC['Mo']
# PIIc = dfIIC['P (mg/g) modeled']
# VIIc = dfIIC['V']

dfIID = pd.read_excel(xls,'IID')
NiIId = dfIID['Ni (%)']
GeIId = dfIID['Ge']
GaIId = dfIID['Ga']
IrIId = dfIID['Ir']
ReIId = dfIID['Re']
RuIId = dfIID['Ru']
RhIId = dfIID['Rh']
PdIId = dfIID['Pd']
PtIId = dfIID['Pt']
AuIId = dfIID['Au']
OsIId = dfIID['Os']
WIId = dfIID['W']
CoIId = dfIID['Co (mg/g)']
CrIId = dfIID['Cr']
CuIId = dfIID['Cu']
SbIId = dfIID['Sb (ng/g)']
AsIId = dfIID['As']
# SIId = dfIID['S (mg/g) modeled']
# MoIId = dfIID['Mo']
# PIId = dfIID['P (mg/g) modeled']
# VIId = dfIID['V']

dfIIE = pd.read_excel(xls,'IIE')
NiIIe = dfIIE['Ni (%)']
GeIIe = dfIIE['Ge']
GaIIe = dfIIE['Ga']
IrIIe = dfIIE['Ir']
ReIIe = dfIIE['Re']
RuIIe = dfIIE['Ru']
RhIIe = dfIIE['Rh']
PdIIe = dfIIE['Pd']
PtIIe = dfIIE['Pt']
AuIIe = dfIIE['Au']
OsIIe = dfIIE['Os']
WIIe = dfIIE['W']
CoIIe = dfIIE['Co (mg/g)']
CrIIe = dfIIE['Cr']
CuIIe = dfIIE['Cu']
SbIIe = dfIIE['Sb (ng/g)']
AsIIe = dfIIE['As']
# SIIe = dfIIE['S (mg/g) modeled']
# MoIIe = dfIIE['Mo']
# PIIe = dfIIE['P (mg/g) modeled']
# VIIe = dfIIE['V']

dfIIF = pd.read_excel(xls,'IIF')
NiIIf = dfIIF['Ni (%)']
GeIIf = dfIIF['Ge']
GaIIf = dfIIF['Ga']
IrIIf = dfIIF['Ir']
ReIIf = dfIIF['Re']
RuIIf = dfIIF['Ru']
RhIIf = dfIIF['Rh']
PdIIf= dfIIF['Pd']
PtIIf = dfIIF['Pt']
AuIIf = dfIIF['Au']
OsIIf = dfIIF['Os']
WIIf = dfIIF['W']
CoIIf = dfIIF['Co (mg/g)']
CrIIf = dfIIF['Cr']
CuIIf = dfIIF['Cu']
SbIIf = dfIIF['Sb (ng/g)']
AsIIf = dfIIF['As']
# SIIf = dfIIF['S (mg/g) modeled']
# MoIIf = dfIIF['Mo']
# PIIf = dfIIF['P (mg/g) modeled']
# VIIf = dfIIF['V']

dfIIG = pd.read_excel(xls,'IIG')
NiIIg = dfIIG['Ni (%)']
GeIIg = dfIIG['Ge']
GaIIg = dfIIG['Ga']
IrIIg = dfIIG['Ir']
ReIIg = dfIIG['Re']
RuIIg = dfIIG['Ru']
RhIIg = dfIIG['Rh']
PdIIg = dfIIG['Pd']
PtIIg = dfIIG['Pt']
AuIIg = dfIIG['Au']
OsIIg = dfIIG['Os']
WIIg = dfIIG['W']
CoIIg = dfIIG['Co (mg/g)']
CrIIg = dfIIG['Cr']
CuIIg = dfIIG['Cu']
SbIIg = dfIIG['Sb (ng/g)']
AsIIg = dfIIG['As']
SIIg = dfIIG['S (mg/g)']
MoIIg = dfIIG['Mo']
PIIg = dfIIG['P (mg/g)']
VIIg = dfIIG['V']

dfIIIAB = pd.read_excel(xls,'IIIAB')
NiIIIab = dfIIIAB['Ni (%)']
GeIIIab = dfIIIAB['Ge']
GaIIIab = dfIIIAB['Ga']
IrIIIab = dfIIIAB['Ir']
ReIIIab = dfIIIAB['Re']
RuIIIab = dfIIIAB['Ru']
RhIIIab = dfIIIAB['Rh']
PdIIIab = dfIIIAB['Pd']
PtIIIab = dfIIIAB['Pt']
AuIIIab = dfIIIAB['Au']
OsIIIab = dfIIIAB['Os']
WIIIab = dfIIIAB['W']
CoIIIab = dfIIIAB['Co (mg/g)']
CrIIIab = dfIIIAB['Cr']
CuIIIab = dfIIIAB['Cu']
SbIIIab = dfIIIAB['Sb (ng/g)']
AsIIIab = dfIIIAB['As']
# SIIIab = dfIIIAB['S (mg/g)']
# MoIIIab = dfIIIAB['Mo']
# PIIIab = dfIIIAB['P']
# VIIIab = dfIIIAB['V']

dfIIIE = pd.read_excel(xls,'IIIE')
NiIIIe = dfIIIE['Ni (%)']
GeIIIe = dfIIIE['Ge']
GaIIIe = dfIIIE['Ga']
IrIIIe = dfIIIE['Ir']
ReIIIe = dfIIIE['Re']
RuIIIe = dfIIIE['Ru']
RhIIIe = dfIIIE['Rh']
PdIIIe = dfIIIE['Pd']
PtIIIe = dfIIIE['Pt']
AuIIIe = dfIIIE['Au']
OsIIIe = dfIIIE['Os']
WIIIe = dfIIIE['W']
CoIIIe = dfIIIE['Co (mg/g)']
CrIIIe = dfIIIE['Cr']
CuIIIe = dfIIIE['Cu']
SbIIIe = dfIIIE['Sb (ng/g)']
AsIIIe = dfIIIE['As']
# SIIIe = dfIIIE['S (mg/g) modeled']
# MoIIIe = dfIIIE['Mo']
# PIIIe = dfIIIE['P (mg/g) modeled']
# VIIIe = dfIIIE['V']

dfIIIF = pd.read_excel(xls,'IIIF')
NiIIIf = dfIIIF['Ni (%)']
GeIIIf = dfIIIF['Ge']
GaIIIf = dfIIIF['Ga']
IrIIIf = dfIIIF['Ir']
ReIIIf = dfIIIF['Re']
RuIIIf = dfIIIF['Ru']
RhIIIf = dfIIIF['Rh']
PdIIIf = dfIIIF['Pd']
PtIIIf = dfIIIF['Pt']
AuIIIf = dfIIIF['Au']
OsIIIf = dfIIIF['Os']
WIIIf = dfIIIF['W']
CoIIIf = dfIIIF['Co (mg/g)']
CrIIIf = dfIIIF['Cr']
CuIIIf = dfIIIF['Cu']
SbIIIf = dfIIIF['Sb (ng/g)']
AsIIIf = dfIIIF['As']
# SIIIf = dfIIIF['S (mg/g) modeled']
# MoIIIf = dfIIIF['Mo']
# PIIIf = dfIIIF['P (mg/g) modeled']
# VIIIf = dfIIIF['V']

dfIVA = pd.read_excel(xls,'IVA')
NiIVa = dfIVA['Ni (%)']
GeIVa = dfIVA['Ge']
GaIVa = dfIVA['Ga']
IrIVa = dfIVA['Ir']
ReIVa = dfIVA['Re']
RuIVa = dfIVA['Ru']
RhIVa = dfIVA['Rh']
PdIVa = dfIVA['Pd']
PtIVa = dfIVA['Pt']
AuIVa = dfIVA['Au']
OsIVa = dfIVA['Os']
WIVa = dfIVA['W']
CoIVa = dfIVA['Co (mg/g)']
CrIVa = dfIVA['Cr']
CuIVa = dfIVA['Cu']
SbIVa = dfIVA['Sb (ng/g)']
AsIVa = dfIVA['As']
# SIVa = dfIVA['S (mg/g)']
# MoIVa = dfIVA['Mo']
# PIVa = dfIVA['P']
# VIVa = dfIVA['V']

dfIVB = pd.read_excel(xls,'IVB')
NiIVb = dfIVB['Ni (%)']
GeIVb = dfIVB['Ge']
GaIVb = dfIVB['Ga']
IrIVb = dfIVB['Ir']
ReIVb = dfIVB['Re']
RuIVb = dfIVB['Ru']
RhIVb = dfIVB['Rh']
PdIVb = dfIVB['Pd']
PtIVb = dfIVB['Pt']
AuIVb = dfIVB['Au']
OsIVb = dfIVB['Os']
WIVb = dfIVB['W']
CoIVb = dfIVB['Co (ppm)']
CrIVb = dfIVB['Cr']
CuIVb = dfIVB['Cu']
SbIVb = dfIVB['Sb (ng/g)']
AsIVb = dfIVB['As']
# SIVb = dfIVB['S (mg/g)']
# MoIVb = dfIVB['Mo']
# PIVb = dfIVB['P']
# VIVb = dfIVB['V']

dfUNGR = pd.read_excel(xls,'ungrouped')
NiUg = dfUNGR['Ni (%)']
GeUg = dfUNGR['Ge']
GaUg = dfUNGR['Ga']
IrUg = dfUNGR['Ir']
ReUg = dfUNGR['Re']
RuUg = dfUNGR['Ru']
RhUg = dfUNGR['Rh']
PdUg = dfUNGR['Pd']
PtUg = dfUNGR['Pt']
AuUg = dfUNGR['Au']
OsUg = dfUNGR['Os']
WUg = dfUNGR['W']
CoUg = dfUNGR['Co (mg/g)']
CrUg = dfUNGR['Cr']
CuUg = dfUNGR['Cu']
SbUg = dfUNGR['Sb (ng/g)']
AsUg = dfUNGR['As']
# SUg = dfUNGR['S (mg/g)']
# MoUg = dfUNGR['Mo']
# PUg = dfUNGR['P']
# VUg = dfUNGR['V']


# Data for meteorites of interest

# Sirjan
# Ni = 5.55
# Ge = 181
# Ga = 59
# Ir = 15.2
# Re = 1.2
# Ru = 20.2
# Rh = 2.1
# Pd = 1.4
# Pt = 24.1
# Au = 0.7
# Os = 9.5
# W = 2.9
# Co = 4.642 #in mg/g
# Cr = 23.2
# Cu = 146
# As = 4.3

Ni = 8.2
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
Co = 2 #in mg/g
Cr = 0
Cu = 0
As = 9.167

# Isotope Dilution HSE
Re = 0.189
Os = 1.423
Ir = 2.019
Ru = 5.223
Pt = 7.055
Pd = 4.079

# Nedagolla
Ni2 = 6.1
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
Co2 = 3.6 #in mg/g
Cr2 = 2600
Cu2 = 1.5

# Del Rio
Ni3 = 11.6
Ge3 = 100
Ga3 = 9.4
Ir3 = 19.6
Re3 = 1.6
Ru3 = 19.2
Rh3 = 2.2
Pd3 = 2.7
Pt3 = 24
Au3 = 0.69
Os3 = 21
W3 = 1.2
Co3 = 6.9 #in mg/g
Cu3 = 336
As3 = 4.9
Mo3 = 11.9


# Mont Dieu IIE
Ni4 = 8.258
Ga4 = 25.4
Ge4 = 61
Ir4 = 7.14
Re4 = 0.71
Ru4 = 10.13
Rh4 = 1.44
Pd4 = 3.4
Pt4 = 13.1
Au4 = 0.93
Os4 = 7.62
W4 = 1.22
Co4 = 4.52 #in mg/g
Cr4 = 8
Cu4 = 274
As4 = 10.1


plt.rc('font', family='calibri')
plt.rcParams["figure.figsize"] = [6, 5]
plt.rcParams["figure.autolayout"] = True



# #================================================================================================================
# plt.rc('font', family='calibri')
# plt.rcParams["figure.figsize"] = [6, 5]
# plt.rcParams["figure.autolayout"] = True

# plt.rc('axes', labelsize=15)
plt.rc('xtick', labelsize= 11)
plt.rc('ytick', labelsize= 11)
# plt.rc('legend', fontsize= 13) 

# Au vs Re
# fig = plt.figure(figsize = (6,5))
# plt.style.use('classic')
# ax = plt.axes()
# ax.set_yscale('log')
# ax.set_xscale('log')
# # ax.tick_params(which = 'both', right=True, top=True, axis="y",direction="in")
# # ax.tick_params(which = 'both', right=True, top=True, axis="x",direction="in")
# ax.xaxis.set_minor_formatter(FormatStrFormatter('%0.1f'))
# ax.xaxis.set_minor_locator(plt.AutoLocator())
# # ax.xaxis.set_minor_locator(plt.MaxNLocator(4))
# # ax.yaxis.set_minor_formatter(FormatStrFormatter('%d'))
# # ax.yaxis.set_major_formatter(FormatStrFormatter('%0.001f'))
# ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
# ax.set_aspect('auto')
# ax.plot(AuIab, ReIab, '.', color = 'b', alpha =1., label = 'IAB')
# ax.plot(AuIIab, ReIIab, 'o', color = 'r', alpha =0.6, label = 'IIAB')
# ax.plot(AuIIc, ReIIc, 'o', color = 'c', alpha =0.6, label = 'IIC')
# ax.plot(AuIId, ReIId, 'o', color = 'm', alpha =0.6, label = 'IID')
# ax.plot(AuIIf, ReIIf, 'o', color = 'hotpink', alpha =1., label = 'IIF')
# ax.plot(AuIIIab, ReIIIab, 'v', color = 'olive', alpha =0.6, label = 'IIIAB')
# ax.plot(AuIIIf, ReIIIf, 'v', color = 'peru', alpha =0.6, label = 'IIIF')
# ax.plot(AuIVa,ReIVa, 's', color = 'aquamarine', alpha =1., label = 'IVA')
# ax.plot(AuIVb, ReIVb, 's', color = 'purple', alpha =0.6, label = 'IVB')
# ax.plot(AuUg, ReUg, 'x', color = 'black', label = 'Ungrouped')
# ax.plot(Au, Re, '^', markersize = 14, color = 'darkorange', label = 'Sirjan 001')
# ax.plot(Au2, Re2,'D', markersize = 11, color = 'green', label = 'Nedagolla (UG)')
# # ax.plot(Au3, Re3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# # ax.plot(Au4, Re4,'D', markersize = 11, color = 'yellow', label = 'Mont Dieu (UG)')

# ax.set_xlim(0.2,3.)
# ax.set_ylim(0.01,1.5)
# plt.ylabel('Re (ppm)', fontsize = 14)
# plt.xlabel('Au (ppm)', fontsize = 14)
# plt.title("Iron Meteorite Distribution, Au vs. Re", fontsize = 14)
# ax.legend(numpoints = 1, loc = 'best',fontsize = 10, markerscale = 0.8, prop={'size': 8})

# plt.savefig("Au_Re.pdf",format='pdf')




# #NI VS GE
fig = plt.figure(figsize = (6,5))
plt.style.use('classic')
ax = plt.axes()
ax.set_xscale('log')
ax.set_yscale('log')
ax.tick_params(which = 'both', right=True, top=True, axis="y",direction="in")
ax.tick_params(which = 'both', right=True, top=True, axis="x",direction="in")
# ax.xaxis.set_minor_formatter(FormatStrFormatter('%d'))
# ax.yaxis.set_minor_formatter(FormatStrFormatter('%d'))
# ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
# ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

ax.set_aspect('auto')
ax.plot(NiIab, GeIab,'.', color = 'b', alpha =0.6, label = 'IAB')
ax.plot(NiIc, GeIc,'.', color = 'g', alpha =0.6, label = 'IC')
ax.plot(NiIIab, GeIIab,'o', color = 'r', alpha =0.6, label = 'IIAB')
ax.plot(NiIIc, GeIIc,'o', color = 'c', alpha =0.6, label = 'IIC')
ax.plot(NiIId, GeIId,'o', color = 'm', alpha =0.6, label = 'IID')
ax.plot(NiIIe, GeIIe,'o', color = 'y', alpha =1, label = 'IIE')
ax.plot(NiIIf, GeIIf,'o', color = 'hotpink', alpha =0.6, label = 'IIF')
ax.plot(NiIIg, GeIIg,'o', color = 'pink', alpha =0.6, label = 'IIG')
ax.plot(NiIIIab, GeIIIab,'v', color = 'olive', alpha =1, label = 'IIIAB')
ax.plot(NiIIIe, GeIIIe,'v', color = 'slategray', alpha =1, label = 'IIIE')
ax.plot(NiIIIf, GeIIIf,'v', color = 'peru', alpha =1, label = 'IIIF')
ax.plot(NiIVa, GeIVa,'s', color = 'aquamarine', alpha =0.6, label = 'IVA')
ax.plot(NiIVb, GeIVb,'s', color = 'purple', alpha =0.6, label = 'IVB')
ax.plot(NiUg, GeUg,'x', color = 'black', label = 'Ungrouped')
# ax.plot(Ni4, Ge4,'D', markersize = 11, color = 'yellow', label = 'Mont Dieu (UG)')
ax.plot(Ni, Ge,'^', markersize = 14, color = 'darkorange', label = 'Sirjan 001')
ax.plot(Ni2, Ge2,'D', markersize = 11, color = 'green', label = 'Nedagolla (UG)')
# ax.plot(Ni3, Ge3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.set_xlim(5,20)
# ax.set_ylim(20,200)
plt.ylabel('Ge (ppm)', fontsize = 14)
plt.xlabel('Ni (wt%)', fontsize = 14)
plt.title("Iron Meteorite Distribution, Ni vs. Ge", fontsize = 14)
ax.legend(numpoints = 1, loc = 'best',fontsize = 10, markerscale = 0.8, prop={'size': 8})

plt.savefig("Ni_Ge.pdf",format='pdf')
plt.show()


# #================================================================================================================
# # fig = plt.figure(figsize=(6,5))
# ax = plt.axes()
# ax.set_xscale('log')
# ax.set_yscale('log')
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.set_aspect('auto')
# ax.plot(NiIab, GaIab,'.', color = 'b', alpha =0.6, label = 'IAB')
# ax.plot(NiIc, GaIc,'.', color = 'g', alpha =0.6, label = 'IC')
# ax.plot(NiIIab, GaIIab,'o', color = 'r', alpha =0.6, label = 'IIAB')
# ax.plot(NiIIc, GaIIc,'o', color = 'c', alpha =0.6, label = 'IIC')
# ax.plot(NiIId, GaIId,'o', color = 'm', alpha =0.6, label = 'IID')
# ax.plot(NiIIe, GaIIe,'o', color = 'yellow', label = 'IIE')
# ax.plot(NiIIf, GaIIf,'o', color = 'hotpink', alpha =0.6, label = 'IIF')
# ax.plot(NiIIg, GaIIg,'o', color = 'pink', alpha =0.6, label = 'IIG')
# ax.plot(NiIIIab, GaIIIab,'v', color = 'olive', label = 'IIIAB')
# ax.plot(NiIIIe, GaIIIe,'v', color = 'slategray', label = 'IIIE')
# ax.plot(NiIIIf, GaIIIf,'v', color = 'peru', label = 'IIIF')
# ax.plot(NiIVa, GaIVa,'s', color = 'aquamarine', alpha =0.6, label = 'IVA')
# ax.plot(NiIVb, GaIVb,'s', color = 'purple', alpha =0.6, label = 'IVB')
# ax.plot(NiUg, GaUg,'x', color = 'black', label = 'Ungrouped')
# ax.plot(Ni, Ga,'v', markersize = 20, color = 'orange', label = 'Sirjan 001')
# ax.plot(Ni2, Ga2,'D', markersize = 20, color = 'D', label = 'Nedagolla (UG)')
# # ax.plot(Ni3, Ga3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# # ax.plot(Ni4, Ga4,'*', markersize = 12, color = 'green', label = 'Mont Dieu (IIE)')
# ax.set_xlim(4,60)
# ax.set_ylim(0.01,1000)


# plt.ylabel('Ga (ppm)', fontsize = 12)
# plt.xlabel('Ni (wt%)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Ni vs. Ga", fontsize = 12)
# ax.legend(numpoints = 1, loc = 'upper right',fontsize = 7, markerscale = 0.8)

# # plt.savefig("Ni_Ga.pdf",format='pdf')

# NI VS IR

# fig = plt.figure(figsize=(5,5))
# plt.style.use('classic')
# ax = plt.axes()
# ax.set_xscale('log')
# ax.set_yscale('log')


# # for inlcuding tick labels in minor ticks and for modifying tick labels for major ticks
# ax.xaxis.set_minor_formatter(FormatStrFormatter('%d'))
# ax.yaxis.set_minor_formatter(FormatStrFormatter('%d'))
# ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
# ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
# # ax.tick_params(which = 'both', right=True, top=True, axis="y",direction="in")
# # ax.tick_params(which = 'both', right=True, top=True, axis="x",direction="in")
# ax.set_aspect('auto')
# ax.plot(NiIab, IrIab,'.', color = 'b', alpha =0.6, label = 'IAB')
# ax.plot(NiIc, IrIc,'.', color = 'g', alpha =0.6, label = 'IC')
# ax.plot(NiIIab, IrIIab,'o', color = 'r', alpha =0.6, label = 'IIAB')
# ax.plot(NiIIc, IrIIc,'o', color = 'c', alpha =0.6, label = 'IIC')
# ax.plot(NiIId, IrIId,'o', color = 'm', alpha =0.6, label = 'IID')
# ax.plot(NiIIe, IrIIe,'o', color = 'y', label = 'IIE')
# ax.plot(NiIIf, IrIIf,'o', color = 'hotpink', alpha =0.6, label = 'IIF')
# ax.plot(NiIIg, IrIIg,'o', color = 'pink', alpha =0.6, label = 'IIG')
# ax.plot(NiIIIab, IrIIIab,'v', color = 'olive', label = 'IIIAB')
# ax.plot(NiIIIe, IrIIIe,'v', color = 'slategray', label = 'IIIE')
# ax.plot(NiIIIf, IrIIIf,'v', color = 'peru', label = 'IIIF')
# ax.plot(NiIVa, IrIVa,'s', color = 'aquamarine', alpha =0.6, label = 'IVA')
# ax.plot(NiIVb, IrIVb,'s', color = 'purple', alpha =0.6, label = 'IVB')
# ax.plot(NiUg, IrUg,'x', color = 'black', label = 'Ungrouped')
# ax.plot(Ni, Ir,'^', markersize = 14, color = 'darkorange', label = 'Sirjan 001')
# ax.plot(Ni2, Ir2,'D', markersize = 11, color = 'green', label = 'Nedagolla (UG)')
# # ax.plot(Ni3, Ir3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# # ax.plot(Ni4, Ir4,'D', markersize = 11, color = 'yellow', label = 'Mont Dieu (UG)')
# # ax.set_xlim(4,60)
# # ax.set_ylim(0.01,100)
# # ax.set_xscale('log')
# # ax.set_yscale('log')

# plt.ylabel('Ir (ppm)', fontsize = 14)
# plt.xlabel('Ni (wt%)', fontsize = 14)
# plt.title("Iron Meteorite Distribution, Ni vs. Ir", fontsize = 14)
# ax.legend(numpoints = 1, loc = 'best',fontsize = 10, markerscale = 0.8)

# # # #plt.rcParams['axes.linewidth'] = 2

# plt.savefig("Ni_Ir.pdf",format='pdf')

#================================================================================================================

# # Au vs Ga
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIab, GaIab, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, GaIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, GaIIc, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, GaIId, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, GaIIf, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, GaIIIab, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, GaIIIf, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, GaIVa, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, GaIVb, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, GaUg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, Ga, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au2, Ga2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# ax.plot(Au3, Ga3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, Ga4,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# plt.ylabel('Ga (ppm)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs Ga", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_Ga.pdf",format='pdf')

# # Au vs Ge
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIab, GeIab, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, GeIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, GeIIc, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, GeIId, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, GeIIf, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, GeIIIab, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, GeIIIf, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, GeIVa, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, GeIVb, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, GeUg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, Ge, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au2, Ge2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# ax.plot(Au3, Ge3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, Ge4,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# plt.ylabel('Ge (ppm)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs Ge", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_Ge.pdf",format='pdf')

# # Au vs As
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIab, AsIab, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, AsIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, AsIIc, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, AsIId, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, AsIIf, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, AsIIIab, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, AsIIIf, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, AsIVa, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, AsIVb, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, AsUg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, As, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au3, As3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, As4,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# plt.ylabel('As (ppm)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs As", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_As.pdf",format='pdf')

# # Au vs Co
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIab, CoIab, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, CoIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, CoIIc, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, CoIId, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, CoIIf, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, CoIIIab, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, CoIIIf, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, CoIVa, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, CoIVb, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, CoUg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, Co, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au2, Co2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# ax.plot(Au3, Co3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, Co4,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# plt.ylabel('Co (mg/g)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs Co", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_Co.pdf",format='pdf')

# # Au vs Ni

# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# NiIIab_mg = [i*10 for i in NiIIab]
# NiIIIab_mg = [i*10 for i in NiIIIab]
# NiIab_mg = [i*10 for i in NiIab]
# NiIVa_mg = [i*10 for i in NiIVa]
# NiIVb_mg = [i*10 for i in NiIVb]
# NiUg_mg = [i*10 for i in NiUg]
# NiIIc_mg = [i*10 for i in NiIIc]
# NiIId_mg = [i*10 for i in NiIId]
# NiIIf_mg = [i*10 for i in NiIIf]
# NiIIIf_mg = [i*10 for i in NiIIIf]
# ax.plot(AuIab, NiIab_mg, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, NiIIab_mg, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, NiIIc_mg, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, NiIId_mg, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, NiIIf_mg, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, NiIIIab_mg, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, NiIIIf_mg, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, NiIVa_mg, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, NiIVb_mg, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, NiUg_mg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, Ni*10, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au2, Ni2*10,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# ax.plot(Au3, Ni3*10,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, Ni4*10,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# plt.ylabel('Ni (mg/g)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs Ni", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_Ni.pdf",format='pdf')

# # Au vs Cu
# # fig = plt.figure()
# # ax = fig.add_subplot()
# # ax.tick_params(axis="y",direction="in")
# # ax.tick_params(axis="x",direction="in")
# # ax.plot(AuIab, CuIab, '.', color = 'b', label = 'IAB')
# # ax.plot(AuIIab, CuIIab, 'o', color = 'r', label = 'IIAB')
# # ax.plot(AuIIc, CuIIc, 'o', color = 'c', label = 'IIC')
# # ax.plot(AuIId, CuIId, 'o', color = 'm', label = 'IID')
# # ax.plot(AuIIf, CuIIf, 'o', color = 'orange', label = 'IIF')
# # ax.plot(AuIIIab, CuIIIab, 'v', color = 'olive', label = 'IIIAB')
# # ax.plot(AuIIIf, CuIIIf, 'v', color = 'peru', label = 'IIIF')
# # ax.plot(AuIVa, CuIVa, 's', color = 'aquamarine', label = 'IVA')
# # ax.plot(AuIVb, CuIVb, 's', color = 'purple', label = 'IVB')
# # ax.plot(AuUg, CuUg, 'x', color = 'black', label = 'UG')
# # ax.plot(Au, Cu, '*', markersize = 10, color = 'black', label = 'Sirjan')
# # ax.plot(Au2, Cu2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# # ax.plot(Au3, Cu3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# # ax.set_yscale('log')
# # plt.ylabel('Cu (ppm)', fontsize = 12)
# # plt.xlabel('Au (ppm)', fontsize = 12)
# # plt.title("Iron Meteorite Distribution, Au vs Cu", fontsize = 12, fontweight = "bold")
# # ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# # plt.savefig("Au_Cr.pdf",format='pdf')

# # # Au vs Cr
# # fig = plt.figure()
# # ax = fig.add_subplot()
# # ax.tick_params(axis="y",direction="in")
# # ax.tick_params(axis="x",direction="in")
# # ax.plot(AuIab, CrIab, '.', color = 'b', label = 'IAB')
# # ax.plot(AuIIab, CrIIab, 'o', color = 'r', label = 'IIAB')
# # ax.plot(AuIIc, CrIIc, 'o', color = 'c', label = 'IIC')
# # ax.plot(AuIId, CrIId, 'o', color = 'm', label = 'IID')
# # ax.plot(AuIIf, CrIIf, 'o', color = 'orange', label = 'IIF')
# # ax.plot(AuIIIab, CrIIIab, 'v', color = 'olive', label = 'IIIAB')
# # ax.plot(AuIIIf, CrIIIf, 'v', color = 'peru', label = 'IIIF')
# # ax.plot(AuIVa, CrIVa, 's', color = 'aquamarine', label = 'IVA')
# # ax.plot(AuIVb, CrIVb, 's', color = 'purple', label = 'IVB')
# # ax.plot(AuUg, CrUg, 'x', color = 'black', label = 'UG')
# # ax.plot(Au, Cr, '*', markersize = 10, color = 'black', label = 'Sirjan')
# # ax.plot(Au2, Cr2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# # ax.set_yscale('log')
# # plt.ylabel('Cr (ppm)', fontsize = 12)
# # plt.xlabel('Au (ppm)', fontsize = 12)
# # plt.title("Iron Meteorite Distribution, Au vs Cr", fontsize = 12, fontweight = "bold")
# # ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# # plt.savefig("Au_Cr.pdf",format='pdf')

# # Au vs W
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIab, WIab, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, WIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, WIIc, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, WIId, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, WIIf, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, WIIIab, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, WIIIf, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, WIVa, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, WIVb, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, WUg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, W, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au2, W2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# ax.plot(Au3, W3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, W4,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# ax.set_yscale('log')
# plt.ylabel('W (ppm)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs W", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_W.pdf",format='pdf')

# # Au vs Pt
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIab, PtIab, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, PtIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, PtIIc, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, PtIId, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, PtIIf, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, PtIIIab, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, PtIIIf, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, PtIVa, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, PtIVb, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, PtUg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, Pt, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au2, Pt2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# ax.plot(Au3, Pt3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, Pt4,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# ax.set_yscale('log')
# plt.ylabel('Pt (ppm)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs Pt", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_Pt.pdf",format='pdf')



# # Au vs Ir
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIab, IrIab, '.', color = 'b', label = 'IAB')
# ax.plot(AuIIab, IrIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(AuIIc, IrIIc, 'o', color = 'c', label = 'IIC')
# ax.plot(AuIId, IrIId, 'o', color = 'm', label = 'IID')
# ax.plot(AuIIf, IrIIf, 'o', color = 'orange', label = 'IIF')
# ax.plot(AuIIIab, IrIIIab, 'v', color = 'olive', label = 'IIIAB')
# ax.plot(AuIIIf, IrIIIf, 'v', color = 'peru', label = 'IIIF')
# ax.plot(AuIVa, IrIVa, 's', color = 'aquamarine', label = 'IVA')
# ax.plot(AuIVb, IrIVb, 's', color = 'purple', label = 'IVB')
# ax.plot(AuUg, IrUg, 'x', color = 'black', label = 'UG')
# ax.plot(Au, Ir, '*', markersize = 10, color = 'black', label = 'Sirjan')
# ax.plot(Au2, Ir2,'*', markersize = 8, color = 'hotpink', label = 'Nedagolla, UG')
# ax.plot(Au3, Ir3,'*', markersize = 8, color = 'green', label = 'Del Rio, IIF')
# ax.plot(Au4, Ir4,'*', markersize = 8, color = 'lightslategray', label = 'Mont Dieu, IIE')
# ax.set_yscale('log')
# plt.ylabel('Ir (ppm)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs Ir", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

# plt.savefig("Au_Ir.pdf",format='pdf')

# Au vs Sb
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.tick_params(axis="y",direction="in")
# ax.tick_params(axis="x",direction="in")
# ax.plot(AuIIab, SbIIab, 'o', color = 'r', label = 'IIAB')
# ax.plot(Au, Sb, 'D', markersize = 6, color = 'black', label = 'Sirjan')
# ax.set_yscale('log')
# plt.ylabel('Ir (ppm)', fontsize = 12)
# plt.xlabel('Au (ppm)', fontsize = 12)
# plt.title("Iron Meteorite Distribution, Au vs Ir", fontsize = 12, fontweight = "bold")
# ax.legend(numpoints = 1, bbox_to_anchor=(1.05, 1.0), loc = 'upper right',fontsize = 7)

plt.show()
