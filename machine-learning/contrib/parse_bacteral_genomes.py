# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:29:58 2018

@author: Jake
"""
import numpy
import pandas as pd
from Bio import Entrez

class PBG_Class():
    final_df = pd.DataFrame()
    sub_str = {}
    final_dict = {}
    csv_text = ''
    input_files = ["genomes_proks.txt",
                   #"genomes_proks-2.txt",
                   #"genomes_proks-3.txt",
                   #"genomes_proks-4.txt",  ## looks bad
                   #"genomes_proks-5.txt",
                   #"genomes_proks-6.txt"
                  ]
        
    def substrings(self):
        check = input('Are there any substrings you would like to enter? y/n ')
        while check.lower() == 'y' or check.lower() == 'yes':
            number_str = input('How many substrings would you like to enter? ')
            number = int(number_str)
            for i in range(number):
                name = input('Please give the name for substring %s: '%str(i+1))
                substring = input('Please enter substring %s: '%str(i+1)).upper()
                pbgclass.sub_str[name] = substring
            check = input('Are there any more substrings you would like to enter? y/n ')

    def pbg(self):
        organisms_dict = {}
        try: 
            for filename in PBG_Class.input_files:
                organisms = [] # for each loop this list will contain the organisms within each genus
                organisms_dict[filename] = organisms #define the contents of the organisms_dict dicitonary
                ## print "reading : " , filename
                data_type = str
                data = numpy.loadtxt( filename, data_type, delimiter="\t" ) #use numpy to load the text from the .txt file contained in the filename variable into the data variable
                    
                for i in range(0,data.shape[0]): 
                    organism = data[i,0] + ' ' + data[i,1] #obtain the identity of each organism (genus, species, and strain)
                    organisms.append(organism) #append each orgamism to the orgamismS list. Note organism and orgamisms are different variables
   
        except IOError as error:
            print( "Error:", str(error)) #if there is an IO error print the error
        Entrez.email = input('Please provide your email address: ') #tells NCBI who you are so they can contact you if need be
        print('Working...')
        sub_strings = PBG_Class.sub_str
        final_dict = PBG_Class.final_dict
        for org_list in organisms_dict.values(): #each value in organisms_dict is a list
            for org in org_list: #gets each organism within said list
                handle = Entrez.esearch(db = 'nuccore', term = org + ' complete genome') #seach the entrez nuccore database for each organisms complete genome. Note this is just a query, not specific key words
                record = Entrez.read(handle) #read the handle vairable to obtain the Entrez nuccore ID for the genome of each organism
                if record['IdList'] != []: #check to see if there actually is an ID for the organism
                    net_handle = Entrez.efetch(db="nuccore", id=record['IdList'][0], rettype="fasta", retmode="text") #if there is an ID read in the genome
                    s = net_handle.read() #the variable s contains the genome is text form
                    sub_dict = {} #this dict will hold the counts for each substring
                    for name,sub_str in sub_strings.items(): #loop through our substrings of interest
                        count = 0 #initialize a count value
                        #matches = re.findall(sub_str,s,overlapped = True) #the next three lines work if the regex (different from re) library is installed but it isn't on the server
                        #for match in matches:
                        #    count +=1
                        sub_len = len(sub_str)
                        for z in range(len(s)): 
                            if s[z:z+sub_len] == sub_str: #essentially accesses s by index to check if a substring is present within the current position in s
                                count +=1 #if a substring is found increment count
                            sub_dict[sub_str] = count #set each key for sub_dict equal to a substring and the value equal to the count of the sub string
                        final_dict[org] = sub_dict #add the organism name and the sub_dict associated with the organism to final_dict
                        net_handle.close() #close net_handle
                    else:
                        pass #if there is no Entrez ID for the organism do nothing. Could easily do something here
        print('Done')
        
    def csv(self):
        order = input('Would you like organism names to be contained in rows or columns? Please specify with "rows" or "columns" ')
        final_dict = PBG_Class.final_dict
        final_df = pd.DataFrame(final_dict)        
        #final_df.to_csv(r'C:\Users\Jake\Documents\Hudson Alpha\Python for Fun\pbgcsv.csv')
        if order.lower() == 'columns':
            PBG_Class.csv_text = final_df.to_csv()
            PBG_Class.final_df = final_df
        else:
            PBG_Class.csv_text = final_df.T.to_csv()
            PBG_Class.final_df = final_df.T
            
    def csv_to_path(self):
        try:
            path = r''+input('Provide the path where you wish to write your CSV file: ')
            file_name = r''+input('Provide the name for the CSV file: ')
            order = input('Would you like organism names to be contained in rows or columns? Please specify with "rows" or "columns" ')
            if order.lower() == 'columns':
                PBG_Class.final_df.to_csv(path+file_name)
            else:
                PBG_Class.final_df.T.to_csv(path+file_name)
                
        except OSError as error:
            print(error)
            print('Path cannon be entered as string, if you entered the path as a string remove the quotations and try again')
            
            