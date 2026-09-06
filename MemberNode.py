from bookingNode import BookingNode

class MemberNode:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.active = True
        self.left = None
        self.right = None
        self.borrowed_head: BookingNode | None = None
        self.hosted_head: BookingNode | None = None

    def add_borrowed_booking(self, booking: BookingNode):
        booking.set_next(self.borrowed_head)
        self.borrowed_head = booking

    def add_hosted_booking(self, booking_node: BookingNode):
        booking_node.set_next(self.hosted_head)
        self.hosted_head = booking_node

    def find_booking(self, booking_id, list_type):
        lower_list_type = list_type.lower()
        if lower_list_type == "borrowed":
             curr = self.borrowed_head
             while curr is not None:
                 if curr.booking_id == booking_id:
                     return curr
                 else:
                     curr = curr.get_next()
                     continue

             if curr is None:
                 print("\nBooking not found.\n")
                 return None

        elif lower_list_type == "hosted":
            curr = self.hosted_head
            while curr is not None:
                if curr.booking_id == booking_id:
                    return curr
                else:
                    curr = curr.get_next()
                    continue

            if curr is None:
                print("\nBooking not found.\n")
                return None


    def remove_booking(self, booking_id, list_type):
        lower_list_type = list_type.lower()
        if lower_list_type == "borrowed":
            prev_node = None
            curr_node = self.borrowed_head
            while curr_node is not None:
                if curr_node.booking_id == booking_id:
                    break
                else:
                    prev_node = curr_node
                    curr_node = curr_node.get_next()


            if curr_node == None:
                print("\nBooking not found.\n")
                return None
            
            if prev_node == None:
                self.borrowed_head = curr_node.get_next()
                curr_node.set_next(None)
                print("\nBooking Removed.\n")
                return curr_node
            else:
                prev_node.set_next(curr_node.get_next())
                curr_node.set_next(None)
                print("\nBooking Removed.\n")
                return curr_node

        elif lower_list_type == "hosted":
            prev_node = None
            curr_node = self.hosted_head
            while curr_node is not None:
                if curr_node.booking_id == booking_id:
                    break
                else:
                    prev_node = curr_node
                    curr_node = curr_node.get_next()

            if curr_node == None:
                print("\nBooking not found.\n")
                return None
            
            if prev_node == None:
                self.hosted_head = curr_node.get_next()
                curr_node.set_next(None)
                print("\nBooking Removed.\n")
                return curr_node
            else:
                prev_node.set_next(curr_node.get_next())
                curr_node.set_next(None)
                print("\nBooking Removed.\n")
                return curr_node
        
        else:
            print("\nInvalid list type specified.\n")
            return

    def display_member(self):
        print(f"Member ID: {self.member_id}")
        print(f"Member Name: {self.name}")
        is_active = "Yes" if self.active else "No"
        print(f"Is Member Active? {is_active}")

    def display_all_booking(self):
        curr = self.borrowed_head
        print("\nBorrowed Members\n")
        while curr is not None:
            print("\n")
            curr.display()
            print("\n")
            curr = curr.get_next()

        curr = self.hosted_head
        print("\nHosting Members\n")
        while curr is not None:
            print("\n")
            curr.display()
            print("\n")
            curr = curr.get_next()    