import os
import csv

poll_csv = os.path.join('../PyPoll/election_data.csv')
# total = 0
#Voter ID, County, and Candidate. 

def unique(candidatelist):
    unique_list=[]

    for x in candidatelist:
        if x not in unique_list:
            unique_list.append(x)
    
    return  unique_list
    # for x in unique_list: 
    #     print(f"{x}")

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') # Split the data on commas
    header = next(csvreader)
     
    voter_id =[] 
    county =[]
    candidate =[] 
    
#     grt_increase = 0
#     FirstFlag = True   
#sortdata = itertools.groupby(sortdata, operator.itemgetter('candidate'))

    for poll_data in csvreader:
        voter_id_x = str(poll_data[0])
        county_x = str(poll_data[1])
        candidate_x = str(poll_data[2])
        

#          if FirstFlag == True:
#             min_date = date
#             min_profitloss = profitloss 
#             FirstFlag = False
#          total = total + profitloss
        voter_id.append(voter_id_x)
        county.append(county_x)
        candidate.append(candidate_x)

    list_length = len(voter_id)



        
    print(f"Election Results") 
    print(f"----------------------------".center(24," ")) 
    print(f"Total Votes: {list_length}")
    print(f"----------------------------".center(24," ")) 
    #for candidate_x in candidate: 
    print(f"Unique Candidate: {unique(candidate)}")
   


# Election Results
# •	-------------------------
# •	Total Votes: 3521001
# •	-------------------------
# •	Khan: 63.000% (2218231
# •	Correy: 20.000% (704200)
# •	Li: 14.000% (492940)
# •	O'Tooley: 3.000% (105630)
# •	-------------------------
# •	Winner: Khan
# -------------------------




 