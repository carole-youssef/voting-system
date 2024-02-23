#pre release 2021
#pre release voting system


names = []
tied_candidates = []
student_abstention = 0
highest_votes = 0
total_votes = 0
no_of_winners = 0

#allowing the user to input name of tutor group
tutor_group = input("please input the name of your tutor group")

#allowing the user to input number of students in tutor group
num_students = int(input("please enter number of students in your tutor group"))
while num_students <28 or num_students >35:
    print ("error out of range try again")
    num_students= int(input("please enter number of students your tutor group"))
    
#allowing the user to input number of candidates in election                  
num_candidates = int(input("please enter number of candidates in election"))

#making sure the number of candidates inputted is between the acceptable range                    
while num_candidates <1 or num_candidates >4:
    print ("error out of range try again")
    num_candidates = int(input("please enter number of candidates in election"))
    
vote_count = [0 for count in range(num_candidates)]

#allowing the user to input names of candidates in election       
for count in range (num_candidates):
    candidate_names = str(input("input name of candidate in election"))
    names.append(candidate_names)

student_unique = [0 for count in range(num_students)]

while True:

#allowing the user to input their unique number
    for count in range (num_students):
         unique_num = int(input("input unique number"))
         print(unique_num)
         
# making sure the user doesnt input the same number to vote twice
         if unique_num in student_unique:
             print ("voted and cannot vote again")
             
         else:
             student_unique[count] = unique_num 
             student_choice = input("vote or abstain")
             
#incrementing the number of abstentions                                  
             if student_choice == "abstain":
                 student_abstention = student_abstention + 1

#asking the user which candidate they would like to vote for 
             if student_choice == "vote":
                    candidate_votes = int(input("who would you like to vote for?"))

                    if candidate_votes == 1:
                          vote_count[0] = vote_count[0]+ 1

                    if candidate_votes == 2:
                            vote_count[1] = vote_count[1]+ 1
                                               
                    if candidate_votes == 3:
                            vote_count[2] = vote_count[2]+ 1
                                               
                    if candidate_votes == 4:
                            vote_count[3] = vote_count[3]+ 1
                            
#calculating the total number of votes in the election
    for count in range (len(vote_count)):
        total_votes = num_students - student_abstention

    percentage_votes = [0 for count in range(num_candidates)]
    
#calculating the percentage votes of each candidate
    for count in range (num_candidates):
        percentage_votes[count] = (vote_count[count] / total_votes)*100

#printing all the relevant information from above        
    print ("Tutor group",tutor_group)
    print ("names of candidates and their vote counts and percentages are:")
    print (names)
    print (vote_count)
    print (percentage_votes, "%")
    print ("total votes:", total_votes)
    print ("total abstentions:", student_abstention)

#finding which candidate has got the highest number of votes
    for count in range (num_candidates):
        if vote_count[count] > highest_votes:
            highest_votes = vote_count[count]
            
#finding the candidate winner of the election or finding a tie        
    for count in range (num_candidates):
        if vote_count[count] == highest_votes:
            candidate_winner = names[count]
            no_of_winners += 1

#printing the names of candidates with a tie and resetting the variables
    if no_of_winners > 1:
        for count in range (num_candidates):
            if vote_count[count] == highest_votes:
                tied_candidates.append(names[count])
                num_candidates = no_of_winners
        print ("we have a tie between:",tied_candidates)
        
        names = tied_candidates
        student_unique = [0 for count in range(num_students)]
        vote_count = [0 for count in range(num_candidates)]
        student_abstention = 0
        highest_votes = 0
        no_of_winners = 0
        
#printing the name of the winner of the election        
    else:
        print ("the winner is:", candidate_winner)
        break
