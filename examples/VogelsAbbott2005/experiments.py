#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
    

def create_experiments(model):
    
    return  [
                           #Lets kick the network up into activation
                           PoissonNetworkKick(model,duration=80*7,drive_period=8*7.0,sheet_list=["Exc_Layer","Inh_Layer"],stimulation_configuration={'component' : 'mozaik.sheets.population_selector.RCRandomPercentage','params' : {'percentage' : 20.0}},lambda_list=[100.0,100.0],weight_list=[0.02, 0.02]),
                           #Spontaneous Activity 
                           #PoissonNetworkKick(model,duration=80*7,drive_period=8*7.0,sheet_list=["Exc_Layer","Inh_Layer"],stimulation_configuration={'component' : 'mozaik.sheets.population_selector.RCRandomPercentage','params' : {'percentage' : 0.0}},lambda_list=[0.0,0.0],weight_list=[0.0, 0.0]),
                           
                           #NoStimulation(model,duration=135.0*2),
            ]
