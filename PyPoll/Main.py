import os
import csv

poll_csv = os.path.join('../PyPoll/election_data.csv')


with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') # Split the data on commas
    header = next(csvreader)
     
    
    unique_candidate_name =[]
    voterID=[] 
    vote_sum=[]
    winner_index=0
  
    
    for poll_data in csvreader:
        voterID.append(poll_data[0]) #reading column 1 data Voters ID
        candidate_name=(poll_data[2]) #reading column 3 data candidate
        if candidate_name in unique_candidate_name: #if is existing candidate
            candidate_index=unique_candidate_name.index(candidate_name)#index where 
            vote_sum[candidate_index] = vote_sum[candidate_index] +1
        else:
            unique_candidate_name.append(candidate_name)
            vote_sum.append(1)
    
    print(f"Election Results")
    print(f"----------------------------".center(24," ")) 
    print(f"Total Votes: {sum(vote_sum)}")
    print(f"----------------------------".center(24," "))

    for i in range(0,len(unique_candidate_name)):   
        print(f"{unique_candidate_name[i]}: {(vote_sum[i]/sum(vote_sum))*100:.03f}% ({vote_sum[i]})  ") # print and format each vote percentage

    for i in range(0,len(unique_candidate_name)-1):  
        if vote_sum[i+1] > vote_sum[i]:
         winner_index=i+1 

    print(f"----------------------------".center(24," ")) 
    print(f"Winner: {unique_candidate_name[winner_index]}")
    print(f"----------------------------".center(24," "))


   
       

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------




 