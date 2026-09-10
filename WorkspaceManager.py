from bookingNode import bookingNode
from MemberNode import MemberNode

class WorkspaceManager:
    def __init__(self):
        self.root = None
        self.current_day = 1

    def insert_member(self, member_id : int, name : str):
        New_member = MemberNode(member_id, name)
        if self.root == None:
            self.root = New_member
            print(f"Member {member_id} is added successfully!")
            return 
        
        current = self.root
        while True:
            if member_id < current.member_id:
                if current.left is None:
                    current.left = New_member
                    print(f"Member {member_id} is added successfully!")
                    return 
            elif member_id > current.member_id:
                if current.right is None:
                    current.right = New_member
                    print(f"Member {member_id} is added successfully!")
                    return
            else:
                print("ERROR! THE ID OF THE MEMBER MUST BE UNIQUE")
                return

    def search_member(self, member_id:int) -> MemberNode | None:
        current = self.root

        while current is not None:
                if member_id < current.member_id:
                    current = current.left
                elif member_id > current.member_id:
                    current = current.right
                else:
                    print("Member Found!")
                    return current

        print("Member not found!")
        print("Enter the correct Member ID")
        return None

    def display_all_members(self, current = None, start = True):
        if start:
            current = self.root

        if current is None:
            return

        self.display_all_members(current.left, start = False)
        current.display_member()
        self.display_all_members(current.right, start = False)

    def deactivate_member(self, member_id : int):
        current = self.search_member(member_id)
        if current is None:
            return

        current.active = False
        print("Member De-activated Successfully!")
        return

    def advance_days(self, days : int):
        if days < 0:
            print("The days to be added cannot be negative.")
            return

        self.current_day += days
        print(f"Time advanced {days} days. Current day: {self.current_day}")

    def book_space(self, booking_id, borrower_id, host_id, duration_days, amount, percentage_penalty):
        if borrower_id != host_id:
            borrower = self.search_member(borrower_id)
            host = self.search_member(host_id)
            if borrower is not None and host is not None:
                if borrower.active == True and host.active == True:
                    due_day = self.current_day + duration_days

                    new_bookings_b = bookingNode(booking_id,amount,borrower_id,host_id,due_day,duration_days,percentage_penalty)
                    new_bookings_h = bookingNode(booking_id,amount,borrower_id,host_id,due_day,duration_days,percentage_penalty) 

                    borrower.add_borrowed_booking(new_bookings_b)
                    host.add_hosted_booking(new_bookings_h)
                    print(f"Booking has been confirmed from day {self.current_day} to day {due_day}")
                    return
                else:
                    print("Make sure both members are active.\n")
                    return
            else:
                print("Error! Members not found!")
                return
        else:
            print("Error! Make sure the host and borrower IDs are unique!")
            return

    def return_booking(self, booking_id, borrower_id, host_id):
        if borrower_id != host_id:
            borrower = self.search_member(borrower_id)
            host = self.search_member(host_id)

            if borrower != None and host != None:
                booking = borrower.remove_booking(booking_id, "borrowed")
                host.remove_booking(booking_id, "hosted")
                if booking is not None:
                    if self.current_day > booking.due_days:
                        over_fee = booking.calculate_overtime_fee(self.current_day)
                        print(f"Overdue Payment Total: {over_fee}")
                        return
                    else:
                        print(f"Payment Total: {booking.amount}")
                        return
                else:
                    return
            else:
                print("Error! Members not found!")
                return
        else:
            print("Error! The borrower and host must be different members!")
            return

    def display_members(self, member_id):
        member = self.search_member(member_id)
        if member is None:
            return 

        member.display_all_booking()