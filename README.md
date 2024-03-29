# voting-system
A system is required to record and count votes for candidates in school council elections.
The voting system will allow for one representative to be elected from a tutor group. The school has between 28 and 35 students in each tutor group, five year groups named Year 7 to Year 11, and there are six tutor groups in each year group. Tutor group names are their year group followed by a single letter e.g. 7A, 7B, etc. All students are allowed to vote in the system. Each student may only vote once for a representative from their tutor group in the election.

Task 1 - Setting up the voting system to allow a tutor group to elect a representative.
Write a program to:
• allow the tutor to enter the name of the tutor group allow the tutor to enter the number of students in the tutor group
• allow the tutor to enter the number of candidates in the election; maximum of four candidates allow the tutor to enter the names of the candidates 
  and store them in a suitable data structure
• allow each student to input their vote or to abstain
• count the votes for each candidate and student abstentions.

When all students have voted, display the name of the tutor group, the votes for each candidate and the name of the candidate who has won the election. If there is a tie for first place, display all candidates with the equal highest number of votes.

Task 2 - Checking that students only vote once.
Each student is given a unique voter number by their teacher.
Extend Task 1 to achieve the following:
• Allow students to enter their unique voter number before casting their vote.
• Check whether the student has already voted:
- if so, supply a suitable message and do not allow them to vote.
- if not, store the unique voter number, but not their vote, in a suitable data structure, and add their vote to the relevant candidate count or
  abstention.
  
Task 3 - Showing statistics and dealing with a tie.
Extend Task 2 to achieve the following:
• Calculate the percentage of the votes that each candidate received from the number of votes cast, excluding abstentions.
• Display the name of each candidate, the number of votes and the percentage of votes they received from the number of votes cast, excluding 
  abstentions.
• Display the total number of votes cast in the election and the number of abstentions.

In the event of a tie, allow the election to be immediately run again, with only the tied candidates as candidates, and all the students from the tutor group voting again.
