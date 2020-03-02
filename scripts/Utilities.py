# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:20:07 2020

@author: mdo
"""

import time
import timeit

from configobj import ConfigObj

import os
import matplotlib.pyplot as plt
from pylab import figure, savefig
from matplotlib.patches import Rectangle
from os.path import join

class utilities:
    def __init__(self):
        self.stepTime = 3
        self.output_dir=""
    
    
    def get_currentTime(self):
        return time.strftime('%Y%m%d_%H%M%S')
    
    def get_result_dir(self):
        return self.output_dir
    
    def set_result_dir(self):
        outputDir = 'C:/Picarro/G2000/Addon'
        timeStr = time.strftime('%Y%m%d_%H%M%S')
        
        
        
        test_result_output_dir = "%s"%outputDir + "/" + "CH4_C2H6_Calibration" + "/"+ "%s"%timeStr
        
        
        try:
            temp_str = test_result_output_dir.split("/")
            temp_ouput_dir = "%s"%outputDir + "/" + temp_str[4]
                                    
            if not os.path.exists(temp_ouput_dir):
                os.makedirs(temp_ouput_dir)
                if not os.path.exists(test_result_output_dir):
                    os.makedirs(test_result_output_dir)
                    self.output_dir = test_result_output_dir
                else:
                    self.output_dir = test_result_output_dir
            else:
                if not os.path.exists(test_result_output_dir):
                    os.makedirs(test_result_output_dir)
                    self.output_dir = test_result_output_dir
                else:
                    self.output_dir = test_result_output_dir
        except:
            print("Cannot set test result output directory\n")
            
    def stepTime_stopWatch(self,interval):
        count = 0
        while count < self.interval:
            count = count + 1
            time.sleep(1)
        
            
    def H2O_is_DRY(self,h2o_conc):
        temp = h2o_conc[int(-0.50*len(h2o_conc)):]
        print(temp)
        current_average_H2O = 	sum(temp)/len(temp)
        print(current_average_H2O)
        if  current_average_H2O < 0.1:
            return True
        else:
			return False
    
    
    def genscatterPlot(self,x,y,x_name,y_name,output_dir,title):
        if not os.path.exists(output_dir):
            print("output directory : %s"%self.output_dir + "is empty or is not exist")
        else:
            
           # outputDir = output_dir
            
            figure()
            timeStr = time.strftime('%Y%m%d_%H%M%S')
            
            #yp = self.fit_value(x,m,b)
            #textstr = "slope = %f"%m + "\n Intercept = %f"%b
            plt.scatter(x,y)
            #plt.plot(x,y,marker='o',markersize=0.7)
            #plt.plot(x,yp,'r-')
                        
            #extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
            #plt.legend([extra,extra],['Slope : %s'%m,'Intercept : %s'%b],loc="best")
            
            plt.title("LinearFit - "  + title)
            
            #if x_name.strip() == "H2O":
            #    plt.xlabel("H2O - %", color = 'black', fontweight = 'bold')
            #elif x_name.strip() == "CH4":
            #    plt.xlabel("CH4 - ppm", color = 'black', fontweight = 'bold')
            #plt.ylabel("H2CO - ppb", color = 'black', fontweight = 'bold')
            
            plt.xlabel("CH4(ppm) , " + x_name , color = 'black', fontweight = 'bold')
            plt.ylabel("CH4(ppm) , " + y_name, color = 'black', fontweight = 'bold')
            savefig((join(output_dir, y_name.strip() + '_' + x_name.strip() + 'scatterPlot' + timeStr + '.png')))
            
            
            plt.show()
            
    def genlinerPlot(self,x,y,m,b,yp,x_name,y_name,output_dir,title,result):
        
        if not os.path.exists(output_dir):
            print("output directory : %s"%self.output_dir + "is empty or is not exist")
        else:
            
           # outputDir = output_dir
            
            figure()
            timeStr = time.strftime('%Y%m%d_%H%M%S')
            
            #yp = self.fit_value(x,m,b)
            #textstr = "slope = %f"%m + "\n Intercept = %f"%b
            plt.scatter(x,y)
            plt.plot(x,yp,'r-')
                        
            extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
            plt.legend([extra,extra],['Slope : %s'%m,'Intercept : %s'%b],loc="best")
            
            plt.title("LinearFit - "  + title)
            
            #if x_name.strip() == "H2O":
            #    plt.xlabel("H2O - %", color = 'black', fontweight = 'bold')
            #elif x_name.strip() == "CH4":
            #    plt.xlabel("CH4 - ppm", color = 'black', fontweight = 'bold')
            #plt.ylabel("H2CO - ppb", color = 'black', fontweight = 'bold')
            x_pos = 5
            y_pos = 8
            plt.text(x_pos,y_pos,result)
            plt.xlabel("CH4(ppm) , " + x_name , color = 'black', fontweight = 'bold')
            plt.ylabel("CH4(ppm) , " + y_name, color = 'black', fontweight = 'bold')
            savefig((join(output_dir, y_name.strip() + '_' + x_name.strip() + '_linearFit' + timeStr + '.png')))
            
            
            plt.show()

    def gen_result_ini(self, target_file_path,x_name,y_name,slope,intercept,startTime, endTime,totalTime,startDate,endDate,title,result):
        if title == "High Precision":
            target_file_path = target_file_path+"/"+"HighPrecisionMode_FitResults.ini"
        elif title == "High Range":
            target_file_path = target_file_path+"/"+"HighRangeMode_FitResults.ini"
        else:
            target_file_path = target_file_path+"/"+"FitResults.ini"
        
        
        if not os.path.exists(target_file_path):
            config = ConfigObj()
            config.filename = target_file_path.split("/")[-1]
            testResult = "Test Result %s_on_%s" %(x_name,y_name)
            timeOverall  = "Test Time Overall"
            operationSpec = "Operation Spec"
            termResult = "Terms Result"
            config[testResult] = {"Test Result":result}
            config[operationSpec]={"Mode":title}
            config[termResult] = {"slope":slope,"Intercept":intercept}
            config[timeOverall] = { "B":startTime,"E":endTime,"H":totalTime[0],
                                     "M":totalTime[1],"S":totalTime[2],"SDate":startDate,"EDate":endDate}
                
            with open(target_file_path,'w') as f:
                config.write(f)
        else:
            config = ConfigObj(target_file_path)
            result_name = "%s_on_%s" %(x_name,y_name)
            timeOverall  = "Test Time Overall"
            operationSpec = "Operation Spec"
            testResult = "Test Result"
            config[testResult] = {"Test Result":result}
            config[operationSpec]={"Mode":title}
            config[result_name] = {"slope":slope,"Intercept":intercept}
            config[timeOverall] = {"B":startTime,"E":endTime,"H":totalTime[0],
                                     "M":totalTime[1],"S":totalTime[2],"SDate":startDate,"EDate":endDate}
            with open(target_file_path,'w') as f:
                config.write(f)
    
    
    #
    def write_proposedFile(self, source_file_path, target_file_path, proposed_list_term):
        timeStr = time.strftime('%Y%m%d_%H%M%S')
        with open(source_file_path) as oldFile:
            with open(target_file_path,'w') as proposedFile:
                for line in oldFile:
                    line = self.get_only_OPTION_CHAR(line)
                    for item in line:
                        if item not in proposed_list_term:
                            proposedFile.write(item+ " = " + str(line[item]) + "\n")
                        else:
                            
                            line[item] = self.remove_comments(line[item])
                            proposedFile.write(item + " = " + str(proposed_list_term[item]))
                            proposedFile.write("\t\t# " + "%s " %timeStr + "change from %s" %line[item] + " to %s" %proposed_list_term[item] + " (MD)" + "\n")           
    
    
    def edit_proposeFile(self,target_file_path):
        config = ConfigObj()
        config.filename = target_file_path.split("/")[-1]
        timeStr = time.strftime('%Y%m%d_%H%M%S')
        config["other"] = {}
        config["CH4"] = {}
        config["CH4_from_C2H6"] = {}
        config["Notes"] = {"Revise Date":timeStr}
        with open(target_file_path,'r') as f:
            for line in f:
                temp_dic = self.get_only_OPTION_CHAR(line)
                for i in temp_dic:
                    if "ch4_conc_slope" in i:
                        config["CH4"][i] = temp_dic[i]
                    elif "ch4_conc_intercept" in i:
                        config["CH4"][i] = temp_dic[i]
                    elif "ch4_from_c2h6_conc_slope" in i:
                        config["CH4_from_C2H6"][i] = temp_dic[i]
                    elif "ch4_from_c2h6_conc_intercept" in i:
                        config["CH4_from_C2H6"][i] = temp_dic[i]
                    else:
                        config["other"][i] = temp_dic[i]
        #config.write()
        with open(target_file_path,'w') as f:
            f.write("[Data]\n")
            for section_name in config.keys():
                f.write("\n#%s"%section_name + "\n")
               
                for i in config[section_name]:
                    if section_name == "Notes":
                        f.write("#%s : %s"%(i,config[section_name][i]+"\n"))
                    else:
                        f.write("%s = %s"%(i,config[section_name][i].strip("\'")) + "\n")        
    
    def remove_comments(self,line):
        COMMENT_CHAR = "#"
        if COMMENT_CHAR in line:
            value, comment = line.split(COMMENT_CHAR,1)
            new_line = value.strip()
            return new_line
        else:
            return line
    
    def get_only_OPTION_CHAR(self, line):
    
        OPTION_CHAR = '='
        
        options = {}
        
       
            #Second, find lines with an option=vale:
        if OPTION_CHAR in line:
            # split on option char:
            option, value = line.split(OPTION_CHAR,1)
            
            #strip spaces:
            option = option.strip()
            value = value.strip()
            
            #store in dictionary:
            options[option] = value
        
        return options
    
    def set_timer(self):
        return timeit.default_timer()
    def end_timer(self):
        return timeit.default_timer()
    
    def set_today(self):
        return time.strftime('%Y'+'/'+'%m'+'/'+'%d')
    def set_realTime(self):
        return time.strftime('%H'+':'+'%M'+':'+'%S')
    
    def get_total_time(self,startTime,endTime):
        print(startTime)
        print(endTime)
        total_time = endTime - startTime
        print(total_time)
        mins,secs = divmod(total_time,60)
        hours, mins = divmod(mins,60)
        
        return(hours,mins,secs)