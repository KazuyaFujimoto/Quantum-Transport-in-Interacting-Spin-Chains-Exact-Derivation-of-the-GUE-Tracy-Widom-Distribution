import matplotlib.pyplot as plt
from matplotlib import rc
import math
import numpy as np
rc('text', usetex=True)


plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 36

fig = plt.figure(figsize=(40,10))
fig.subplots_adjust(hspace=0.2)
ax1 = fig.add_subplot(1, 3, 3)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 1)



### Delta=20 ###
site1, Plmp1 = np.loadtxt("data/delta20/Plmp_200.txt", comments='!', unpack=True)
site2, Plmp2 = np.loadtxt("data/delta20/Plmp_300.txt", comments='!', unpack=True)
site3, Plmp3 = np.loadtxt("data/delta20/Plmp_400.txt", comments='!', unpack=True)
site4, Plmp4 = np.loadtxt("data/delta20/Plmp_500.txt", comments='!', unpack=True)
site5, gue1, gue2, gue3, gue4, gue5, gue6 = np.loadtxt("data/GUE.txt", comments='!', unpack=True)

ax1.text(-6.2,0.5,r"$ ({\rm c})~\Delta=20$")
ax1.set_xlim(-6.5,3.5)
ax1.set_ylim(0.00001,1.2)
ax1.set_yscale('log', base = 10)
ax1.set_xlabel(r"$ (-x + L/2 - 1/2 - t)/(t/2)^{1/3} $",labelpad = 5)
ax1.set_ylabel(r"$ P(x,t)(t/2)^{1/3} $")
ax1.tick_params(axis='y',which='both',left='on',right='on')
ax1.plot( (-site1[::1] + 49.5 - 2.50)/((2.50/2.0)**(1.0/3.0)),Plmp1[::1]*((2.50/2.0)**(1.0/3.0)), color="skyblue",marker='^',fillstyle = 'none',markeredgewidth=2.5,markersize=20.0,alpha=1,linestyle=' ',label=r"${ t=2.50 } $")
ax1.plot( (-site2[::1] + 49.5 - 3.75)/((3.75/2.0)**(1.0/3.0)),Plmp2[::1]*((3.75/2.0)**(1.0/3.0)), color="dodgerblue",marker='s',fillstyle = 'none',markeredgewidth=2.5,markersize=18.0,alpha=1,linestyle=' ',label=r"${ t=3.75 } $")
ax1.plot( (-site3[::1] + 49.5 - 5.00)/((5.00/2.0)**(1.0/3.0)),Plmp3[::1]*((5.00/2.0)**(1.0/3.0)), color="royalblue",marker='p',fillstyle = 'none',markeredgewidth=2.5,markersize=22.0,alpha=1,linestyle=' ',label=r"${ t=5.00 } $")
ax1.plot( (-site4[::1] + 49.5 - 6.25)/((6.25/2.0)**(1.0/3.0)),Plmp4[::1]*((6.25/2.0)**(1.0/3.0)), color="darkmagenta",marker='o',fillstyle = 'none',markeredgewidth=2.5,markersize=20.0,alpha=1,linestyle=' ',label=r"${ t=6.25 } $")
ax1.plot(site5[::1],gue1[::1], color="black",marker='none',fillstyle = 'none',linewidth=2.0,alpha=1.0,linestyle='--',label=r"${ \rm GUE ~Tracy \mathchar`- Widom } $")
ax1.legend(loc='lower center',fancybox=False,fontsize=25,ncol=1,framealpha=0.5)


### Delta=10 ###
site1, Plmp1 = np.loadtxt("data/delta10/Plmp_200.txt", comments='!', unpack=True)
site2, Plmp2 = np.loadtxt("data/delta10/Plmp_300.txt", comments='!', unpack=True)
site3, Plmp3 = np.loadtxt("data/delta10/Plmp_400.txt", comments='!', unpack=True)
site4, Plmp4 = np.loadtxt("data/delta10/Plmp_500.txt", comments='!', unpack=True)
site5, gue1, gue2, gue3, gue4, gue5, gue6 = np.loadtxt("data/GUE.txt", comments='!', unpack=True)

ax2.text(-6.2,0.5,r"$ ({\rm b})~\Delta=10$")
ax2.set_xlim(-6.5,3.5)
ax2.set_ylim(0.00001,1.2)
ax2.set_yscale('log', base = 10)
ax2.set_xlabel(r"$ (-x + L/2 - 1/2 - t)/(t/2)^{1/3} $",labelpad = 5)
ax2.set_ylabel(r"$ P(x,t)(t/2)^{1/3} $")
ax2.tick_params(axis='y',which='both',left='on',right='on')
ax2.plot( (-site1[::1] + 49.5 - 2.50)/((2.50/2.0)**(1.0/3.0)),Plmp1[::1]*((2.50/2.0)**(1.0/3.0)), color="skyblue",marker='^',fillstyle = 'none',markeredgewidth=2.5,markersize=20.0,alpha=1,linestyle=' ',label=r"${ t=2.50 } $")
ax2.plot( (-site2[::1] + 49.5 - 3.75)/((3.75/2.0)**(1.0/3.0)),Plmp2[::1]*((3.75/2.0)**(1.0/3.0)), color="dodgerblue",marker='s',fillstyle = 'none',markeredgewidth=2.5,markersize=18.0,alpha=1,linestyle=' ',label=r"${ t=3.75 } $")
ax2.plot( (-site3[::1] + 49.5 - 5.00)/((5.00/2.0)**(1.0/3.0)),Plmp3[::1]*((5.00/2.0)**(1.0/3.0)), color="royalblue",marker='p',fillstyle = 'none',markeredgewidth=2.5,markersize=22.0,alpha=1,linestyle=' ',label=r"${ t=5.00 } $")
ax2.plot( (-site4[::1] + 49.5 - 6.25)/((6.25/2.0)**(1.0/3.0)),Plmp4[::1]*((6.25/2.0)**(1.0/3.0)), color="darkmagenta",marker='o',fillstyle = 'none',markeredgewidth=2.5,markersize=20.0,alpha=1,linestyle=' ',label=r"${ t=6.25 } $")
ax2.plot(site5[::1],gue1[::1], color="black",marker='none',fillstyle = 'none',linewidth=2.0,alpha=1.0,linestyle='--',label=r"${ \rm GUE~Tracy \mathchar`- Widom } $")
ax2.legend(loc='lower center',fancybox=False,fontsize=25,ncol=1,framealpha=0.5)


### Delta=5 ###
site1, Plmp1 = np.loadtxt("data/delta5/Plmp_200.txt", comments='!', unpack=True)
site2, Plmp2 = np.loadtxt("data/delta5/Plmp_300.txt", comments='!', unpack=True)
site3, Plmp3 = np.loadtxt("data/delta5/Plmp_400.txt", comments='!', unpack=True)
site4, Plmp4 = np.loadtxt("data/delta5/Plmp_500.txt", comments='!', unpack=True)
site5, gue1, gue2, gue3, gue4, gue5, gue6 = np.loadtxt("data/GUE.txt", comments='!', unpack=True)

ax3.text(-6.2,0.5,r"$ ({\rm a})~\Delta=5$")
ax3.set_xlim(-6.5,3.5)
ax3.set_ylim(0.00001,1.2)
ax3.set_yscale('log', base = 10)
ax3.set_xlabel(r"$ (-x + L/2 - 1/2 - t)/(t/2)^{1/3} $",labelpad = 5)
ax3.set_ylabel(r"$ P(x,t)(t/2)^{1/3} $")
ax3.tick_params(axis='y',which='both',left='on',right='on')
ax3.plot( (-site1[::1] + 49.5 - 2.50)/((2.50/2.0)**(1.0/3.0)),Plmp1[::1]*((2.50/2.0)**(1.0/3.0)), color="skyblue",marker='^',fillstyle = 'none',markeredgewidth=2.5,markersize=20.0,alpha=1,linestyle=' ',label=r"${ t=2.50 } $")
ax3.plot( (-site2[::1] + 49.5 - 3.75)/((3.75/2.0)**(1.0/3.0)),Plmp2[::1]*((3.75/2.0)**(1.0/3.0)), color="dodgerblue",marker='s',fillstyle = 'none',markeredgewidth=2.5,markersize=18.0,alpha=1,linestyle=' ',label=r"${ t=3.75 } $")
ax3.plot( (-site3[::1] + 49.5 - 5.00)/((5.00/2.0)**(1.0/3.0)),Plmp3[::1]*((5.00/2.0)**(1.0/3.0)), color="royalblue",marker='p',fillstyle = 'none',markeredgewidth=2.5,markersize=22.0,alpha=1,linestyle=' ',label=r"${ t=5.00 } $")
ax3.plot( (-site4[::1] + 49.5 - 6.25)/((6.25/2.0)**(1.0/3.0)),Plmp4[::1]*((6.25/2.0)**(1.0/3.0)), color="darkmagenta",marker='o',fillstyle = 'none',markeredgewidth=2.5,markersize=20.0,alpha=1,linestyle=' ',label=r"${ t=6.25 } $")
ax3.plot(site5[::1],gue1[::1], color="black",marker='none',fillstyle = 'none',linewidth=2.0,alpha=1.0,linestyle='--',label=r"${ \rm GUE ~Tracy \mathchar`- Widom } $")
ax3.legend(loc='lower center',fancybox=False,fontsize=25,ncol=1,framealpha=0.5)

plt.savefig("fig2.pdf",bbox_inches='tight')

