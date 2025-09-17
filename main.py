print ("wellcome to this chatbot")
name = input("what is your name? ")
print ("hello " + name + "!")
age = input("how old are you? ")



def chatbot_guide():
	while True:
		print("\nWelcome to the Chatbot Guide!")
		print("1. Placeholder Option 1")
		print("2. Placeholder Option 2")
		print("3. Placeholder Option 3")
		print("4. Exit Chatbot")
		choice = input("Please select an option (1-4): ")
		if choice == '1':
			print("You selected Placeholder Option 1. (Feature coming soon)")
		elif choice == '2':
			print("You selected Placeholder Option 2. (Feature coming soon)")
		elif choice == '3':
			print("You selected Placeholder Option 3. (Feature coming soon)")
		elif choice == '4':
			print("Exiting chatbot. Goodbye!")
			break
		else:
			print("Invalid option. Please try again.")


if __name__ == "__main__":
	chatbot_guide()