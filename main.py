# namedtuple


# --------------------------------------------------------

# employees = [
#     (1, "Toxir", "Toxirov", 27, "toxir@gmail.com"),
#     (2, "Sobir", "Sobirov", 32, "sobir@gmail.com")
# ]

# for employee in employees:
#     employee.name
#     # print(employee[0], employee[1], employee[4])

# --------------------------------------------------------

# class Employee:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
#
# employees = [
#     (1, "Toxir", "Toxirov", 27, "toxir@gmail.com"),
#     (2, "Sobir", "Sobirov", 32, "sobir@gmail.com")
# ]
#
# # em = Employee(employees[0][0], employees[0][1], employees[0][2], employees[0][3], employees[0][4])
#
# print(em.name)


# --------------------------------------------------------------------------

class Employee:
    def __init__(self, id, name, lastname, age, email):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email


employees = [
    (1, "Toxir", "Toxirov", 27, "toxir@gmail.com"),
    (2, "Sobir", "Sobirov", 32, "sobir@gmail.com")
]

for employee in employees:
    em = Employee(*employee)
    em.name = 'Jalil'
    print(em.id, em.name, em.lastname, em.age, em.email)


# --------------------------------------------------------------------------

from collections import namedtuple

Employee = namedtuple('Employee', 'id name lastname age email')

employees = [
    (1, "Toxir", "Toxirov", 27, "toxir@gmail.com"),
    (2, "Sobir", "Sobirov", 32, "sobir@gmail.com")
]

for employee in employees:
    em = Employee(*employee)
    print(em.id, em.name, em.lastname, em.age, em.email)




"""Car"""
"""id, model, color, speed, price"""












