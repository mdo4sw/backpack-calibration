# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:26:21 2020

@author: mdo
"""
import string


class ref_supervisor:
    def __init__(self):
        
        self.dataCLK_state = ""
        
        self.current_H2O_state = "unknown"
        self.data = {"1.0":[0.0,False],
                     "2.0":[0.0,False],
                     "3.0":[0.0,False],
                     "4.0":[0.0,False],
                     "5.0":[0.0,False],
                     "6.0":[0.0,False],
                     "7.0":[0.0,False],
                     "8.0":[0.0,False],
                     "9.0":[0.0,False],
                     "10.0":[0.0,False]}
                     
        self.instrumentName = ""
    
    def set_instrumentName(self,instrumentName):
        self.instrumentName = instrumentName
        
    def get_instrumentName(self):
        return self.instrumentName
    
    def set_data(self,seqNum,data):
        self.data[seqNum][0] = data
        self.data[seqNum][1] = True
        
    def get_data_status(self,seqNum):
        return self.data[seqNum][1]
    
    def get_data_value(self,seqNum):
        return self.data[seqNum][0]
    
    def get_data(self):
        temp_data = {}
        for i in self.data:
            temp_data[i]= self.data[i][0]
            
        return temp_data
        
    def set_dataCLK_state(self,state):
        state = string.lower(state)
        if state == "high":
            self.dataCLK_state = "high"
        elif state == "low":
            self.dataCLK_state = "low"
            
    def get_dataCLK_state (self):        
        return self.dataCLK_state
    
    def set_currentH2O_conc(self,conc):
        self.current_H2O_conc = conc
    
    def get_currentH2O_conc(self):
        return self.current_H2O_conc
    
    def set_H2O_status(self,state):
        self.current_H2O_state = state
    
    def get_H2O_status(self):
        return self.current_H2O_state
        
        