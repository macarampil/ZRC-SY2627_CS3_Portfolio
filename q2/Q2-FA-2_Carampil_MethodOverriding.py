# Parent Class_---------------------------------
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        calculated_amount = self.__bill_amount * 1.0  # No discount for regular people (normal na people)
        return calculated_amount

#mga baby na classes (child classes)----------------------------------
class Senior_Patient(Patient):
    def calculate_bill(self):
        calculated_amount = self.get_bill_amount() * 0.80  # 20% discount for senior patients (para sa maga oldies)
        return calculated_amount


class PhilHealth_Patient(Patient):
    def calculate_bill(self):
        calculated_amount = self.get_bill_amount() * 0.85  # 15% discount for PhilHealth patients (para sa mga tao na merong insurance)
        return calculated_amount

#-------------objects here----------------#
regular_patient1 = Patient("I said rererebeca", 1000)
oldie_patient1 = Senior_Patient("Jaden Piket Smith", 1000)
philhealth_patient1 = PhilHealth_Patient("Bi Ngi", 1000)

print("Hospital Billing System")
print("--------------------------")
print("Patient Name:", regular_patient1.get_name())
print("Original Bill: ₱",regular_patient1.get_bill_amount())
print("Final Bill: ₱",regular_patient1.calculate_bill())
print()
print("Patient Name:", oldie_patient1.get_name())
print("Original Bill: ₱",oldie_patient1.get_bill_amount())
print("Final Bill: ₱",oldie_patient1.calculate_bill())
print()
print("Patient Name:", philhealth_patient1.get_name())
print("Original Bill: ₱",philhealth_patient1.get_bill_amount())
print("Final Bill: ₱",philhealth_patient1.calculate_bill())
print()