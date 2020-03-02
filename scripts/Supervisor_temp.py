# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from DUT_Supervisor import dut_supervisor
from MFC_Supervisor import mfc_supervisor
from REF_Supervisor import ref_supervisor
from fit_data import Fit_Evaluation
from instrCal_Supervisor import InstrCal_file
from Utilities import utilities




class main_supervisor:
    def __init__(self):
        
        
        # declare objects including DUT, MFC and GOLDEN  
        self.DUT = dut_supervisor()
        self.MFC = mfc_supervisor()
        self.REF = ref_supervisor()
        self.UTIL = utilities()
        self.ANALYSIS = Fit_Evaluation()
        self.calFile = InstrCal_file()
        
        # variables
        self.data_length = 10
        self.temp_data = []
        self.DUT_data_clk = False
        self.REF_data_clk = False
        self.Seq_clk = False
        self.if_DUT_ready = False
        self.DUT_state_des = ""
        self.riseCycle = False
        self.fallCycle = False
        self.startingcycleNum = ""
        self.endingcycleNum = ""
        
        
        self.DUT_states_dict = {"1": "MeasBuffer_Check",
                                "2": "CavityPressure_Check",
                                "3": "H2O_Check" ,
                                "4": "data_collecting"
                                }
        
        self.next_action = ""
        self.status_file_path = "R:/crd_G2000/NomadR/For_Energy/4148-NOMADR4079/Standard Tests/Calibration/HP"
        self.next_seq = False
        
        self.set_analysisData_successful = False
        
        
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
    def set_DUT_mode(self,idle_mode,armed_mode):
        self.DUT.set_mode(idle_mode,armed_mode)
    
    def get_DUT_mode(self):
        return self.DUT.get_mode()
    
    def set_DUT_dataCLK_state(self,state):
        self.DUT.set_dataCLK_state(state)
        
    def get_DUT_dataCLK_state(self):        
        return self.DUT.get_current_state()
    
    
    def get_current_DUT_state(self):
        return self.DUT.get_current_state()
    
    def set_DUT_state(self, DUT_state_code, ready_to_next_seq):
        self.DUT.set_state(DUT_state_code, ready_to_next_seq)
    
    def set_DUT_data(self,seqNum,data):
        self.DUT.set_data(seqNum, data)
    
    
    def set_DUT_data_ave(self,data):
        self.DUT.set_data_ave(data)
        
    def get_DUT_data(self):
        return self.DUT.get_data()

    def get_DUT_data_ave(self):
        return self.DUT.get_data_ave()
    
    
    def collect_DUT_data_ave(self,data_length):
        return self.DUT.collect_data(data_length)
    
    def reset_DUT_data_ave(self):
        self.DUT.reset_data_ave()
        
         
    #########################################
    
    
    
    
    
    ############ For MFC ##################
    def set_MFC_seqCLK_state(self,state):
        self.MFC.set_seqCLK_state(state)
        
    def get_MFC_seqCLK_state(self):        
        return self.MFC.get_seqCLK_state()
    
    def seq_countDown(self,interval):
        self.util.stepTime_stopWatch(interval)
    
    def endOF_MFCSeq(self):
        temp_current_seq = int(float(self.get_MFC_seq()))
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
    
    def set_MFC_seq_withSeqNum(self,seqNum):
        self.MFC.set_seq(str(seqNum).strip())
        
        
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
    
   ################## For Data Analysis ####################
    def check_analysis_data(self):
        if self.set_analysisData_successful:
            return True
        else:
            return False
    
    def set_analysis_data(self,ref_data,dut_data):
        try:
            count = 0
            temp_x_data = []
            temp_y_data = []
            #print("test")
            for i in range(0,len(ref_data)):
                count = count + 1
                temp_seq = i + 1
                temp_seq = str(temp_seq)+"."+"0"
                temp_x_data.append(ref_data[temp_seq])
                #print(temp_x_data)
                self.ANALYSIS.set_x_data(temp_x_data)
            
            count = 0
            temp_y_data = []    
            for i in range(0,len(dut_data)):
                count = count + 1
                temp_seq = i + 1
                temp_seq = str(temp_seq)+"."+"0"
                
                temp_y_data.append(dut_data[temp_seq])
                #print(temp_y_data)
                self.ANALYSIS.set_y_data(temp_y_data)
                
            self.set_analysisData_successful = True
            
        except:
            #self.set_analysis_data = False
            print("Can't set data")
            
    def slope_intercept_fit(self):
        self.ANALYSIS.fitting_data(1)
        self.ANALYSIS.set_linearFit_value()

    def get_slope(self):
        return self.ANALYSIS.get_slope()
    
    def get_intercept(self):
        return self.ANALYSIS.get_intercept()
    
    def plot_figure(self,output_dir):
        
    
        self.ANALYSIS.plotting_linear_fit("CH4_Ref","CH4_DUT",output_dir)

        print(self.ANALYSIS.get_slope())
        print(self.ANALYSIS.get_intercept())
        print(self.ANALYSIS.get_y_val())
   
   #########################################################
   
   
   
   ################### InstrCal File ######################
    def set_origin_terms(self,target_file):
        self.calFile.set_origin_terms(target_file)
        #print(self.calFile.get_origin_terms())
        
    def set_proposed_terms(self,temp_mode,temp_slope,temp_intercept):
       
       temp_proposed_term_dic = {}
       temp_original_term = self.calFile.get_origin_terms()
       
       if temp_mode == "idle":
           #print("Test")
           
           for i in temp_original_term:
               if i == "ch4_conc_intercept":
                   temp_original_intercept = temp_original_term[i]
                   temp_intercept = float(temp_original_intercept) - float(temp_intercept)
                   
           temp_proposed_term_dic = {"ch4_conc_slope":temp_slope,"ch4_conc_intercept":temp_intercept}
           #print(temp_proposed_term_dic)
           #self.calFile.set_proposed_terms(temp_proposed_term_dic)
           
       elif temp_mode == "armed":
           for i in temp_original_term:
               if i == "ch4_from_c2h6_conc_intercept":
                   temp_original_intercept = temp_original_term[i]
                   temp_intercept = float(temp_original_intercept) - float(temp_intercept)
                   
           temp_proposed_term_dic = {"ch4_from_c2h6_conc_slope":temp_slope,"ch4_from_c2h6_conc_intercept":temp_intercept}
           
       self.calFile.set_proposed_terms(temp_proposed_term_dic)
   
   
   
    def get_proposed_terms(self):
       return self.calFile.get_proposed_terms()
   
    def generate_proposed_InstCalFile(self):
        
        source_file_name = self.calFile.get_InstrCal_file()
        target_file_name = self.UTIL.get_result_dir()+"/"+ "InstrCal_proposed.ini"
        
        self.set_origin_terms(source_file_name)

        self.set_proposed_terms(self.get_DUT_mode(), self.get_slope(), self.get_intercept())

        proposed_list_term= self.calFile.get_proposed_terms()

        #file_name = "R:/crd_G2000/_Coordinators/NomardR/DEV/calibration/data/20200122/InstrCal.ini"
        
        self.UTIL.write_proposedFile(source_file_name, target_file_name, proposed_list_term)
        self.UTIL.edit_proposeFile(target_file_name)
   ########################################################

    def set_cycle(self):
        if not self.riseCycle and not self.fallCycle:
            
    def set_result_dir(self):
        self.UTIL.set_result_dir()
    
    def get_result_dir (self):
        return self.UTIL.get_result_dir()
    
    def gen_status_file(self):
        target_filePath = self.status_file_path
        seqNum = self.MFC.get_seq()
        data = self.REF.get_data_value(seqNum)
        status = self.REF.get_data_status(seqNum)
        self.UTIL.gen_status_ini(target_filePath, seqNum,data, status)
  
    
    
    def go_next_seq(self,seqNum):
        ref_unit_ready = self.REF.get_data_status(seqNum)
        dut_unit_ready = self.DUT.get_data_status(seqNum)
        
        if ref_unit_ready and dut_unit_ready:
            self.next_seq = True
            return self.next_seq
            #if self.MFC.get_overall_status():
            #    self.next_action == "start data collection"
            #else:
             #   self.next_action = "Start MFC setup"
        else:
            self.next_seq = False
            return self.next_seq
            
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