# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:32:13 2020

@author: mdo
"""

import pylab as plb
from Utilities import utilities 
#Notes:
#the data need to be an array of data 

class Fit_Evaluation():
    def __init__(self):
        self.x_dat = []
        self.y_dat = []
        self.y_val = []
        self.m = 0.0
        self.b = 0.0
        self.main_dat = {}
        
        #self.set_main_data(data)
        self.utility = utilities ()
        
        
    def get_x_dat(self):
        return self.x_dat
    
    def get_y_dat(self):
        return self.y_dat
    
    def get_slope(self):
        return self.m
    
    def get_intercept(self):
        return self.b
    
    def get_y_val(self):
        return self.y_val
    
    def set_main_data(self, data):
        self.main_dat = data
    
    def set_x_data(self,temp_x_dat):
        self.x_dat = temp_x_dat
    
    def set_y_data(self,temp_y_dat):
        self.y_dat = temp_y_dat
        
        
    def fitting_data(self,fit_order):
        print(self.x_dat)
        print(self.y_dat)
        (self.m, self.b) = plb.polyfit(self.x_dat, self.y_dat,fit_order)
    
    def set_linearFit_value(self):
        self.y_val = plb.polyval([self.m,self.b],self.x_dat)
    
    def plotting_scatterPlot(self,x_name, y_name, output_dir, title):
        x_dat = self.get_x_dat()
        y_dat = self.get_y_dat()
        self.utility.genscatterPlot(x_dat,y_dat,x_name,y_name,output_dir,title)
        
    def plotting_linear_fit(self, x_name, y_name, output_dir, title,result):
        x_dat = self.get_x_dat()
        y_dat = self.get_y_dat()
        y_val = self.get_y_val()
        m = self.get_slope()
        b = self.get_intercept()
        self.utility.genlinerPlot(x_dat, y_dat,m,b,y_val,x_name, y_name,output_dir,title,result )
   
    def generating_linear_fit(self, x_name, y_name, ref_name, output_dir):
        #x_name = main_data_process.get_variable_name(main_data_process.get_H2O_index()).strip()
        #y_name = main_data_process.get_variable_name(main_data_process.get_H2CO_index()).strip()
        
        self.set_dat_parameters(x_name, y_name, ref_name, 1)
        self.set_linearFit_value()