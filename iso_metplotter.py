import matplotlib.pyplot as plt
import pandas as pd
from numpy import *

plt.rc('font', family='calibri')
plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


xls = pd.ExcelFile('IronMetIsoData.xlsx')

# all in eplsion [Mo92, Mo94, Mo95. Mo97, Mo100]
isotope = ['\u03B5$^{92}$Mo', '\u03B5$^{94}$Mo', '\u03B5$^{95}$Mo', '\u03B5$^{97}$Mo', '\u03B5$^{100}$Mo']  
# data from Spitzer 2020

dfMo = pd.read_excel(xls,'Mo')
IcMo = dfMo['IC']
ErrIcMo = dfMo['± 95% CI (IC)']
IIabMo = dfMo['IIAB']
ErrIIabMo = dfMo['± 95% CI (IIAB)']
IIdMo = dfMo['IID']
ErrIIdMo = dfMo['± 95% CI (IID)']
IIIabMo = dfMo['IIIAB']
ErrIIIabMo = dfMo['± 95% CI (IIIAB)']
IIIeMo = dfMo['IIIE']
ErrIIIeMo = dfMo['± 95% CI (IIIE)']

# only have Mo94 and Mo95 data
IabMo = dfMo['IAB']
ErrIabMo = dfMo['± 95% CI (IAB)']
IIcMo = dfMo['IIC']
ErrIIcMo = dfMo['± 95% CI (IIC)']
IIeMo = dfMo['IIE']
ErrIIeMo = dfMo['± 95% CI (IIE)']
IIfMo = dfMo['IIF']
ErrIIfMo = dfMo['± 95% CI (IIF)']
IIIfMo = dfMo['IIIF']
ErrIIIfMo = dfMo['± 95% CI (IIIF)']
IVaMo = dfMo['IVA']
ErrIVaMo = dfMo['± 95% CI (IVA)']
IVbMo = dfMo['IVB']
ErrIVbMo = dfMo['± 95% CI (IVB)']

sirjMo = [99, 61, 40.5, 29.5, 21]
sirjMo = [i/100 for i in sirjMo]
ErrSirjMo = [70, 16, 9, 7, 29]
ErrSirjMo = [i/100 for i in ErrSirjMo]

nedMo = dfMo['Nedagolla']
ErrNedMo = dfMo['± 95% CI (Ned)']

mdMo = dfMo['Mont Dieu']
ErrMdMo = dfMo['± 95% CI (MD)']

nedUncorr = [.64, .545, .32, .16, .10]
ErrNedUncorr = [.1, .075, .06, .06, .06]

x = linspace(0.,3.0, 10)
y = 0.528 * x -0.058


# Plots
fig = plt.figure()

ax = fig.add_subplot()

ax.tick_params(axis="y",direction="in")
ax.tick_params(axis="x",direction="in")

ax.set_xlabel('\u03B5$^{94}$Mo')
ax.set_ylabel('\u03B5$^{95}$Mo')
# twin1.set_ylabel('\u0394' + '$T_{CAI}$')

ax.errorbar(IcMo[1], IcMo[2], xerr = ErrIcMo[1], yerr = ErrIcMo[2], color = 'red', marker = 'D', markersize = '8', label = 'IC')
ax.errorbar(IIabMo[1], IIabMo[2], xerr = ErrIIabMo[1], yerr = ErrIIabMo[2], color = 'red', marker = 's', markersize = '8', label = 'IIAB')
ax.errorbar(IIIabMo[1], IIIabMo[2], xerr = ErrIIIabMo[1], yerr = ErrIIIabMo[2], color = 'red', marker = 'o', markersize = '8', label = 'IIIAB')
ax.errorbar(IIIeMo[1], IIIeMo[2], xerr = ErrIIIeMo[1], yerr = ErrIIIeMo[2], color = 'red', marker = 's', markersize = '8', label = 'IIIE')
ax.errorbar(IVaMo[1], IVaMo[2], xerr = ErrIVaMo[1], yerr = ErrIVaMo[2], color = 'red', marker = '^', markersize = '8', label = 'IVA')

ax.errorbar(IIcMo[1], IIcMo[2], xerr = ErrIIcMo[1], yerr = ErrIIcMo[2], color = 'blue', marker = '>', markersize = '8', label = 'IIC')
ax.errorbar(IIdMo[1], IIdMo[2], xerr = ErrIIdMo[1], yerr = ErrIIdMo[2], color = 'blue', marker = 'v', markersize = '8', label = 'IID')
ax.errorbar(IIfMo[1], IIfMo[2], xerr = ErrIIfMo[1], yerr = ErrIIfMo[2], color = 'blue', marker = 'o', markersize = '8', label = 'IIF')
ax.errorbar(IIIfMo[1], IIIfMo[2], xerr = ErrIIIfMo[1], yerr = ErrIIIfMo[2], color = 'blue', marker = '^', markersize = '8', label = 'IIIF')
ax.errorbar(IVbMo[1], IVbMo[2], xerr = ErrIVbMo[1], yerr = ErrIVbMo[2], color = 'blue', marker = 'D', markersize = '8', label = 'IVB')


ax.errorbar(sirjMo[1], sirjMo[2], xerr = ErrSirjMo[1], yerr = ErrSirjMo[2], color = 'black', marker = 'p', markersize = '10', label = 'Sirjan')
ax.errorbar(nedMo[1], nedMo[2], xerr = ErrNedMo[1], yerr = ErrNedMo[2], color = 'orange', marker = 'p', markersize = '10', label = 'Nedagolla')
# ax.errorbar(mdMo[1], mdMo[2], xerr = ErrMdMo[1], yerr = ErrMdMo[2], color = 'green', marker = 'p', markersize = '10', label = 'Mont Dieu')
# ax.plot(x, y, color = 'r', alpha =0.7)

ax.legend(numpoints = 1, loc = 'best',fontsize = 7, markerscale =0.8)
plt.savefig("Mo94_95.pdf",format='pdf')



plt.rc('axes', labelsize=15)
plt.rc('xtick', labelsize= 15)
plt.rc('ytick', labelsize= 13)
plt.rc('legend', fontsize= 13) 

fig = plt.figure(figsize=(6,5))
# plt.style.use('classic')
ax = fig.add_subplot()

ax.tick_params(which = 'both', right=True, top=True, axis="y",direction="in")
ax.tick_params(which = 'both', right=True, top=True, axis="x",direction="in")


# ax.errorbar(isotope, IcMo, yerr = ErrIcMo, color = 'red', marker = 'D', markersize = '8', alpha =0.7, label = 'IC')
# ax.errorbar(isotope, IIabMo, yerr = ErrIIabMo, color = 'red', marker = 's', markersize = '8', alpha =0.7, label = 'IIAB')
# ax.errorbar(isotope, IIIabMo,yerr = ErrIIIabMo, color = 'red', marker = 'o', markersize = '8', alpha =0.7, label = 'IIIAB')
# ax.errorbar(isotope, IIIeMo, yerr = ErrIIIeMo, color = 'red', marker = 's', markersize = '8', alpha =0.7, label = 'IIIE')
# ax.errorbar(isotope, IVaMo, yerr = ErrIVaMo, color = 'red', marker = '^', markersize = '8', alpha =0.7, label = 'IVA')

# ax.errorbar(isotope, IIcMo, yerr = ErrIIcMo, color = 'blue', marker = '>', markersize = '8', alpha =0.7, label = 'IIC')
# ax.errorbar(isotope, IIdMo, yerr = ErrIIdMo, color = 'blue', marker = 'v', markersize = '8', alpha =0.7, label = 'IID')
# ax.errorbar(isotope, IIfMo, yerr = ErrIIfMo, color = 'blue', marker = 'o', markersize = '8', alpha =0.7, label = 'IIF')
# ax.errorbar(isotope, IIIfMo, yerr = ErrIIIfMo, color = 'blue', marker = '^', markersize = '8', alpha =0.7, label = 'IIIF')
# ax.errorbar(isotope, IVbMo, yerr = ErrIVbMo, color = 'blue', marker = 'D', markersize = '8', alpha =0.7, label = 'IVB')

sirjMo = [i*100 for i in sirjMo]
ErrSirjMo = [i*100 for i in ErrSirjMo]
nedMo = [i*100 for i in nedMo]
ErrNedMo = [i*100 for i in ErrNedMo]


isotope = ['\u03bc$^{92}$Mo', '\u03bc$^{94}$Mo', '\u03bc$^{95}$Mo', '\u03bc$^{97}$Mo', '\u03bc$^{100}$Mo']
ax.errorbar(isotope, sirjMo, yerr = ErrSirjMo, color = 'darkorange', marker = '^', markersize = '10', markeredgewidth = 1., markeredgecolor = 'black', label = 'Sirjan 001')
ax.errorbar(isotope, nedMo, yerr = ErrNedMo, color = 'green', marker = 'D', markersize = '8', markeredgewidth = 1., markeredgecolor = 'black', label = 'Nedagolla (UG)')
# ax.errorbar(isotope, mdMo, yerr = ErrMdMo, color = 'green', marker = 'p', markersize = '10', alpha = 0.8, label = 'Mont Dieu')
# plt.ylabel('\u03bc - deviation')
# plt.axhline(y = 0, color = 'gray')
# plt.xticks(fontsize=16)
ax.set_ylim(0,120)
# for t in ax.get_xticklabels():
    # t.set_fontstyle('italic')
leg = plt.legend(numpoints = 1, loc = 'best', markerscale =1., frameon=False)
plt.savefig("MoIso.pdf",format='pdf')

plt.show()