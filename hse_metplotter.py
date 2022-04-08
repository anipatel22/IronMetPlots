from typing import ValuesView
import matplotlib.pyplot as plt
import pandas as pd

xls = pd.ExcelFile('IronMeteoriteData.xlsx')
dfIAB = pd.read_excel(xls, 'IABnorm')
dfIC = pd.read_excel(xls,'ICnorm')
dfIIAB = pd.read_excel(xls, 'IIABnorm')
dfIIC = pd.read_excel(xls, 'IICnorm')
dfIID = pd.read_excel(xls, 'IIDnorm')
dfIIF = pd.read_excel(xls, 'IIFnorm')
dfIIIAB = pd.read_excel(xls, 'IIIABnorm')
dfIIIF = pd.read_excel(xls,'IIIFnorm')
dfIIIE = pd.read_excel(xls,'IIIEnorm')
dfIVA = pd.read_excel(xls,'IVAnorm')
dfIVB = pd.read_excel(xls, 'IVBnorm')
dfUG = pd.read_excel(xls, 'UGnorm')

# These are IVA meteorite compositions from McCoy et al. 2011 normalized to Orgueil
elem = dfIVA['Elem']
JT = dfIVA['Jamestown AVG']
ME = dfIVA['Maria Elena AVG']
Y = dfIVA['Yanhuitlan AVG']
G = dfIVA['Gibeon AVG']
C = dfIVA['Charlotte AVG']
M = dfIVA['Muonionalusta']
BL = dfIVA['Bushman Land AVG']
S = dfIVA['Steinbach AVG']
NW = dfIVA['New Westville  AVG']
D = dfIVA['Duchesne AVG']
DH = dfIVA['Duel Hill (1854) AVG']
FC = dfIVA['Fuzzy Creek AVG']
C2 = dfIVA['Chinautla AVG']
E = dfIVA['EET 83230']

# These are IVB meteorite compositions from Walker et al. 2008, Campbell and Humayun 2005,
# and Honesto et al. 2007 normalized to Orgueil.
mIVB1 = dfIVB['CoGH AVG']
mIVB2 = dfIVB['Iquique']
mIVB3 = dfIVB['Kokomo']
mIVB4 = dfIVB['Tlacotepec AVG']
mIVB5 = dfIVB['Hoba AVG']
mIVB6 = dfIVB['Santa Clara']
mIVB7 = dfIVB['Tinnie']
mIVB8 = dfIVB['Temera']
mIVB9 = dfIVB['Weaver Mtns AVG']
mIVB10 = dfIVB['Tawallah Valley AVG']
mIVB11 = dfIVB['Skookum AVG']
mIVB12 = dfIVB['Warburton  Range AVG']
mIVB13 = dfIVB['Cape of Good Hope ']
mIVB14 = dfIVB['Tlacotepec']
mIVB15 = dfIVB['Hoba']
mIVB16 = dfIVB['Santa Clara2']
mIVB17 = dfIVB['Skookum']
mIVB18 = dfIVB['Tawallah Valley']
mIVB19 = dfIVB['Warburton Range']
mIVB20 = dfIVB['Weaver Mountains']
mIVB21 = dfIVB['Iquique2']
mIVB22 = dfIVB['Kokomo2']

#IAB meteorite compositions from Worsham et al. 2016 normalized to Orgueil
mIAB1 = dfIAB['Landes']
mIAB2 = dfIAB['Seligman']
mIAB3 = dfIAB['Yenberrie']
mIAB4 = dfIAB['Ballinger AVG']
mIAB5 = dfIAB['Cranbourne']
mIAB6 = dfIAB['Campo del Cielo']
mIAB7 = dfIAB['New Leipzig']
mIAB8 = dfIAB['Magura']
mIAB9 = dfIAB['Canyon Diablo']
mIAB10 = dfIAB['Odessa']
mIAB11 = dfIAB['Jenkins']
mIAB12 = dfIAB['ALHA 77283']
mIAB13 = dfIAB['Youndegin']
mIAB14 = dfIAB['Smithville']
mIAB15 = dfIAB['Seymour']
mIAB16 = dfIAB['Bogou']
mIAB17 = dfIAB['Burgavali']
mIAB18 = dfIAB['Morasko']
mIAB19 = dfIAB['Seeliisgen']
mIAB20 = dfIAB['Sarepta AVG']
mIAB21 = dfIAB['Hope']
mIAB22 = dfIAB['Pine River']
mIAB23 = dfIAB['Shrewsbury AVG']
mIAB24 = dfIAB['Comanche']
mIAB25 = dfIAB['Bahjoi']
mIAB26 = dfIAB['Toluca']
mIAB27 = dfIAB['Deport']
mIAB28 = dfIAB['Balfour Downs']
mIAB29 = dfIAB['Bischtiibe AVG']
mIAB30 = dfIAB['Goose Lake']
mIAB31 = dfIAB['Persimmon Creek AVG']
mIAB32 = dfIAB['Mungindi']
mIAB33 = dfIAB['Edmonton (KY) AVG']
mIAB34 = dfIAB['Maltahohe']
mIAB35 = dfIAB['Anoka AVG']
mIAB36 = dfIAB['Carlton']
mIAB37 = dfIAB['Lamesa AVG']
mIAB38 = dfIAB['Tazewell']
mIAB39 = dfIAB['Dayton AVG']
mIAB40 = dfIAB['Freda']
mIAB41 = dfIAB['Quarat al Hanish']
mIAB42 = dfIAB['Chebankol']
mIAB43 = dfIAB['Sombrerete']
mIAB44 = dfIAB['Kofa']
mIAB45 = dfIAB['ALHA 80104']
mIAB46 = dfIAB['Mount Magnet']
mIAB47 = dfIAB['TIL 91725']
mIAB48 = dfIAB['Caddo County']
mIAB49 = dfIAB['Zagora']
mIAB50 = dfIAB['Mertzon']
mIAB51 = dfIAB['EET 84300 AVG']
mIAB52 = dfIAB['Woodbine']
mIAB53 = dfIAB['Pitts AVG']
mIAB54 = dfIAB['Mundrabilla']
mIAB55 = dfIAB['Duplicate']
mIAB56 = dfIAB['Waterville AVG']
mIAB57 = dfIAB['Georgetown']
mIAB58 = dfIAB['Osseo']
mIAB59 = dfIAB['Sardis AVG']

# IC comps from Tornabene 2020 normalized to Orgueil
mIC1 = dfIC['Arispe']
mIC2 = dfIC['Union County']
mIC3 = dfIC['Mount Dooling']
mIC4 = dfIC['Bendego']
mIC5 = dfIC['Chihuahua City']
mIC6 = dfIC['NWA 2743']
mIC7 = dfIC['St. Francois County']
mIC8 = dfIC['Santa Rosa']
mIC9 = dfIC['Nocoleche (anomalous)']
mIC10 = dfIC['Winburg (anomalous)']

# IIAB comps from Hilton 2020 normalized to Orgueil
mIIAB1 = dfIIAB['USNM1']
mIIAB2 = dfIIAB['USNM2']
mIIAB3 = dfIIAB['USNM3']
mIIAB4 = dfIIAB['USNM4']
mIIAB5 = dfIIAB['USNM5']

# IIC comps from Tornabene 2020 normalized to Orgueil
mIIC1 = dfIIC['Darinskoe']
mIIC2 = dfIIC['Perryville']
mIIC3 = dfIIC['Cratheu´s (1950)']
mIIC4 = dfIIC['Kumerina']
mIIC5 = dfIIC['Ballinoo']
mIIC6 = dfIIC['Salt River']
mIIC7 = dfIIC['Unter Mässing']
mIIC8 = dfIIC['Wiley']
mIIC9 = dfIIC['Cratheu´s (Field Museum)']
mIIC10 = dfIIC['Para`  de Minas']

# IID comps from Hilton 2020 normalized to Orgueil
mIID1 = dfIID['UCLA']
mIID2 = dfIID['USNM 2467']
mIID3 = dfIID['USNM 1071']
mIID4 = dfIID['USNM 2397']
mIID5 = dfIID['USNM']
mIID6 = dfIID['USNM 777']
mIID7 = dfIID['USNM 309']
mIID8 = dfIID['USNM 838']
mIID9 = dfIID['USNM 3008']
mIID10 = dfIID['USNM 3016']
mIID11 = dfIID['USNM 3533']
mIID12 = dfIID['USNM 788']

# IIF comps from Hilton 2020 (IIF paper) normalized to Orgueil
mIIF1 = dfIIF['Dorofeevka']
DelRio = dfIIF['Del Rio']
mIIF3 = dfIIF['Monahans (1983)']
mIIF4 = dfIIF['Purmela']
mIIF5 = dfIIF['Repeev Khutor']
mIIF6 = dfIIF['Corowa']

# IIIAB comps from Hilton 2020 normalized to Orgueil
mIIIAB1 = dfIIIAB['m1']
mIIIAB2 = dfIIIAB['m2']
mIIIAB3 = dfIIIAB['m3']
mIIIAB4 = dfIIIAB['m4']
mIIIAB5 = dfIIIAB['m5']

# IIIE comps from normalized to Orgueil
mIIIE1 = dfIIIE['Armanty']
mIIIE2 = dfIIIE['Ulasitai']

# IIIF comps from Zhang et al. 2022 normalized to Orgueil
mIIIF1 = dfIIIF['Cerro del Inca']
mIIIF2 = dfIIIF['Moonbi']
mIIIF3 = dfIIIF['St. Genevieve County']
mIIIF4 = dfIIIF['Clark County']
mIIIF5 = dfIIIF['Nelson County']
mIIIF6 = dfIIIF['Oakley (iron)']
mIIIF7 = dfIIIF['Klamath Falls']
mIIIF8 = dfIIIF['Fitzwater Pass']


# Ungrouped comps normalized to Orgueil
mUG1 = dfUG["Babb's Mill"]
mUG2 = dfUG["South Byron"]
mUG3 = dfUG["ILD 83500"]
mUG4 = dfUG["unknown"]
mUG5 = dfUG["ALH84233"]
mUG6 = dfUG["EET87516"]
mUG7 = dfUG["LEW85369"]
mUG8 = dfUG["LEW86211"]
mUG9 = dfUG["Oglat Sidi Ali, Morroco"]
mUG10 = dfUG["Chinga"]
mUG11 = dfUG["Tishomingo"]
mUG12 = dfUG["Willow Grove"]
mUG13 = dfUG["Nedagolla"]

# Sirjan LA ICP MS
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

# nomralizing Sirjan to Orgueil (Palme Lodders 2014)
Re = Re/0.04
Os = Os/0.495
Ir = Ir/0.469
Ru = Ru/0.69
Pt = Pt/0.925
Pd = Pd/0.56

sirj = [Re, Os, Ir, Ru, Pt, Pd]

nedag = [10.6, 11.7717, 9.5394, 8.402898551, 8.596756757, 3.130357143]


fig = plt.figure()
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

ax1.tick_params(axis="y",direction="in")
ax1.tick_params(axis="x",direction="in")
ax1.set_title('IVA')
ax1.set_ylabel('HSE/Orgueil')

ax2.tick_params(axis="y",direction="in")
ax2.tick_params(axis="x",direction="in")
ax2.set_title('IVB')

ax3.tick_params(axis="y",direction="in")
ax3.tick_params(axis="x",direction="in")
ax3.set_title('IAB')

ax4.tick_params(axis="y",direction="in")
ax4.tick_params(axis="x",direction="in")
ax4.set_title('IIAB')
ax4.set_ylabel('HSE/Orgueil')

ax5.tick_params(axis="y",direction="in")
ax5.tick_params(axis="x",direction="in")
ax5.set_title('IIIAB')

ax6.tick_params(axis="y",direction="in")
ax6.tick_params(axis="x",direction="in")
ax6.set_title('UG')



ax1.plot(elem, JT, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, ME, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, Y, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, G, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, C, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, M, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, BL, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, S, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, NW, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, D, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, DH, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, FC, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, C2, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, E, color = 'red', marker = '.', lw = 0.5)
ax1.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax1.axhline(y = 0, color = 'black', lw = 0.5)

ax2.plot(elem, mIVB1, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB2, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB3, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB4, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB5, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB6, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB7, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB8, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB9, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB10, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB11, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB12, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB13, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB14, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB15, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB16, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB17, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB18, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB19, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB20, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB21, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, mIVB22, color = 'red', marker = '.', lw = 0.5)
ax2.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax2.axhline(y = 0, color = 'black', lw = 0.5)

ax3.plot(elem, mIAB1, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB2, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB3, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB4, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB5, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB6, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB7, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB8, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB9, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB10, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB11, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB12, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB13, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB14, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB15, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB16, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB17, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB18, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB19, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB20, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB21, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB22, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB23, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB24, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB25, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB26, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB27, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB28, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB29, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB30, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB31, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB32, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB33, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB34, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB35, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB36, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB37, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB38, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB39, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB40, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB41, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB42, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB43, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB44, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB45, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB46, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB47, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB48, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB49, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB50, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB51, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB52, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB53, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB54, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB55, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB56, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB57, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB58, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, mIAB59, color = 'red', marker = '.', lw = 0.5)
ax3.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax3.axhline(y = 0, color = 'black', lw = 0.5)

ax4.plot(elem, mIIAB1, color = 'red', marker = '.', lw = 0.5)
ax4.plot(elem, mIIAB2, color = 'red', marker = '.', lw = 0.5)
ax4.plot(elem, mIIAB3, color = 'red', marker = '.', lw = 0.5)
ax4.plot(elem, mIIAB4, color = 'red', marker = '.', lw = 0.5)
ax4.plot(elem, mIIAB5, color = 'red', marker = '.', lw = 0.5)
ax4.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax4.axhline(y = 0, color = 'black', lw = 0.5)

ax5.plot(elem, mIIIAB1, color = 'red', marker = '.', lw = 0.5)
ax5.plot(elem, mIIIAB2, color = 'red', marker = '.', lw = 0.5)
ax5.plot(elem, mIIIAB3, color = 'red', marker = '.', lw = 0.5)
ax5.plot(elem, mIIIAB4, color = 'red', marker = '.', lw = 0.5)
ax5.plot(elem, mIIIAB5, color = 'red', marker = '.', lw = 0.5)
ax5.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax5.axhline(y = 0, color = 'black', lw = 0.5)


ax6.plot(elem, mUG1, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG2, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG3, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG4, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG5, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG6, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG7, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG8, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG9, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG10, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG11, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG12, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, mUG13, color = 'red', marker = '.', lw = 0.5)
ax6.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax6.plot(elem, nedag, color = 'green', marker = '.', lw = 0.5)
ax5.axhline(y = 0, color = 'black', lw = 0.5)

fig = plt.figure()
ax11 = fig.add_subplot(231)
ax12 = fig.add_subplot(232)
ax13 = fig.add_subplot(233)
ax14 = fig.add_subplot(234)
ax15 = fig.add_subplot(235)
ax16 = fig.add_subplot(236)

ax11.tick_params(axis="y",direction="in")
ax11.tick_params(axis="x",direction="in")
ax11.set_title('IIC')
ax11.set_ylabel('HSE/Orgueil')

ax12.tick_params(axis="y",direction="in")
ax12.tick_params(axis="x",direction="in")
ax12.set_title('IID')

ax13.tick_params(axis="y",direction="in")
ax13.tick_params(axis="x",direction="in")
ax13.set_title('IIF')

ax14.tick_params(axis="y",direction="in")
ax14.tick_params(axis="x",direction="in")
ax14.set_title('IIIF')
ax14.set_ylabel('HSE/Orgueil')

ax15.tick_params(axis="y",direction="in")
ax15.tick_params(axis="x",direction="in")
ax15.set_title('IC')

ax16.tick_params(axis="y",direction="in")
ax16.tick_params(axis="x",direction="in")
ax16.set_title('IIIE')


ax11.plot(elem, mIIC1, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC2, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC3, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC4, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC5, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC6, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC7, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC8, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC9, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, mIIC10, color = 'red', marker = '.', lw = 0.5)
ax11.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax11.axhline(y = 0, color = 'black', lw = 0.5)

ax12.plot(elem, mIID1, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID2, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID3, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID4, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID5, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID6, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID7, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID8, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID9, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID10, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID11, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, mIID12, color = 'red', marker = '.', lw = 0.5)
ax12.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax12.axhline(y = 0, color = 'black', lw = 0.5)

ax13.plot(elem, mIIF1, color = 'red', marker = '.', lw = 0.5)
ax13.plot(elem, DelRio, color = 'purple', marker = '.', lw = 0.5)
ax13.plot(elem, mIIF3, color = 'red', marker = '.', lw = 0.5)
ax13.plot(elem, mIIF4, color = 'red', marker = '.', lw = 0.5)
ax13.plot(elem, mIIF5, color = 'red', marker = '.', lw = 0.5)
ax13.plot(elem, mIIF6, color = 'red', marker = '.', lw = 0.5)
ax13.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax13.axhline(y = 0, color = 'black', lw = 0.5)

ax14.plot(elem, mIIIF1, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, mIIIF2, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, mIIIF3, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, mIIIF4, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, mIIIF5, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, mIIIF6, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, mIIIF7, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, mIIIF8, color = 'red', marker = '.', lw = 0.5)
ax14.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax14.axhline(y = 0, color = 'black', lw = 0.5)

ax15.plot(elem, mIC1, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC2, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC3, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC4, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC5, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC6, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC7, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC8, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC9, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, mIC10, color = 'red', marker = '.', lw = 0.5)
ax15.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax15.axhline(y = 0, color = 'black', lw = 0.5)

ax16.plot(elem, mIIIE1, color = 'red', marker = '.', lw = 0.5)
ax16.plot(elem, mIIIE2, color = 'red', marker = '.', lw = 0.5)
ax16.plot(elem, sirj, color = 'blue', marker = '.', lw = 0.5)
ax16.axhline(y = 0, color = 'black', lw = 0.5)

plt.show()