# Import necessary modules
import os
import csv
import statistics

# Create Path to File
election_data = os.path.join("..", "PyPoll","Resources", "election_data.csv")

# Initalize Variables
candidate_list =[]

# First For Loop 
# Open & Read CSV File
with open(election_data) as csvfile:
    
# CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=",")

# Read The Header Row First (Skip This Step If There Is No Header)   
    csv_header = next(csvfile)
    
# Read Each Row Of Data After The Header   
    for row in csvreader:
        if row [2] not in candidate_list:
            candidate_list.append(row[2])
    print(f'List Of Candidates: {candidate_list}')

#Second For Loop
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)   
    Khan_Votes = 0
    Correy_Votes = 0
    Li_Votes = 0
    O_Tooley_Votes = 0
    
# Read Each Row Of Data After The Header & Calculate Total Number of Votes  
    for row in csvreader:
        if row [2] == candidate_list[0]:
               Khan_Votes += 1
        elif row [2] == candidate_list[1]:
               Correy_Votes += 1
        elif row [2] == candidate_list[2]:
               Li_Votes += 1
        elif row [2] == candidate_list[3]:
               O_Tooley_Votes += 1
               
Total_Votes = Khan_Votes + Correy_Votes + Li_Votes + O_Tooley_Votes

# Print Analysis
print("Election Results")
print("-------------------------------------------------------------") 
print(f'Total Votes: {Total_Votes}')   
print("-------------------------------------------------------------")   
print('Khan:{round(Khan_Votes/Total_Votes")*100,3)} ({Khan_Votes})')
print('Correy:{round(Correy_Votes/Total_Votes")*100,3)}% ({Correy_Votes})')
print('Li:{round(Li_Votes/Total_Votes")*100,3)}% ({Li_Votes})')
print("O'Tooley:{round(O_Tooley_Votes/Total_Votes)*100,3)}% ({O_Tooley_Votes})")
print("-------------------------------------------------------------")            
if Khan_Votes > Correy_Votes and Khan_Votes > Li_Votes and Khan_Votes > O_Tooley_Votes:
    Winner = "Khan"
elif Correy_Votes > Khan_Votes and Correy_Votes > Li_Votes and Correy_Votes > O_Tooley_Votes:
    Winner = "Correy"
elif Li_Votes > Khan_Votes and Li_Votes > Correy_Votes and Li_Votes > O_Tooley_Votes:
    Winner = "Li"
elif O_Tooley_Votes > Khan_Votes and O_Tooley_Votes > Correy_Votes and O_Tooley_Votes > Li_Votes:
    Winner = "O_Tooley"

print(f'Winner: {Winner}')
print("-------------------------------------------------------------") 

#Specify File
output_path = 'Election Results.txt'

#Open File & Specify The Variable To Hold The Contents
with open(output_path, 'w', newline ='') as csvfile:

#Write New Data
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------------------------------------"])
    csvwriter.writerow([f'Total Votes: {Total_Votes}'])
    csvwriter.writerow(["---------------------------------------------------------------"])
    csvwriter.writerow([f'Khan: {round((Khan_Votes/Total_Votes)*100,3)}% ({Khan_Votes})'])
    csvwriter.writerow([f'Correy: {round((Correy_Votes/Total_Votes)*100,3)}% ({Correy_Votes})'])
    csvwriter.writerow([f'Li: {round((Li_Votes/Total_Votes)*100,3)}% ({Li_Votes})'])
    csvwriter.writerow([f"O'Tooley: {round((O_Tooley_Votes/Total_Votes)*100,3)}% ({O_Tooley_Votes})"])
    csvwriter.writerow(["---------------------------------------------------------------"])   
    csvwriter.writerow([f'Winner: {Winner}']) 
    csvwriter.writerow(["---------------------------------------------------------------"])              
     