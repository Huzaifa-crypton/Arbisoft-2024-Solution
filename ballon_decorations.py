# Required imports
import sys
import math

# Calc number of colors in a pattern
def calculate_number_of_colors(pattern):
	white = 0
	orange = 0
	blue = 0
	for color in pattern:
		if color == "w":
			white+=1
		elif color == "o":
			orange+=1
		elif color == "b":
			blue+=1
	return blue , orange , white

def main():
	# Reading input from file
	file_path = sys.argv[1]
	f = open(file_path, "r")
	color_pattern = f.readline()
	color_pattern = color_pattern.replace('\n' , "")
	starting_index = int(f.readline())
	ending_index = int(f.readline())
	
	# Preprocessing data to extract information
	no_of_patterns = 0
	ending_pattern = ""
	pattern_length = len(color_pattern)
	# Number of balloons that can fit in the given section
	number_of_balloons_in_section = (ending_index - starting_index) + 1
	# Finding out the balloon number that will start the pattern in the section 
	skip_balloons_in_section = starting_index % pattern_length
	
	# Pattern that will continue from prev section
	balloon_pattern_from_prev_section = color_pattern[skip_balloons_in_section:]
	# Creating a new pattern of the same length as the original pattern that will be used in the desired section
	new_pattern = balloon_pattern_from_prev_section + color_pattern[:skip_balloons_in_section]
	num_of_blue , num_of_orange , num_of_white = calculate_number_of_colors(new_pattern)
	
	if pattern_length <= number_of_balloons_in_section:
		# Calculating the number of complete patterns that can occur in our section
		no_of_patterns = math.floor(number_of_balloons_in_section / pattern_length)
		number_of_balloons_in_section -= pattern_length*no_of_patterns
		# Calculating the remaining pattern to fill up the section
		ending_pattern = new_pattern[:number_of_balloons_in_section]
	else:
		ending_pattern = new_pattern[:number_of_balloons_in_section]
	
	# Calculating the number of balloon colors utilizing the pattern
	num_of_blue	*= no_of_patterns
	num_of_white *= no_of_patterns 
	num_of_orange *= no_of_patterns
	
	temp_num_of_blue , temp_num_of_orange , temp_num_of_white = calculate_number_of_colors(ending_pattern)
	
	# Adding the number of colors of the remaining pattern
	num_of_blue	+= temp_num_of_blue
	num_of_white += temp_num_of_white 
	num_of_orange += temp_num_of_orange
	
	print('b'+str(num_of_blue)+'o'+str(num_of_orange)+'w'+str(num_of_white))
	
main()