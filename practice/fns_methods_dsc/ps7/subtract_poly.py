def subtract_polynomials(polynomial_1, polynomial_2):
    all_coefficients = {}
    all_coefficients.update(polynomial_1)

    for key, value in polynomial_2.items():
        if key in all_coefficients:
            all_coefficients[key] -= value
        else:
            all_coefficients[key] = -value

    representation = get_representation(all_coefficients)
    print(representation)


def get_representation(polynomial_coefficients):
    representation = ""
    all_powers = polynomial_coefficients.keys()
    max_power = max(all_powers)
    for power in sorted(all_powers, reverse=True):
        coefficient = polynomial_coefficients[power]
        if power == max_power:
            coefficient = '' if coefficient == 1 else '-' if coefficient == -1 else coefficient
        else:
            if coefficient > 0:
                representation += " + "
            elif coefficient < 0:
                representation += " - "
            else:
                continue
            coefficient = abs(coefficient)

        if coefficient == 1:
            coefficient = ''
        if power > 1 and coefficient != 0:
            representation += "{}x^{}".format(coefficient, power)
        elif power == 1 and coefficient != 0:
            representation += "{}x".format(coefficient)
        elif power == 0 and coefficient != 0:
            representation += "{}".format(
                abs(polynomial_coefficients[power]))
        if representation == '':
            representation = '0'
    return representation


if __name__ == "__main__":
    first_polynomial_coefficients_number = int(input())
    first_polynomial_coefficients = dict()
    for i in range(first_polynomial_coefficients_number):
        power, coefficient = input().split()
        first_polynomial_coefficients[int(power)] = int(coefficient)

    second_polynomial_coefficients_number = int(input())
    second_polynomial_coefficients = dict()
    for _ in range(second_polynomial_coefficients_number):
        power, coefficient = input().split()
        second_polynomial_coefficients[int(power)] = int(coefficient)

    subtract_polynomials(first_polynomial_coefficients,
                         second_polynomial_coefficients)