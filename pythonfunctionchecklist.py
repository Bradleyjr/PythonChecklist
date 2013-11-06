def check_list():

	value = raw_input("Did you start your function definition with def?  (y/n):")
	if value == "y":
		print "Ok, good."
	else:
		print "Please do that."
		return
	
	value1 = raw_input("Does your function name have only characters and _ (underscore) characters?  (y/n):")
	if value1 == "y":
		print "Cool"
	else:
		print "Please do that."
		return
		
	value2 = raw_input("Did you put an open parenthesis ( right after the function name?  (y/n):")
	if value2 == "y":
		print "Good"
	else:
		print "Please do that."
		return
	
	value3 = raw_input("Did you put your arguments after the parenthesis ( separated by commas?  (y/n):")
	if value3 == "y":
		print "Amazing"
	else:
		print "Please do that."
		return
	
	value4 = raw_input("Did you make each argument unique (meaning no duplicated names)?  (y/n):")
	if value4 == "y":
		print "Good job"
	else:
		print "Please do that."
		return
	
	value5 = raw_input("Did you put a close parenthesis and a colon ): after the arguments?  (y/n):")
	if value5 == "y":
		print "Fantastic"
	else:
		print "Please do that."
		return
	
	value6 = raw_input("Did you indent all lines of code you want in the function four spaces? No more, no less.  (y/n):")
	if value6 == "y":
		print "Awesome"
	else:
		print "Please do that."
		return
	
	value7 = raw_input("Did you end your function by going back to writing with no indent (dedenting we call it)?  (y/n):")
	if value7 == "y":
		print "Congratulations, you have made a correct function!"
	else:
		print "Please do that."
		return

	question = raw_input('Would you like to continue to the \"Running/Calling a Function Checklist\"?    (y/n)')
	if question == "y":
		print "Alrighty, we will start that up for you!"
		import callingafunctionchecklist
	else:
		print "Ok, goodbye."
		return
		
check_list()

