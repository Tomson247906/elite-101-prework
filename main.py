from orders import orders

#this is what greets the user
name = input("what is your name?").strip().title()
print ("hello " + name + " is there something I can help you with?")


#this is what defines what the guide will say
def chatbot_guide():
    while True:
        print("\nChatbot Menu:")
        print("1. order hasn't arrived")
        print("2. report an issue")
        print("3. Request a refund")
        print("4. order status")
        print("5. leave a review")
        print("6. Exit")

        #this allows the user to pick between the options
        choice = input("Enter your choice (1-6): ").strip()

        #this opition allows the user to say that their has not arrived and it responds saying that cooks are backed up and asking if the user would like a refund
        if choice == '1':
            print("Oh no, we're sorry to hear that. our cooks are backed up right now so it may take a bit longer than usual to get your food out. But, would you like a refund?")
            refund = input("Would you like a refund? (yes/no): ").strip().lower()
            if refund == 'yes':
                print("Your refund is being processed. You should see it in your account within 5-7 business days.")
            elif refund == 'no':
                print("we are sorry for the inconvenience. your order will be out as soon as possible.")
            else:
                print("please put a yes/no response")
        #this allows the user to report an issue and it thanks them for reporting it
        elif choice == '2':
            print("what issue would you like to report?")
            issue = input("Please describe the issue: ")
            print(f"Thank you for reporting the issue: {issue}. Our team will look into it shortly.")
            issue_fix = input("is there anyway for us to fix this.(yes/no)")
            if issue_fix == 'yes':
                solution = input("How can we fix this for you").strip().title()
            elif issue_fix == "no":
                money_back = input("Would you like a refund? (yes/no):").strip().lower()
                if money_back == "yes":
                    print("Your refund is being processed. You should see it in your account within 5-7 business days.")
                elif money_back == "no":
                    print("we are sorry for our mistake and will try our best to improve")
                else:
                    print("please put a yes/no response")
        #this allows the user to request a refund and it asks for them to provide a reason for the refund
        elif choice == '3':
            print("You selected a refund.")
            reason = input("Please provide a reason for the refund: ")
            print(f"Thank you for providing the reason: {reason}. Your refund request is being processed.")


        #this allows the user to check the status of their order by providing their order ID
        elif choice == '4':
            order_id = int(input("Please enter your order ID: "))
            order_found = False
            for order in orders:
                if order["order_id"] == order_id:
                    print(f"Order ID: {order_id}, Status: {order['status']}")
                    order_found = True
                    break
            if not order_found:
                print("Order ID not found.")
        

        #this allows the user to leave a review and it thanks them for their feedback
        elif choice =='5':
            review = input("Please leave your review: ")
            print("Thank you for your feedback!")


        #this allows the user to exit the chatbot
        elif choice == '6':
            print("Exiting chatbot. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
	chatbot_guide()