# The data we need to retrieve. 
#1. The total number of votes cast 
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winnter of the election based on popular vote. 
#resources/election_results.csv
# Datetime module
#Import the datetime class from the datetime module 
#import datetime
#use the now() attribute on thee datetime class to get the present time
#now = daatetime.datetime.now()
#Print the present time. 
#print("The time right now is", now)


#Direct path to the file 

#Assign a variable for the file to load and the path.
file_to_load = "/Users/rutvikkulkarni/Desktop/Data Bootcamp/Election_Analysis/Resources/election_results.csv"

#Open the election results and read the file
with open (file_to_load) as election_data:

    #To do: perform analysis
    print(election_data)

# To do: perform analysis 

#Close the file 
election_data.close()

import os
dir(os)
#Assign a variable for the file to load and the path 
file_to_load = os.path.join("/Users/rutvikkulkarni/Desktop/Data Bootcamp/Election_Analysis/Resources","election_results.csv")
#Open the election results and read the file 
with open(file_to_load) as election_data:
    #print the file object
    print(election_data)

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("/Users/rutvikkulkarni/Desktop/Data Bootcamp/Election_Analysis/analysis", "election_analysis.txt")
#using the open() funtion with the "w" mode we will write data to the file
open(file_to_save,"w")

# Use the open statement to open the file as a text file
with open(file_to_save,"w") as txt_file:

#Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")


#Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/rutvikkulkarni/Desktop/Data Bootcamp/Election_Analysis/Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/rutvikkulkarni/Desktop/Data Bootcamp/Election_Analysis/analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    #print the header row
    headers = next(file_reader)
    print(headers)




    