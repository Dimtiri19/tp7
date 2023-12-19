from fraction import Fraction

# Création de fractions
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 4)
fraction3 = Fraction(2, 2)


# Opérations avec les fractions
sum_fraction = fraction1 + fraction2
diff_fraction = fraction1 - fraction3
prod_fraction = fraction2 * fraction3
div_fraction = fraction1 / fraction2
#pow_fraction = fraction3 ** fraction1

# Affichage des résultats
print(f"Sum: {sum_fraction}")
print(f"Difference: {diff_fraction}")
print(f"Product: {prod_fraction}")
print(f"Division: {div_fraction}")
#print(f"Power: {pow_fraction}")

# Utilisation des méthodes supplémentaires
print(f"Is zero? {fraction1.is_zero()}")
print(f"Is an integer? {fraction2.is_integer()}")
print(f"Is proper fraction? {fraction3.is_proper()}")
print(f"Is a unit fraction? {fraction1.is_unit()}")
print(f"Is adjacent to fraction3? {fraction1.is_adjacent_to(fraction3)}")

# Utilisation de la méthode as_mixed_number
mixed_number = fraction2.as_mixed_number()
print(f"Fraction 2 as a mixed number: {mixed_number}")

# Conversion en float
float_value = float(fraction3)
print(f"Float value of fraction3: {float_value}")
