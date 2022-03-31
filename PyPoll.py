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


#1. Initialize a total vote counter
total_votes = 0 

candidate_options = []

#1. Declare the empty dictionary 
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    #print the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #Add it to the list of candidates. 
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0 

            #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1

    #Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        #After opening the file print the final vote count to the terminal.
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

        print(election_results,end = "")
        #Save the final vote count to the text file.
        txt_file.write(election_results)
        

#Determine the percentage of votes for each candidate by looping through the counts 
#1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
    #2.Retrive vote count of a candidate. 
            votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes
            vote_percentage = float(votes)/float(total_votes)*100


    #To do: print out each candidates name, vote count, and percentage of votes to the terminal
            candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)




    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
if(votes>winning_count) and (vote_percentage>winning_percentage):
       #If true then set winning_count = votes and winning_percent = Vote_percentage.  
       winning_count = votes 
       winning_percentage = vote_percentage 
       #And, set the winning_candidate equal to the candidates name. 
       winning_candidate = candidate_name 

    

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

txt_file.write(winning_candidate_summary)


    #Print the candidate vote dictionary     
print(candidate_votes)

print(candidate_options)


#Print the total votes 
print(total_votes)






    