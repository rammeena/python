class employee:
    def __init__(self, role, salary):
        self.role = role
        self.salary = salary

    def is_contract_emp(self):
        return self.salary <= 1250

    def is_regular_emp(self):
        return self.salary > 1250
