def checklist2():
	
	value = raw_input("Did you call/use/run this function by typing its name?   (y/n)")
	if value == 'y':
		print "Good"
	else:
		print "Well, get to it then!"
		return
		
	value1 = raw_input("Did you put the ( character after the name to run it?   (y/n)")
	if value1 == 'y':
		print "Awesome"
	else:
		print "Get crackin'"
		return
			
	value2 = raw_input("Did you put the values you want into the parenthesis separated by commas?   (y/n)")
	if value2 == 'y':
		print "Sweet, keep going."
	else:
		print "Looks, like you didn't. Go do it."
		return
		
	value3 = raw_input("Did you end the function call with a ) character?   (y/n)")
	if value3 == 'y':
		print "Congratulations, you have successfully called a function!"
		return
	else:
		print "You missed the last step, fix it."
		return
		
checklist2()
