import matplotlib.pyplot as plt

plt.rc('font', family='calibri')
plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True

# Radiochronology data for NC and CC groups from Kruijer et al. 2017, supplemental info (table s5) 
# Corresponding time since CAI formation included

# ==============================================
# epsilon W-182 preexposure

# NC
IC_w182 = -3.45
ErrIC_w182 = .04
IIAB_w182 = -3.40
ErrIIAB_w182 = .03
IIE_w182 = - 2.527272727
ErrIIE_w182 = 0.11
IIIAB_w182 = -3.35
ErrIIIAB_w182 = .03
IIIE_w182 = -3.28
ErrIIIE_w182 = .06
IVA_w182 = -3.32
ErrIVA_w182 = .05
# CC ------------------
IIC_w182 = -3.2
ErrIIC_w182 = .12
IID_w182 = -3.23
ErrIID_w182 = .04
IIF_w182 = -3.21
ErrIIF_w182 = .05
IIIF_w182 = -3.24
ErrIIIF_w182 = .1
IVB_w182 = -3.18
ErrIVB_w182 = .05

# ==============================================
#  epsilon W-183

# NC
IC_w183 = -0.05
ErrIC_w183 = .02
IIAB_w183 = -0.02
ErrIIAB_w183 = .02
IIE_w183 = - -0.095
ErrIIE_w183 = 0.04636363636
IIIAB_w183 = -0.03
ErrIIIAB_w183 = .02
IIIE_w183 = -0.05
ErrIIIE_w183 = .04
IVA_w183 = 0.
ErrIVA_w183 = .07
# CC ------------------
IIC_w183 = 0.30
ErrIIC_w183 = .04
IID_w183 = 0.13
ErrIID_w183 = .01
IIF_w183 = 0.09
ErrIIF_w183 = .02
IIIF_w183 = 0.08
ErrIIIF_w183 = .07
IVB_w183 = 0.13
ErrIVB_w183 = .02

# ==============================================
#  time since CAI

# NC
IC_dT = 0.3
IIAB_dT = 0.8
IIE_dT = 10.96
IIIAB_dT = 1.2
IIIE_dT = 1.8
IVA_dT = 1.5
# CC ------------------
IIC_dT = 2.6
IID_dT = 2.3
IIF_dT = 2.5
IIIF_dT = 2.2
IVB_dT = 2.8

# ==============================================
# Sirjan data

sirj_w182 = -2.962
ErrSirj_w182 = .045

sirj_w183 = -.013
ErrSirj_w183 = .040

sirj_dT = 5.2
ErrSirj_dT = .4


# ==============================================
# Mont Dieu data

md_w182 = -2.96
ErrMd_w182 = .1

md_w183 = -.013
ErrMd_w183 = .03

md_dT = 5.2
ErrMd_dT = 1.3

# ==============================================
# Nedagolla data

N_w182 = -2.77
ErrN_w182 = .18

N_w183 = 0.09
ErrN_w183 = .09

N_dT = 7.8
ErrN_dT = 2.8

# ==============================================
# plotting routine

fig = plt.figure()

ax = fig.add_subplot()
# twin1 = ax.twinx()

ax.tick_params(axis="y",direction="in")
ax.tick_params(axis="x",direction="in")

ax.set_xlabel('\u03B5$^{183}$W')
ax.set_ylabel('\u03B5$^{182}$W')
# twin1.set_ylabel('\u0394' + '$T_{CAI}$')

ax.errorbar(IC_w183, IC_w182, xerr = ErrIC_w183, yerr = ErrIC_w182, color = 'red', marker = 'D', markersize = '8', label = 'IC')
ax.errorbar(IIAB_w183, IIAB_w182, xerr = ErrIIAB_w183, yerr = ErrIIAB_w182, color = 'red', marker = 's', markersize = '8', label = 'IIAB')
# ax.errorbar(IIE_w183, IIE_w182, xerr = ErrIIE_w183, yerr = ErrIIE_w182, color = 'red', marker = 'o', markersize = '8', label = 'IIE')
ax.errorbar(IIIAB_w183, IIIAB_w182, xerr = ErrIIIAB_w183, yerr = ErrIIIAB_w182, color = 'red', marker = 'o', markersize = '8', label = 'IIIAB')
ax.errorbar(IIIE_w183, IIIE_w182, xerr = ErrIIIE_w183, yerr = ErrIIIE_w182, color = 'red', marker = 's', markersize = '8', label = 'IIIE')
ax.errorbar(IVA_w183, IVA_w182, xerr = ErrIVA_w183, yerr = ErrIVA_w182, color = 'red', marker = '^', markersize = '8', label = 'IVA')

ax.errorbar(IIC_w183, IIC_w182, xerr = ErrIIC_w183, yerr = ErrIIC_w182, color = 'blue', marker = '>', markersize = '8', label = 'IIC')
ax.errorbar(IID_w183, IID_w182, xerr = ErrIID_w183, yerr = ErrIID_w182, color = 'blue', marker = 'v', markersize = '8', label = 'IID')
ax.errorbar(IIF_w183, IIF_w182, xerr = ErrIIF_w183, yerr = ErrIIF_w182, color = 'blue', marker = 'o', markersize = '8', label = 'IIF')
ax.errorbar(IIIF_w183, IIIF_w182, xerr = ErrIIIF_w183, yerr = ErrIIIF_w182, color = 'blue', marker = '^', markersize = '8', label = 'IIIF')
ax.errorbar(IVB_w183, IVB_w182, xerr = ErrIVB_w183, yerr = ErrIVB_w182, color = 'blue', marker = 'D', markersize = '8', label = 'IVB')

ax.errorbar(sirj_w183, sirj_w182, xerr = ErrSirj_w183, yerr = ErrSirj_w182, color = 'black', marker = 'p', markersize = '10', label = 'Sirjan')
ax.errorbar(md_w183, md_w182, xerr = ErrMd_w183, yerr = ErrMd_w182, color = 'green', marker = 'p', markersize = '10', alpha = 0.7, label = 'Mont Dieu (UG)')
ax.errorbar(N_w183, N_w182, xerr = ErrN_w183, yerr = ErrN_w182, color = 'orange', marker = 'p', markersize = '10', alpha = 1., label = 'Nedagolla (UG)')
ax.legend(numpoints = 1, loc = 'best',fontsize = 7, markerscale =0.8)
plt.savefig("Wtime.pdf",format='pdf')
plt.show()