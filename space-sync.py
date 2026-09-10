from WorkspaceManager import WorkspaceManager

wm = WorkspaceManager()

while True:
    print("\n--- WORKSPACE MENU ---")
    print("1. Add Member")
    print("2. Search Member")
    print("3. Display All Members")
    print("4. Deactivate Member")
    print("5. Advance Days")
    print("6. Book Space")
    print("7. Return Booking")
    print("8. Display Member Bookings")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    try:
        if choice == "1":
            m_id = int(input("Enter Member ID: "))
            name = input("Enter Name: ")
            wm.insert_member(m_id, name)

        elif choice == "2":
            m_id = int(input("Enter Member ID: "))
            wm.search_member(m_id)

        elif choice == "3":
            wm.display_all_members()

        elif choice == "4":
            m_id = int(input("Enter Member ID: "))
            wm.deactivate_member(m_id)

        elif choice == "5":
            days = int(input("Enter days to advance: "))
            wm.advance_days(days)

        elif choice == "6":
            b_id = int(input("Enter Booking ID: "))
            borrower_id = int(input("Enter Borrower ID: "))
            host_id = int(input("Enter Host ID: "))
            duration = int(input("Enter Duration (days): "))
            amount = float(input("Enter Amount: "))
            penalty = float(input("Enter Penalty Percentage: "))
            wm.book_space(b_id, borrower_id, host_id, duration, amount, penalty)

        elif choice == "7":
            b_id = int(input("Enter Booking ID: "))
            borrower_id = int(input("Enter Borrower ID: "))
            host_id = int(input("Enter Host ID: "))
            wm.return_booking(b_id, borrower_id, host_id)

        elif choice == "8":
            m_id = int(input("Enter Member ID: "))
            wm.display_members(m_id)

        elif choice == "9":
            print("THANKS FOR USING SPACE-SYNC❤️")
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")
    
    except ValueError:
        print("Error! Invalid Input! Please enter a valid numbers where required!")