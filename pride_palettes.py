#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:50:33 2020

@author: cailingallinger
"""

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
#from scipy.interpolate import interp2d

x,y,c = zip(*np.random.rand(300,3)*4-2)

#x0 = np.arange(-5.01, 5.01, 0.25)
#x1 = np.arange(-5.01, 5.01, 0.25)
#xx, yy = np.meshgrid(x0, x1)
#z = np.sin(xx**2+yy**2)

norm=plt.Normalize(0,1) 

def pride():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#760089","#0044ff","#00811f","#ffef00","#ff8c00","#e70000","#784e18","#000000"])

def pride_r():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#000000","#784e18","#e70000","#ff8c00","#ffef00","#00811f","#0044ff","#760089"])

def trans():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#55CDFC","#55CDFC","#F7A8B8","#F7A8B8","#FFFFFF","#FFFFFF"]) 

def trans_r():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#FFFFFF","#FFFFFF","#F7A8B8","#F7A8B8","#55CDFC","#55CDFC"]) 

def bi():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#0000ff","#0000ff","#a349a4","#ff0080","#ff0080"]) #reversed

def bi_r():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#ff0080","#ff0080","#a349a4","#0000ff","#0000ff"]) 

def lesbian():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#D62900","#FF9B55","#FFFFFF","#D461A6","#A50062"])

def lesbian_r():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#A50062","#D461A6","#FFFFFF","#FF9B55","#D62900"])

def gq():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#48821E","#48821E","#FFFFFF","#FFFFFF","#B77FDD","#B77FDD"]) 

def gq_r():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#B77FDD","#B77FDD","#FFFFFF","#FFFFFF","#48821E","#48821E"])

def nb():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#000000","#9C59D1","#FFFFFF","#FFF430"])

def nb_r():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#FFF430","#FFFFFF","#9C59D1","#000000"])

def leather():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#000000","#26297e","#26297e","#000000","#26297e","#26297e","#FFFFFF","#26297e","#26297e","#000000","#e50d3c","#26297e","#000000"])

def leather_r():
    return matplotlib.colors.LinearSegmentedColormap.from_list("", ["#000000","#26297e","#e50d3c","#000000","#26297e","#26297e","#FFFFFF","#26297e","#26297e","#000000","#26297e","#26297e","#000000"])

fig,axs = plt.subplots(2,3,figsize=(12,6))
bi_plot = axs[0,0].scatter(x,y,c=c, cmap=bi(), norm=norm) 
divider = make_axes_locatable(axs[0,0])
cax = divider.append_axes("right", size='5%', pad=0.05, axes_class=plt.Axes)
cbar=plt.colorbar(bi_plot,cax=cax,extend='both',shrink=0.8)

trans_plot = axs[1,0].scatter(x,y,c=c, cmap=trans(), norm=norm) 
divider = make_axes_locatable(axs[1,0])
cax = divider.append_axes("right", size='5%', pad=0.05, axes_class=plt.Axes)
cbar=plt.colorbar(trans_plot,cax=cax,extend='both',shrink=0.8)

gq_plot = axs[0,1].scatter(x,y,c=c, cmap=gq(), norm=norm) 
divider = make_axes_locatable(axs[0,1])
cax = divider.append_axes("right", size='5%', pad=0.05, axes_class=plt.Axes)
cbar=plt.colorbar(gq_plot,cax=cax,extend='both',shrink=0.8)

pride_plot = axs[1,1].scatter(x,y,c=c, cmap=pride(), norm=norm)
divider = make_axes_locatable(axs[1,1])
cax = divider.append_axes("right", size='5%', pad=0.05, axes_class=plt.Axes)
cbar=plt.colorbar(pride_plot,cax=cax,extend='both',shrink=0.8)

lesb_plot = axs[0,2].scatter(x,y,c=c, cmap=lesbian(), norm=norm)
divider = make_axes_locatable(axs[0,2])
cax = divider.append_axes("right", size='5%', pad=0.05, axes_class=plt.Axes)
cbar=plt.colorbar(lesb_plot,cax=cax,extend='both',shrink=0.8)

nb_plot = axs[1,2].scatter(x,y,c=c, cmap=nb(), norm=norm)
divider = make_axes_locatable(axs[1,2])
cax = divider.append_axes("right", size='5%', pad=0.05, axes_class=plt.Axes)
cbar=plt.colorbar(nb_plot,cax=cax,extend='both',shrink=0.8)

fig.subplots_adjust(right=0.94,wspace=0.25,hspace=0.15)
plt.show()


