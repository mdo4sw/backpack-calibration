# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:44:45 2020

@author: mdo
"""
from configobj import ConfigObj
import os

class InstrCal_file():
    def __init__(self):
        self.origin_term_dic={}
        self.file_exist = False
        self.proposed_term_dic = {}
        self.InstrCal_file_path = 'C://Picarro//G2000//InstrConfig//Calibration//InstrCal'
        self.InstrCal_file_name = 'InstrCal.ini'
        
    def get_InstrCal_file(self):
        return self.InstrCal_file_path + "/" + self.InstrCal_file_name
    
    def set_origin_terms(self,target_file_path):
        if os.path.exists(target_file_path):
            self.file_exist = True
            #print("TESTTTTT")
            config = ConfigObj(target_file_path)
            config.filename = target_file_path.split("/")[-1]
            for i in config.keys():
                if i == 'Data':
                    self.origin_term_dic = config['Data']
        else:
            self.file_exist = False

    def get_origin_terms(self):
        return self.origin_term_dic
    
    def set_proposed_terms(self,temp_proposed_term_dic):
        self.proposed_term_dic = temp_proposed_term_dic
        #print("TEEST")
        #print(temp_proposed_term_dic)
        
        #for i in temp_proposed_term_dic:
        #    if i in self.proposed_term_dic:
        #        self.proposed_term_dic[i] = temp_proposed_term_dic[i]
        #print(self.proposed_term_dic)
        
    def get_proposed_terms(self):
        return self.proposed_term_dic
    




