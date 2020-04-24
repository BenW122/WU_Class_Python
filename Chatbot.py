while True:
	n = raw_input("Please say 'hi':")
	if n.strip() == 'hello':
		print("Hello there! I'm Isa, what is your name?")
	x = raw_input()
	print("Hi" + x + ","+  "it's nice to meet you. How is your day going?")
	y = raw_input()
	daygood = ["fine","well","wonderful","amazing","good","very good","very well", "super","great"]
	daybad = ["bad","could be better","awful","not good"]
	if y in daygood:
		print("I'm glad to hear that.")
	elif y in daybad:
			print("I'm sorry to hear that, what is wrong?")
			z = raw_input()
			if "much to do" in z:
				print("You should sleep more.")
	else:
		print("I'm sorry but I don't understand this.")


			
