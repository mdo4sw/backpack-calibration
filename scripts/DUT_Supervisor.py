# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:57:18 2020

@author: mdo
"""
import string

class dut_supervisor:
    def __init__(self):
        self.mode = ""
        self.if_DUT_ready_next_seq = False
        self.DUT_state_des = ""
        self.DUT_states_dict = {"1": "MeasBuffer_Check",
                                "2": "CavityPressure_Check",
                                "3": "H2O_Check" ,
                                "4": "Initiating_measurement",
                                "5": "DataAve"
                                }
        self.temp_data = []
        
        self.instrumentName = ""
        
        self.dataCLK_state = False
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
        
    def set_instrumentName(self,instrumentName):
        self.instrumentName = instrumentName
        
    def get_instrumentName(self):
        return self.instrumentName
    
    def set_mode(self,idle_mode, armed_mode):
        if idle_mode:
            self.mode = "idle"
        elif armed_mode:
            self.mode = "armed"
        else:
            self.mode = "unknown"
    
    def get_mode(self):
        return self.mode
    
        
    def set_data(self,seqNum,data):
        if self.data[seqNum][0] == 0.0:
            self.data[seqNum][0] = data
            self.data[seqNum][1] = True
        else:
            temp_ave_data = (self.data[seqNum][0] + data)/2
            self.data[seqNum][0] = temp_ave_data
            self.data[seqNum][1] = True
        
        
    def get_data_status(self,seqNum):
        return self.data[seqNum][1]
    
    #return dictionary 
    def get_data(self):
        temp_data = {}
        for i in self.data:
            temp_data[i]= self.data[i][0]
        return temp_data
    
    def set_dataCLK_state(self, state):
        state = string.lower(state)
        if state == "high":
            self.dataCLK_state = True
        elif state == "low":
            self.datCLK_state = False
            
    def get_data_clk_state(self):
        return self.dataCLK_state 
    
    
    def states_lookup(self, DUT_state):
        temp_state_code = str(DUT_state)
        for i in self.DUT_states_dict:
            #print(i)
            #print(self.DUT_states_dict[i])
            if temp_state_code == i:
                return True
        print("Can't match current DUT state to the record")
        return False
                
            
    def get_current_state(self):
        return self.DUT_state_des
    
   
    
    def set_state(self, DUT_state_code,ready_to_next_seq):
        temp_state = str(DUT_state_code).strip()
        #self.DUT_state_des = temp_DUT_state
        if str(ready_to_next_seq) == "1":
            self.ready_to_next_seq = True
        else:
            self.ready_to_next_seq = False
            
        if self.states_lookup(temp_state):
            self.DUT_state_des = (self.DUT_states_dict[temp_state])
        else:
            print("Can't set current DUT state")
                
                    
    def ready_to_next_seq(self):        
        return self.ready_to_next_seq

        
    def ready_to_measure(self):
        temp_current_state = self.get_current_state()
        if temp_current_state == "Initiating_measurement":
            return True
        else:
            return False
    
    def ready_to_getData(self):
        temp_current_state = self.get_current_state()
        if temp_current_state == "DataAve":
            return True
        else:
            return False
    def reset_data_ave(self):
        self.temp_data = []
        
    def set_data_ave(self,data):
        self.temp_data.append(data)
        print(self.temp_data)
        
    def get_data_ave(self):
        return sum(self.temp_data)/len(self.temp_data)
        
    def collect_data(self,data_length):
        if len(self.temp_data) < data_length:
            print(len(self.temp_data))
            return True
        else:
            return False
        
    