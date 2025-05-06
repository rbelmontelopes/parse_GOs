import os
import pandas as pd

# set dir were the file is
os.chdir('/mnt/hd/GOs')
#read the file
GOs= open("go.obo").readlines()

#create empty lists to populate with the terms
go_list_ID=[]
go_list_name=[]
go_list_class=[]

#loop to fill the lists
for line in GOs:
    ID=[]
    name=[]
    Class=[]
    if not line.startswith('id:'): # if is not an ID line skip
        pass
    else: # else append the line to the list
        go_list_ID.append(line.replace('id: ','').replace('\n','')) #remove the extra characters with replace
    if not line.startswith('name:'): # if is not an name line skip
        pass
    else: # else append the line to the list
        go_list_name.append(line.replace('name: ','').replace('\n','')) #remove the extra characters with replace
    if not line.startswith('namespace:'): # if is not an class line skip
        pass
    else: # else append the line to the list
        go_list_class.append(line.replace('namespace: ','').replace('\n','')) #remove the extra characters with replace

# concatenate the lists in one dataframe
go=pd.DataFrame({'ID':go_list_ID,'name':go_list_name,'Class':go_list_class})
#set the index
go.set_index('ID', inplace=True)
#write to file
go.to_csv("GOs.tsv", sep='\t',index=True)

#filter only biological process annotations
go_bp=go[go['Class'] == 'biological_process']
#write to file
go_bp.to_csv("GOs_BP.tsv", sep='\t',index=True)

#filter only molecular function annotations
go_mf=go[go['Class'] == 'molecular_function']
#write to file
go_mf.to_csv("GOs_MF.tsv", sep='\t',index=True)

#filter only cellular component annotations
go_cc=go[go['Class'] == 'cellular_component']
#write to file
go_cc.to_csv("GOs_CC.tsv", sep='\t',index=True)
