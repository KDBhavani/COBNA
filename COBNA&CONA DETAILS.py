# -*- coding: utf-8 -*-
"""
Created on Sun May 15 01:11:05 2022

@author: sys
"""
import json
import os

cona_matched_data=[]
cobna_matched_data=[]
cona_cobna_matched_data=[]
dummy_cobna_matched_data=[]
dummy_cona_matched_data=[]
parent_matched_data=[]
BU_merged_to_21100_matched_data =[]
BU_move_to_sub_of_21100_matched_data=[]
sub_of_11015_matched_data=[]
BU_move_to_sub_of_21100_matched_data =[]
BU_move_to_sub_of_21100_matched_data =[]
BU_merged_to_21100_matched_data=[]
BU_move_to_sub_of_21100_matched_data=[]
BU_move_to_sub_of_21100_matched_data=[]
BU_move_to_sub_of_21100_becomes_parent_of_11120_matched_data=[]
BU_move_to_sub_of_21100_matched_data=[]
Minority_Owner_of_11020_and_11080_matched_data=[]
BU_merged_to_21100_matched_data=[]
COFC_Elim_matched_data=[]
CONA_Consol_Elim_matched_data=[]
COBNA_Consol_Elim_only_YTD_NI_to_remain_matched_data=[]
Move_to_new_COGC_CONSOL_node_matched_data=[]
COFC_US_Elim_matched_data=[]
CONA_US_Elim_matched_data=[]
COBNA_US_Elim_only_YTD_NI_to_remain_matched_data=[]
COFC_NonUS_Elim_matched_data=[]
COBNA_Non_US_Elim_should_zero_out_matched_data=[]
NonUS_Elim_Cap1_Global_Corp_should_zero_out_matched_data=[]
NonUS_Elim_Cap_one_Holdings_should_zero_out_matched_data=[]
NonUS_Elim_COBEP_HFS_should_zero_out_matched_data=[]
BU_move_to_CONA_for_consolidation_matched_data=[]
BU_to_be_dissolved_pre_LEGO_matched_data=[]
BU_to_be_dissolved_pre_LEGO_matched_data=[]
BU_moved_to_sub_of_11105_matched_data=[]
IC_loan_with_11110_to_be_terminated_matched_data=[]
cona_cobna_lst=["21100","11000"]
BU_LST=["10000","11000","11015","11016","11020","11051","11054","11060","11080","11105","11400","12000","22380","EC010","EC097","EC100","EC105","ED010","ED097","ED100","EF010","EF100","EF105","EF120","EF126","11030","11050","11110","11120","12020"]
for file in filelist:
    with open(file)as f:
        data = json.load(f)
    print(type(data))
    data_str = json.dumps(data)

    cona_key = data_str.find("21100")
    cobna_key = data_str.find("11000")
    dummy_cobna_key = data_str.find("DUMMY_COBNA")
    dummy_cona_key = data_str.find("DUMMY_CONA")
    parent_key = data.str.find("10000")
    BU_merged_to_21100_key = data_str.find("11000")
    BU_move_to_sub_of_21100_key = data_str.find("11015")
    sub_of_11015_key = data_str.find("11016")
    BU_move_to_sub_of_21100_key = data_str.find("11020")
    BU_move_to_sub_of_21100_key = data_str.find("11051")
    BU_merged_to_21100_key = data_str.find("11054")
    BU_move_to_sub_of_21100_key = data_str.find("11060")
    BU_move_to_sub_of_21100_key = data_str.find("11080")
    BU_move_to_sub_of_21100_becomes_parent_of_11120_key = data_str.find("11105")
    BU_move_to_sub_of_21100_key = data_str.find("11400")
    Minority_Owner_of_11020_and_11080_key =  data_str.find("12000")
    BU_merged_to_21100_key = data_str.find("22380")
    COFC_Elim_key = data_str.find("EC010")
    CONA_Consol_Elim_key = data_str.find("EC097")
    COBNA_Consol_Elim_only_YTD_NI_to_remain_key = data_str.find("EC100")
    Move_to_new_COGC_CONSOL_node_key =  data_str.find("EC105")
    COFC_US_Elim_key = data_str.find("ED010")
    CONA_US_Elim_key = data_str.find("ED097")
    COBNA_US_Elim_only_YTD_NI_to_remain_key = data_str.find("ED100")
    COFC_NonUS_Elim_key = data_str.find("EF010")
    COBNA_Non_US_Elim_should_zero_out_key =  data_str.find("EF100")
    NonUS_Elim_Cap1_Global_Corp_should_zero_out_key = data_str.find("EF105")
    NonUS_Elim_Cap_one_Holdings_should_zero_out_key = data_str.find("EF120")
    NonUS_Elim_COBEP_HFS_should_zero_out_key = data_str.find("EF126")
    BU_move_to_CONA_for_consolidation_key = data_str.find("11030")
    BU_to_be_dissolved_pre_LEGO_key = data_str.find("11050")
    BU_to_be_dissolved_pre_LEGO_key = data_str.find("11110")
    BU_moved_to_sub_of_11105_key = data_str.find("11120")
    IC_loan_with_11110_to_be_terminated_key = data_str.find("12020")
    
    
    if cona_key > 0 and cobna_key ==-1:
        cona_matched_data.append(file)
    elif dummy_cobna_key > 0:
        dummy_cobna_matched_data.append(file)
    elif dummy_cona_key > 0:
        dummy_cona_matched_data.append(file)
    elif cobna_key > 0 and cona_key ==-1:
        cobna_matched_data.append(file)
    elif parent_key > 0:
        parent_matched_data.append(file)
    elif BU_merged_to_21100_key > 0:
        BU_merged_to_21100_matched_data .append(file)
    elif BU_move_to_sub_of_21100_key > 0:
        BU_move_to_sub_of_21100_matched_data.append(file)
    elif sub_of_11015_key > 0:
        sub_of_11015_matched_data.append(file)
    elif BU_move_to_sub_of_21100_key > 0:
        BU_move_to_sub_of_21100_matched_data .append(file)
    elif BU_move_to_sub_of_21100_key > 0:
        BU_move_to_sub_of_21100_matched_data .append(file)
    elif BU_merged_to_21100_key > 0:
        BU_merged_to_21100_matched_data .append(file)
    elif BU_move_to_sub_of_21100_key > 0:
        BU_move_to_sub_of_21100_matched_data .append(file)
    elif BU_move_to_sub_of_21100_key > 0:
        BU_move_to_sub_of_21100_matched_data .append(file)
    elif BU_move_to_sub_of_21100_becomes_parent_of_11120_key > 0:
        BU_move_to_sub_of_21100_becomes_parent_of_11120_matched_data.append(file)
    elif BU_move_to_sub_of_21100_key > 0:
        BU_move_to_sub_of_21100_matched_data .append(file)
    elif Minority_Owner_of_11020_and_11080_key > 0:
        Minority_Owner_of_11020_and_11080_matched_data.append(file)
    elif BU_merged_to_21100_key > 0:
        BU_merged_to_21100_matched_data .append(file)
    elif COFC_Elim_key > 0:
        COFC_Elim_matched_data.append(file)
    elif CONA_Consol_Elim_key > 0:
        CONA_Consol_Elim_matched_data.append(file)
    elif COBNA_Consol_Elim_only_YTD_NI_to_remain_key > 0:
        COBNA_Consol_Elim_only_YTD_NI_to_remain_matched_data.append(file)
    elif Move_to_new_COGC_CONSOL_node_key > 0:
        Move_to_new_COGC_CONSOL_node_matched_data.append(file)
    elif COFC_US_Elim_key > 0:
        COFC_US_Elim_matched_data.append(file)
    elif CONA_US_Elim_key > 0:
        CONA_US_Elim_matched_data.append(file)
    elif COBNA_US_Elim_only_YTD_NI_to_remain_key > 0:
        COBNA_US_Elim_only_YTD_NI_to_remain_matched_data.append(file)
    elif COFC_NonUS_Elim_key > 0:
        COFC_NonUS_Elim_matched_data.append(file)
    elif COBNA_Non_US_Elim_should_zero_out_key > 0:
        COBNA_Non_US_Elim_should_zero_out_matched_data.append(file)
    elif NonUS_Elim_Cap1_Global_Corp_should_zero_out_key > 0:
        NonUS_Elim_Cap1_Global_Corp_should_zero_out_matched_data.append(file)
    elif NonUS_Elim_Cap_one_Holdings_should_zero_out_key > 0:
        NonUS_Elim_Cap_one_Holdings_should_zero_out_matched_data.append(file)
    elif NonUS_Elim_COBEP_HFS_should_zero_out_key > 0:
        NonUS_Elim_COBEP_HFS_should_zero_out_matched_data.append(file)
    elif BU_move_to_CONA_for_consolidation_key > 0:
        BU_move_to_CONA_for_consolidation_matched_data.append(file)
    elif BU_to_be_dissolved_pre_LEGO_key > 0:
        BU_to_be_dissolved_pre_LEGO_matched_data.append(file)
    elif BU_to_be_dissolved_pre_LEGO_key > 0:
        BU_to_be_dissolved_pre_LEGO_matched_data.append(file)
    elif BU_moved_to_sub_of_11105_key > 0:
        BU_moved_to_sub_of_11105_matched_data.append(file)
    elif IC_loan_with_11110_to_be_terminated_key > 0:
        IC_loan_with_11110_to_be_terminated_matched_data.append(file)
    if all(x in data_str for x in cona_cobna_lst):
        cona_cobna_matched_data.append(file)
       
        
print("cona_matched_data  results",cona_matched_data)
print("cobna_matched_data  results",cobna_matched_data)
print("cona_cobna_matched_data  results",cona_cobna_matched_data)
print("dummy_cona_matched_data  results",dummy_cona_matched_data)
print("dummy_cobna_matched_data  results",dummy_cobna_matched_data)
print("parent_matched_data  results",parent_matched_data)
print("BU_merged_to_21100_matched_data  results",BU_merged_to_21100_matched_data)
print("BU_move_to_sub_of_21100_matched_data  results",BU_move_to_sub_of_21100_matched_data)
print("sub_of_11015_matched_data  results", sub_of_11015_matched_data)
print("BU_move_to_sub_of_21100_matched_data results", BU_move_to_sub_of_21100_matched_data)
print("BU_move_to_sub_of_21100_matched_data  results",BU_move_to_sub_of_21100_matched_data)
print("BU_merged_to_21100_matched_data  results",BU_merged_to_21100_matched_data)
print("BU_move_to_sub_of_21100_matched_data  results",BU_move_to_sub_of_21100_matched_data)
print("BU_move_to_sub_of_21100_matched_data  results",BU_move_to_sub_of_21100_matched_data)
print("BU_move_to_sub_of_21100_becomes_parent_of_11120_matched_data results", BU_move_to_sub_of_21100_becomes_parent_of_11120_matched_data)
print("BU_move_to_sub_of_21100_matched_data  results",BU_move_to_sub_of_21100_matched_data)
print("Minority_Owner_of_11020_and_11080_matched_data  results", Minority_Owner_of_11020_and_11080_matched_data )
print("BU_merged_to_21100_matched_data  results",BU_merged_to_21100_matched_data)
print("COFC_Elim_matched_data results", COFC_Elim_matched_data)
print("CONA_Consol_Elim_matched_data results",CONA_Consol_Elim_matched_data)
print("COBNA_Consol_Elim_only_YTD_NI_to_remain_matched_data results",COBNA_Consol_Elim_only_YTD_NI_to_remain_matched_data)
print("Move_to_new_COGC_CONSOL_node_matched_data results", Move_to_new_COGC_CONSOL_node_matched_data)
print("COFC_US_Elim_matched_data results", COFC_US_Elim_matched_data)
print("CONA_US_Elim_matched_data results",CONA_US_Elim_matched_data)
print("COBNA_US_Elim_only_YTD_NI_to_remain_matched_data results", COBNA_US_Elim_only_YTD_NI_to_remain_matched_data)
print("COFC_NonUS_Elim_matched_data results", COFC_NonUS_Elim_matched_data)
print("COBNA_Non_US_Elim_should_zero_out_matched_data  results", COBNA_Non_US_Elim_should_zero_out_matched_data )
print("NonUS_Elim_Cap1_Global_Corp_should_zero_out_matched_data  results", NonUS_Elim_Cap1_Global_Corp_should_zero_out_matched_data )
print("NonUS_Elim_Cap_one_Holdings_should_zero_out_matched_data results",NonUS_Elim_Cap_one_Holdings_should_zero_out_matched_data)
print("NonUS_Elim_COBEP_HFS_should_zero_out_matched_data results",NonUS_Elim_COBEP_HFS_should_zero_out_matched_data)
print("BU_move_to_CONA_for_consolidation_matched_data results", BU_move_to_CONA_for_consolidation_matched_data )
print("BU_to_be_dissolved_pre_LEGO_matched_data results", BU_to_be_dissolved_pre_LEGO_matched_data)
print("BU_to_be_dissolved_pre_LEGO_matched_data results",BU_to_be_dissolved_pre_LEGO_matched_data) 
print("BU_moved_to_sub_of_11105_matched_data results", BU_moved_to_sub_of_11105_matched_data )
print("IC_loan_with_11110_to_be_terminated_matched_data results", IC_loan_with_11110_to_be_terminated_matched_data)


        
    
    
    
    


    
        
        