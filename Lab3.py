import classes1.Student
import classes1.Order
import classes1.Book
import classes1.Employee
import classes1.Library
import classes1.Property

st1 = classes1.Student.Student("John", (3, 1, 3, 2, 1, 2, 3))
st2 = classes1.Student.Student("Peter", (5, 5, 5, 4, 5, 4, 5))

print(st1.is_passed())
print(st2.is_passed())

# zad 2

l1 = classes1.Library.Library('Katowcie', 'Ulicowa',
                              '42-144', '2-12', 654465867)
l2 = classes1.Library.Library('Płock', 'Kamila Mamońskiego',
                              '60-997', '8-20', 876548384)

e1 = classes1.Employee.Employee('Mateusz', 'Grzegoszewski', '12.03.2000',
                                '12.03.2020', 'Bytom',
                                'Bytomska', '24-333', 123456789)
e2 = classes1.Employee.Employee('Andrzej', 'Andrzejowski', '12.03.2000',
                                '12.03.2020', 'Bytom',
                                'Bytomska', '23-231', 123456789)
e3 = classes1.Employee.Employee('Johannes', 'Paul', '12.03.2000',
                                '12.03.2020', 'der Bytom',
                                'Czeska', '25-120', 123456780)

b1 = classes1.Book.Book(l1, '07.07.2000', 'Henryk', 'Pisarski', '777')
b2 = classes1.Book.Book(l1, '07.07.2000', 'Henryk', 'Pisarski', '665')
b3 = classes1.Book.Book(l2, '07.07.2000', 'Henryk', 'Pisarski', '656')
b4 = classes1.Book.Book(l2, '07.07.2000', 'Henryk', 'Pisarski', '566')
b5 = classes1.Book.Book(l2, '07.07.2000', 'Henryk', 'Pisarski', '997')

o1 = classes1.Order.Order(e1, 'Andrzej Hubert', [b1, b2], '07.07.2107')
o2 = classes1.Order.Order(e2, 'Julia Juliowska', [b2, b3], '07.07.2106')

# print(o1, o2)

# zad 3

house = classes1.Property.House(4321, 4, 50000, 'Katowice', 'Uliczna', 10)
flat = classes1.Property.Flat(44, 3, 10000, 'Hubertów', 6)

print(house)
print(flat)
