...

It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18
...

def display_match_details(team1, score1, overs1, team2, score2, overs2):
    print("Match Details:")
    print("Team 1:")
    print(f"Name: {team1}")
    print(f"Score: {score1}")
    print(f"Overs played: {overs1}")
    print("Team 2:")
    print(f"Name: {team2}")
    print(f"Score: {score2}")
    print(f"Overs played: {overs2}")

# Input for Team 1
print("Team 1:")
team1_name = input("Team Name:\n")
team1_score = input("Score:\n")
team1_overs = input("Overs played:\n")

# Input for Team 2
print("Team 2:")
team2_name = input("Team name:\n")
team2_score = input("Score:\n")
team2_overs = input("Overs played:\n")

# Displaying match details
display_match_details(team1_name, team1_score, team1_overs, team2_name, team2_score, team2_overs)
