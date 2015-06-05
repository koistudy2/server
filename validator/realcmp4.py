# This is validator
# It compares one Real number, Absolute or Relative Error in 1e-4
# Only double
# It ignores whitespace but whitespaces SHOULD NOT Separate token
# Whitespace is \t, \n, \r, space
# If valid, function returns True, otherwise, it returns False
# EXAMPLE validator_realcmp4.validator("","1.9999","   2.0001") > True
# EXAMPLE validator_realcmp4.validator("","1.9999","\n0.20001E+1") > True
# EXAMPLE validator_realcmp4.validator("","1.9999","2.0001E-1") > False
# EXAMPLE validator_realcmp4.validator("","1.9999","\t20.001000000001E-1") > True
# EXAMPLE validator_realcmp4.validator("","1.9999 54545 54545","\t20.001000000001E-1") > False
class validator_realcmp4:
	@staticmethod
	def validator(data,user_output,solution_output):
		EPS=1e-4
		user_output_split=user_output.split()
		solution_output_split=solution_output.split()
		if len(user_output_split) is not 1: return False
		if len(solution_output_split) is not 1: return False #This should not be happened
		try:
			user_float=float(user_output_split[0])
			solution_float=float(solution_output_split[0])
			if user_float-solution_float < EPS and solution_float-user_float < EPS: return True
			if -EPS<user_float<EPS or -EPS<solution_float<EPS: return False
			if -EPS< (user_float-solution_float)/solution_float < EPS: return True
			if -EPS< (user_float-solution_float)/user_float < EPS: return True
			return False
		except:
			return False #float changing failed, divided by zero or such thing