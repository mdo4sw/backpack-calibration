# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from DUT_Supervisor import dut_supervisor
from MFC_Supervisor import mfc_supervisor
from REF_Supervisor import ref_supervisor

from Utilities import utilities



class main_supervisor:
    def __init__(self):
        
        
        # declare objects including DUT, MFC and GOLDEN  
        self.DUT = dut_supervisor()
        self.MFC = mfc_supervisor()
        self.REF = ref_supervisor()
        self.UTIL = utilities()
        
        
        # variables
        self.DUT_data_clk = False
        self.REF_data_clk = False
        self.Seq_clk = False
        self.if_DUT_ready = False
        self.DUT_state_des = ""
        self.DUT_states_dict = {"1": "MeasBuffer_Check",
                                "2": "CavityPressure_Check",
                                "3": "H2O_Check" ,
                                "4": "data_collecting"
                                }
        self.next_Action = ""
        
        
        
    ############ For GOLDEN unit ############
    def set_REF_dataCLK_state(self):
        if self.get_REF_H2O_state() == "wet":
            self.REF.set_dataCLK_state("low")
        elif self.get_REF_H2O_state() == "dry":
            self.REF.set_dataCLK_state("high")
            
        
    def get_REF_dataCLK_state(self):        
        return self.REF.get_dataCLK_state()
    
    
    def set_REF_H2O_state(self,conc):
        if(self.UTIL.H2O_is_DRY(conc)):
            self.REF.set_H2O_status("dry")
        else:
            self.REF.set_H2O_status("wet")
    
    def get_REF_H2O_state(self):
        return self.REF.get_H2O_status()
    


    def set_REF_data(self,seqNum,data):
        self.REF.set_data(seqNum, data)
    def get_REF_data(self):
        return self.REF.get_data()
    
    ########################################
    
    
    
    
    
    ########### For DUT unit ###############
    def set_DUT_dataCLK_state(self,state):
        self.DUT.set_dataCLK_state(state)
        
    def get_DUT_dataCLK_state(self):        
        return self.DUT.get_current_state()
    
    
    def get_current_DUT_state(self):
        return self.dut.get_current_state()
    
    def set_DUT_state(self, DUT_state_code):
        self.dut.set_state(DUT_state_code)
    
    def set_DUT_data(self,seqNum,data):
        self.REF.set_data(seqNum, data)
    def get_DUT_data(self):
        return self.REF.get_data()          
    #########################################
    
    
    
    
    
    ############ For MFC ##################
    def set_MFC_seqCLK_state(self,state):
        self.MFC.set_seqCLK_state(state)
        
    def get_MFC_seqCLK_state(self):        
        return self.MFC.get_seqCLK_state()
    
    def seq_countDown(self,interval):
        self.util.stepTime_stopWatch(interval)
    
    def endOF_MFCSeq(self):
        temp_current_seq = int(self.get_MFC_seq())
        max_seqNum = len(self.MFC.get_flow_sequences())-1
        #print(temp_current_seq)
        #print(max_seqNum)
        if temp_current_seq == max_seqNum:
            
            return True
        else:
            
            return False
    
    def get_MFC_seq_value(self,seqNum):
        return self.MFC.get_seq_value(seqNum)
    
    def set_MFC_seq(self):
        temp_current_seq = int(self.get_MFC_seq())
        max_seqNum = len(self.MFC.get_flow_sequences())-1
        if temp_current_seq != max_seqNum:
            temp_current_seq = temp_current_seq + 1
            self.MFC.set_seq(str(temp_current_seq))
            return 1 # this mean the current seq is not at the end, so increase to the next seq
        else:
            return 0 # this mean the seq is at the end, can't increase to the next seq
        
    def get_MFC_seq(self):
        return self.MFC.get_seq()            
        
    def set_MFC_status(self,channel_rangeList):
        temp_list = []
        for i in channel_rangeList:
            temp_list.append(str(i).strip())
        self.MFC.set_channel_status(temp_list)
        
    def get_MFC_channel(self,channel):
        return self.MFC.get_channel_range(channel)
        
    
    def get_MFC_channel_status(self,channel):
        return self.MFC.get_channel_status(channel)
    
    def if_MFC_ready(self):
        return self.MFC.get_overall_status()
        
    def set_MFC_COMport(self,MFC_port):
        self.MFC.set_COMPort(MFC_port)
    
    def get_MFC_COMport(self):
        return self.MFC.get_COMPort()
        
        
   #########################################################
            
  
    def get_next_action(self):
        return self.next_action
    
    def set_next_action(self):
        if self.dut.ready_to_measure():
            if self.MFC.get_overall_status():
                self.next_action == "start data collection"
            else:
                self.next_action = "Start MFC setup"
        else:
            self.next_action = "Idle"
            
            
    def idle_5seconds(self):
        count = 0
        while count < 5:
            count = count + 1
            #print(count)
        #print("end count")    
    def idle_seconds(self,numberofSecond):
        count = 0
        while count < numberofSecond:
            count = count + 1
            #print(count)