#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:23:28 2023

@author: felix
"""

import matplotlib.pyplot as plt
import numpy as np
import uncertainties as un
import uncertainties.unumpy as unp
import scipy 
import scipy.odr as odr


class fit:
    
    def __init__(self, func, xdata, ydata, guess, identifier="fit"):
        self.func = func
        self.xdata = xdata
        self.ydata = ydata
        self.guess = guess
        self.identifier = identifier
        
        self.datacolour = "rebeccapurple"
        self.fitcolour = "cornflowerblue"
        
        
    
    def odr_fit(self):
        
        model = odr.Model(self.func)
        mydata = odr.RealData(unp.nominal_values(self.xdata),unp.nominal_values(self.ydata),unp.std_devs(self.xdata),unp.std_devs(self.ydata))
        myodr = odr.ODR(mydata, model, beta0=self.guess)
        out = myodr.run()
        
        errors = [np.sqrt(out.cov_beta[ii,ii]) for ii in range(len(out.beta))]
        
        self.out = out
        
        return unp.uarray(out.beta, errors)


        #pxspace = np.linspace(0,4,1000)
        #plt.plot(pxspace,fitfunc(out.beta,pxspace),label="fit")

        #plt.xlabel(r"$P_{RF}$ in W")
        #plt.ylabel(r"$\epsilon$")
        #plt.legend()
        #plt.xlim(0.3,2.1)
        #plt.savefig("EoverPRF.pdf",dpi = 300)
        
        
    def print(self):
        
        print("\n printing beta for \"" , self.identifier, "\" : ", self.beta, "\n")
        
    def pprint(self):
        
        self.out.pprint()
    
        

    def run(self, method=0):
        
        self.method = method
        if(self.method==0):
            self.beta = self.odr_fit()
        
    
    def calcBoundaries(self, xdata, ydata):
        
        xmin = xdata[0].nominal_value-xdata[0].std_dev
        xmax = xdata[0].nominal_value+xdata[0].std_dev
        for cc in range(len(unp.nominal_values(xdata))):
            if(xdata[cc].nominal_value-xdata[cc].std_dev < xmin):
                xmin = xdata[cc].nominal_value-xdata[cc].std_dev
            if(xdata[cc].nominal_value+xdata[cc].std_dev > xmax):
                xmax = xdata[cc].nominal_value+xdata[cc].std_dev
        
        x1, x2 = xmin-(xmax-xmin)/10,xmax+(xmax-xmin)/10
        
        return x1,x2
    
    def plot(self, xlabel = None, ylabel = None):
        
        plt.close()
        plt.errorbar(x = unp.nominal_values(xdata), y = unp.nominal_values(ydata),
                     xerr = unp.std_devs(xdata) , yerr = unp.std_devs(ydata),
                     fmt = '.', capsize = 3, label = 'datapoints', color = self.datacolour)
        
        xmin,xmax = self.calcBoundaries(xdata,ydata)
        
        xspace = np.linspace(xmin,xmax,1000)
        yspace = [self.func(unp.nominal_values(self.beta),xx) for xx in xspace]
        plt.plot(xspace,yspace, label = 'fit', color = self.fitcolour)
        plt.xlim(xmin, xmax)
        
        if(xlabel!=None):
            plt.xlabel(xlabel)
            
        if(ylabel!=None):
            plt.ylabel(ylabel)
        
        plt.legend()
        
            
            
        
    








xdata = unp.uarray([1,2,3,4],[0.1]*4)
ydata = unp.uarray([1/2,1,3/2,2],[0.1]*4)

def fit_func(beta,x):
    return beta[0]*x

guess = [0.5]

fit = fit(fit_func, xdata, ydata, guess, identifier="linear")
fit.run()
fit.print()
fit.pprint()
fit.plot(xlabel = "hello", ylabel = "world")

























