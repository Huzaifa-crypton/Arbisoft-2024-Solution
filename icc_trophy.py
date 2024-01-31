# Imports
import requests
import sys
import math

# Calculate match weightage
def calculate_match_weightage(date):
    date = date.split("/")
    weights = [10 , 9 , 8 , 7 , 6 , 5, 4 , 3 , 2 , 1 , 0.5]
    return weights[2024-int(date[2]) if 2024-int(date[2]) < len(weights) else 10 ]

# Applying weighted percentage FORMULA = (match_won/total_matches)*weight
def calculcate_percentage_winning(matches_won_by_team , total_matches):
	weights = [0.5,1,2,3,4,5,6,7,8,9,10]
	total_percentage_winning = 0
	weight_sum = 0
	for i in range(len(total_matches)):
		if total_matches[i]>0:
			weight_sum+=weights[i]
			total_percentage_winning += ((matches_won_by_team[i]/total_matches[i])*100)*weights[i]
	# Rounding off the values
	total_percentage_winning/=weight_sum
	return round(total_percentage_winning,2)

# Calculate teams score in a match
def calculate_team_score(score_card):
    total_score = 0
    for score in score_card:
        total_score+=score['score']
    return total_score

# Function to calculate matches won and the winning percentage
def winning_percentage(matches , team1 , team2):
    matches_won_by_team1 = [0]*11
    matches_won_by_team2 = [0]*11
    total_matches = [0]*11
    
    for match in matches:
		# Match weight
        match_weight = calculate_match_weightage(match['date'])
		# Teams score
        team1_score = calculate_team_score(match["scoreCardTeam1"])
        team2_score = calculate_team_score(match["scoreCardTeam2"])
		# Counting matches won by each team w.r.t the weight
        if team1_score > team2_score:
            matches_won_by_team1[math.floor(match_weight)]+=1
        elif team2_score > team1_score:
            matches_won_by_team2[math.floor(match_weight)]+=1
        total_matches[math.floor(match_weight)]+=1
    
    return calculcate_percentage_winning(matches_won_by_team1 , total_matches) , calculcate_percentage_winning(matches_won_by_team2 , total_matches)
    
# Total matches played by the teams
def matches_played(matches , team1 , team2):
    return [match for match in matches if (match['team1'] == team1 and match['team2'] == team2) or (match['team1'] == team2 and match['team2'] == team1)]


def calculate_winning_probability(matches , team1 , team2):
    matches_played_by_team1_team2 = matches_played(matches , team1 , team2)
    winning_percentage_team1 , winning_percentage_team2= winning_percentage(matches_played_by_team1_team2 , team1 , team2)
    return str(winning_percentage_team1)+"%,"+str(winning_percentage_team2)+"%"

def main():
    file_path = sys.argv[1]
    f = open(file_path, "r")
    team1 , team2 = f.readline().replace("\n" , "").split(",")

    matches = requests.get("https://l0l6pp2i0k.execute-api.eu-north-1.amazonaws.com/default/icc_matches")
    matches = matches.json()
	
    teams_winning_probability = calculate_winning_probability(matches , team1 , team2)
    print(teams_winning_probability)    

main()