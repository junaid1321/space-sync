from bookingNode import BookingNode
from MemberNode import memberNode

class WorkspaceManager:
    def __init__(self):
        self.root = None
        self.current_day = 1

    def insert_member(self, member_id : int, name : str):
        New_member = memberNode(member_id, name)
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

    def search_member(self, member_id:int) -> memberNode | None:
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



