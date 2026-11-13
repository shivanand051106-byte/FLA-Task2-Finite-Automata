# Test Cases for Task 2
from mobile_number_dfa import MobileNumberDFA
from vehicle_number_dfa import VehicleNumberDFA
from date_validation_dfa import DateValidationDFA

def run_tests():
    print("--- Running Task 2 Tests ---")
    
    # Mobile tests
    m_dfa = MobileNumberDFA()
    mobile_tests = [
        ("+919876543210", True),
        ("09876543210", True),
        ("9876543210", True),
        ("5876543210", False),
        ("+914876543210", False),
        ("987654321", False)
    ]
    for num, expected in mobile_tests:
        assert m_dfa.validate(num) == expected, f"Failed mobile: {num}"
    print("Mobile validation tests passed!")

    # Vehicle tests
    v_dfa = VehicleNumberDFA()
    vehicle_tests = [
        ("MH12AB1234", True),
        ("DL3CAB1234", True),
        ("DL3A1234", False),
        ("MH121234", False)
    ]
    for v, expected in vehicle_tests:
        assert v_dfa.validate(v) == expected, f"Failed vehicle: {v}"
    print("Vehicle validation tests passed!")

    # Date tests
    d_dfa = DateValidationDFA()
    date_tests = [
        ("29-02-2024", True),
        ("29-02-2023", False),
        ("31/04/2021", False),
        ("15/08/1947", True)
    ]
    for d, expected in date_tests:
        assert d_dfa.validate(d) == expected, f"Failed date: {d}"
    print("Date validation tests passed!")

if __name__ == '__main__':
    run_tests()
