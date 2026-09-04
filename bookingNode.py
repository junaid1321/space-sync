class bookingNode:
    def __init__(self, booking_id, amount, member_id, host_id, booking_day, due_days, penalty_percentage):
        self.booking_id = booking_id
        self.amount = amount
        self.member_id = member_id
        self.host_id = host_id
        self.booking_day = booking_day
        self.due_days = due_days
        self.penalty_percentage = penalty_percentage
        self.settled = False
        self.next = None

    def calculate_overtime_fee(self, current_day):
        deadline_day = self.booking_day + self.due_days
        if current_day <= deadline_day:
            return self.amount
        else:
            overdue_days = current_day - deadline_day
            penalty_fee = self.amount * (self.penalty_percentage/100)
            penalty_overdue = penalty_fee * overdue_days
            return (self.amount + penalty_overdue)

    def display(self):
        print("Booking Details: \n")
        print(f"Booking ID: {self.booking_id}")
        print(f"Booking Day: {self.booking_day}")
        print(f"Host ID: {self.host_id}")
        print(f"Member ID: {self.member_id}")
        print(f"Amount: $ {self.amount}")
        print(f"Due Day: {self.due_days}")
        print(f"Penalty Rate: {self.penalty_percentage}%")
        status = "Yes" if self.settled else "No"
        print(f"Is it settled? {status}")

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def is_settled(self):
        return self.settled == True

    def set_settled(self):
        self.settled = True
        return self.settled

    