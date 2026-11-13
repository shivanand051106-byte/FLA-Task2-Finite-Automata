from mobile_number_dfa import MobileNumberDFA
from vehicle_number_dfa import VehicleNumberDFA
from date_validation_dfa import DateValidationDFA
import test_cases

def main():
    print("=========================================")
    print("Deterministic Finite Automata Applications")
    print("=========================================")
    test_cases.run_tests()

if __name__ == '__main__':
    main()
