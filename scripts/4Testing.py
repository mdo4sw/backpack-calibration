# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:23:25 2020

@author: mdo
"""
from Supervisor import main_supervisor
from MFC_Supervisor import mfc_supervisor
from fit_data import Fit_Evaluation

from Utilities import utilities
import time

## the followin is to test MFC_Supervisor 
'''
main = mfc_supervisor()

a = ["500","500","1000","100"]
main.set_channel_status(a)
for i in range(1,5):
    print(main.get_channel_range(str(i)), main.get_channel_status(str(i)))

print(main.get_overall_status())
'''
### the following is to test Supervisor
 
main = main_supervisor()
#main.set_DUT_state(2)
#print(main.get_current_DUT_state())
current_H2O = [0.3, 0.2, 0.3, 0.1, 0.08]
count = 0

diff = 0
'''  
for i in range(0,len(main.get_DUT_data())-1):
    
    while main.collect_DUT_data_ave(10):
        temp = i + count
        
        diff = diff + 0.005
        count = count + diff
        print(temp)
        main.set_DUT_data_ave(temp)
        time.sleep(1)
        
    temp_ave = main.get_DUT_data_ave()   
    print(temp_ave)
    temp_seq = i + 1
    temp_seq = str(temp_seq)+"."+"0"
    print(count)
    main.set_DUT_data(temp_seq,temp_ave)
    main.reset_DUT_data_ave()
    

count = 0

for i in range(0,len(main.get_REF_data())-1):
    count = count + 1
    temp_seq = i + 1
    temp_seq = str(temp_seq)+"."+"0"
    main.set_REF_data(temp_seq,count)
'''   
#main.set_REF_H2O_state(current_H2O)
#print(main.get_REF_H2O_state())
#aveVal = 3.3

#while not main.go_next_seq(main.get_MFC_seq()):
    
#    main.set_DUT_state(2,1)
    #tem_state = main.get_current_DUT_state()
#    print("Current State : %s\n"%tem_state)
    #mainSUP.set_next_action()
    #logFunc("Next action :%s\n"%mainSUP.get_next_action())
#    main.set_DUT_data(main.get_MFC_seq(),aveVal)
        
            
#print(main.DUT_read_to_measure())
'''
main.set_next_action()

print(main.get_next_action())

while main.get_next_action() == "Idle":
    main.idle_seconds(15)
    main.set_DUT_state("4")
    main.set_next_action()

print(main.get_next_action())

#check if seq is at the end

while True:
    if(main.endOF_MFCSeq()):
        print("End of seq\n")
        break
    else:
        main.set_MFC_seq()
        temp_current_seq = main.get_MFC_seq()
        print("Current seq : %s\n"%main.get_MFC_seq())
        print("Set the seq to %s\n"%main.get_MFC_seq_value(temp_current_seq))
        main.seq_countDown()
    
''' 
'''   
main.set_DUT_mode(True,False)
main.set_DUT_name("6162-NOMADR4084")
main.set_REF_name("6166-FDD1010")
print(main.get_REF_data())
print(main.get_DUT_data()) 
output_dir = "R:/crd_G2000/_Coordinators/NomardR/DEV/calibration/data/20200122"
main.set_analysis_data(main.get_REF_data(),main.get_DUT_data())
print(main.check_analysis_data())

if main.check_analysis_data():
    main.slope_intercept_fit()
    main.plot_figure(output_dir)
    print(main.ANALYSIS.get_slope())
    print(main.ANALYSIS.get_intercept())
    
else:
    print("Can't set data")


print(main.get_DUT_mode())
print(main.ANALYSIS.get_slope())
print(main.ANALYSIS.get_intercept())
'''

####### instcal file ############
#file_name = "R:/crd_G2000/_Coordinators/NomardR/DEV/calibration/data/20200206/InstrCal.ini"
#main.generate_proposed_InstCalFile()
#print(proposed_list_term)
#main.UTIL.gen_result_ini(output_dir,main.REF.get_instrumentName(),main.DUT.get_instrumentName(),main.ANALYSIS.get_slope(),main.ANALYSIS.get_intercept())


#target_file_name = "R:/crd_G2000/_Coordinators/NomardR/DEV/calibration/data/20200206/InstrCal_proposed.ini"

#proposed_list_term={"ch4_conc_slope": 9.0,"ch4_conc_intercept" : 9.0,
#                    "ch4_from_c2h6_conc_slope":9.0,"ch4_from_c2h6_conc_intercept":9.0}

#utl.write_proposedFile(file_name,target_file_name,proposed_list_term)
#utl.edit_proposeFile(target_file_name)

target_file_path = "R://crd_G2000//_Coordinators//NomardR//DEV//calibration//data//20200220"

main.set_startTime()
time.sleep(5)
main.set_endTime()

startTime = main.get_realstartTime()
endTime = main.get_realendTime()
print(startTime)
print(endTime)
totalTime = main.get_totalTime()

today= main.UTIL.get_today()
title = "High Range"
result = "PASS"
main.UTIL.gen_result_ini(target_file_path,"CH4_REF","CH4_DUT","1.0","1.2",startTime,endTime,totalTime,today,title,result)
    
    
    
    
    
    
    
    