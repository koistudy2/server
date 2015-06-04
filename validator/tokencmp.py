# This is validator
# Like classic validator, It compares sequence of tokens
# It ignores whitespace, whitespace only separates tokens
# Token should be equal
# separator can be \t, \n, \r, space
# If valid, function returns true, otherwise, it returns false
# EXAMPLE validator("","2\t3","2  3") returns true
# EXAMPLE validator("","2 3","2 03") returns false
# EXAMPLE validator("","2 3 4","2 4 3") returns false

def validator(data,user_output,solution_output):
	user_output_split=user_output.split()
	solution_output_split=solution_output.split()
	return user_output_split == solution_output_split