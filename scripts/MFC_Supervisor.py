# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:02:18 2020

@author: mdo
"""
import string

class mfc_supervisor:
    def __init__(self):
        
        self.seqCLK_state = False
        self.MFC_communication = False
        self.MFC_port = ""
        self.MFC_channels = {"1":[500,"False"], 
                             "2":[500,"False"], 
                             "3":[1000,"False"], 
                             "4":[100,"False"]}
        
        self.MFC_range_check = False
        self.MFC_status = "Unknown"
        
        self.Flow_Sequences = {"0" : [0.0, 0.0 , 425.0 , 0.0],
                               "1" : [0.0, 0.0 , 425.0 , 0.0],
                               "2" : [0.0, 12.0, 413.0 , 0.0],
                               "3" : [0.0, 50.0, 375.0 , 0.0],
                               "4" : [0.0, 100.0, 325.0 , 0.0],
                               "5" : [0.0, 150.0, 275.0 , 0.0],
                               "6" : [0.0, 150.0, 275.0, 0.0],
                               "7" : [0.0, 100.0, 325.0 , 0.0],
                               "8" : [0.0, 50.0, 375.0 , 0.0],
                               "9" : [0.0, 12.0, 413.0 , 0.0],
                               "10" : [0.0, 0.0 , 425.0 , 0.0]}
        
        self.current_flow_seq = "0"
    
    
    def set_seqCLK_state(self,state):
        state = string.lower(state)
        if state == "high":
            self.seqCLK_state = True
        elif state == "low":
            self.seqCLK_state = False
            
    def get_seqCLK_state(self):
        return self.seqCLK_state
    
    
    def get_flow_sequences(self):
        return self.Flow_Sequences
        
    def get_overall_status(self):
        if self.MFC_status == "Active":
            return True
        else:
            return False
        
    def set_COMPort(self,MFC_port):
        self.MFC_port = MFC_port
    
    def get_COMPort(self):
        return self.MFC_port
    
    def set_channel_status(self,channelRange_list):
        index = 1
        MFC_range_check_count = 0
        for i in channelRange_list:
            if i == str(self.MFC_channels[str(index)][0]):
                self.MFC_channels[str(index)][1]="True"
                MFC_range_check_count = MFC_range_check_count + 1
            index = index + 1
        #print(MFC_range_check_count)
        if MFC_range_check_count == 4:
            
            self.MFC_range_check = True
            self.MFC_status = "Active"
    
      
    def get_channel_range(self,channel):
        return self.MFC_channels[str(channel)][0]
    
    def get_channel_status(self,channel):
        return self.MFC_channels[str(channel)][1]
    
    
    def set_seq(self, seq_Num):
        self.current_flow_seq = seq_Num
    
    def get_seq(self):
        return self.current_flow_seq
    
        
    def get_seq_value(self,seq_Num):
        seq_Num = str(seq_Num)   
        return self.Flow_Sequences[seq_Num]
        
        
    def show_content(self):
        for i in self.MFC_channels:
            print("Channel %s"%i)
            print("Range : %s"%self.MFC_channels[i][0])
            print("Status : %s"%self.MFC_channels[i][1])
            
            
                