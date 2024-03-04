class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return 'Zamówienie obsługiwane przez ' + self.employee + \
               ' Zamówione przez ' + self.student + ' Zawierające ' \
               + str(str([ksiazka]) for ksiazka in self.books) + \
               ' o dacie ' + self.order_date