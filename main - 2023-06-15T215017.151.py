class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number


class Job:
    def __init__(self, customer, date, duration):
        self.customer = customer
        self.date = date
        self.duration = duration


class LawnMowingManagement:
    def __init__(self):
        self.customers = []
        self.jobs = []

    def add_customer(self, name, address, phone_number):
        customer = Customer(name, address, phone_number)
        self.customers.append(customer)
        print(f"Customer '{name}' added successfully.")

    def schedule_job(self, customer_name, date, duration):
        customer = self._find_customer_by_name(customer_name)
        if customer:
            job = Job(customer, date, duration)
            self.jobs.append(job)
            print(f"Job scheduled for customer '{customer_name}' on {date} for {duration} hours.")
        else:
            print(f"Customer '{customer_name}' not found.")

    def _find_customer_by_name(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None


# Create a lawn mowing management instance
lawn_mowing = LawnMowingManagement()

# Add customers
lawn_mowing.add_customer("John Doe", "123 Main St", "555-1234")
lawn_mowing.add_customer("Jane Smith", "456 Elm St", "555-5678")

# Schedule jobs
lawn_mowing.schedule_job("John Doe", "2023-06-10", 2)
lawn_mowing.schedule_job("Jane Smith", "2023-06-12", 3)


