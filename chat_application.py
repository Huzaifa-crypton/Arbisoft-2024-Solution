# Imports
import sys

# Encode function
def encode(input_string , key):
	encoded_string = ""
	for ch in input_string:
		# Add 0 to encoded string if upper case character is found
		if ch.isupper():
			encoded_string+="0"
		found_ch = False
		for ind , key_item in enumerate(key , start = 1):
			# Check if a key_item contains the required character
			if key_item.find(ch.lower()) != -1:
				# Add position of character in the key
				encoded_string+=str(ind)*(key_item.index(ch.lower())+1)
				found_ch = True
		if found_ch == False:
			return "Error"
		# Adding delimiter at the end
		encoded_string+="0"
	return encoded_string

# Decode function
def decode(input_string , key):
	decoded_string = ""
	while len(input_string) > 1:
		upper_case = True if input_string[0] == "0" else False 
		# Remove the "0" character
		input_string = input_string[1:] if upper_case else input_string
		# Find index of next delimiter (0)
		index_of_next_delimiter = input_string.find("0")
		# Extract the character stream we need to decode
		
		# If index of delimiter not found then the encoded string is not valid
		if index_of_next_delimiter == -1:
			return "Error"
		next_character_stream = input_string[:index_of_next_delimiter]
		# Update the input string
		input_string = input_string[index_of_next_delimiter+1:]
		
		# Decoding
		# If the index is not present in key, then Error
		if int(next_character_stream[0])-1 >= len(key):
			return "Error"
		key_item = key[int(next_character_stream[0])-1]
		item_number_in_key = len(next_character_stream[1:])
		
		# If the index is not present in key_item, then Error
		if item_number_in_key >= len(key_item):
			return "Error"
		decoded_string += key_item[item_number_in_key].upper() if upper_case else key_item[item_number_in_key]
	return decoded_string

def main():
	# Take input from file
	file_path = sys.argv[1]
	f = open(file_path, "r")
	key = f.readline().replace('"' , "").replace('\n' , '').replace(" ","").split(",")
	encode_decode = int(f.readline())
	input_string = f.readline().replace('\n' , '')
	
	result = ""
	# 1 to encode and 2 to decode
	if encode_decode == 1:
		result = encode(input_string , key)
	else:
		result = decode(input_string , key)
	print(result)
		
main()