# DFA for Indian Vehicle Registration Number Validation
# This version cleanly handles standard formats and ensures improper mixes like DL3A1234 are rejected.

class VehicleNumberDFA:
    def validate(self, vehicle_num: str) -> bool:
        state = 0
        digits_in_serial = 0

        for char in vehicle_num:
            if state == 0:
                # First letter of State Code
                if char.isalpha():
                    state = 1
                else:
                    return False
            elif state == 1:
                # Second letter of State Code
                if char.isalpha():
                    state = 2
                else:
                    return False
            elif state == 2:
                # First digit of District Code
                if char.isdigit():
                    state = 3
                else:
                    return False
            elif state == 3:
                # Can be:
                # - Second digit of District Code (e.g., MH12... -> state 4)
                # - A letter if District Code is alphanumeric with 1 digit (e.g., DL3C... -> state 5)
                if char.isdigit():
                    state = 4
                elif char.isalpha():
                    state = 5
                else:
                    return False
            elif state == 4:
                # After standard 2-digit district code (e.g. MH12)
                # Expecting first letter of Series Code
                if char.isalpha():
                    state = 6
                else:
                    return False
            elif state == 5:
                # After alphanumeric district (e.g. DL3C)
                # Must be followed by 1 or 2 letter Series Code.
                # So we expect the start of the Series Code here.
                if char.isalpha():
                    state = 6
                else:
                    return False
            elif state == 6:
                # We have read 1 letter of the Series Code.
                # We can either read another letter (completing a 2-letter series)
                # or start reading the 4 digits of the unique registration number.
                if char.isalpha():
                    state = 60
                elif char.isdigit():
                    state = 7
                    digits_in_serial = 1
                else:
                    return False
            elif state == 60:
                # We have read a 2-letter series. Must transition to digits.
                if char.isdigit():
                    state = 7
                    digits_in_serial = 1
                else:
                    return False
            elif state == 7:
                if char.isdigit():
                    digits_in_serial += 1
                    if digits_in_serial == 4:
                        state = 10
                else:
                    return False
            elif state == 10:
                return False

        return state == 10
