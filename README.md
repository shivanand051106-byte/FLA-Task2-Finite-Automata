# FLA Task 2: Deterministic Finite Automata (DFA) Applications

This repository contains Python implementations of Deterministic Finite Automata (DFA) designed to validate various structured input formats such as Indian mobile numbers, vehicle registration numbers, and calendar dates.

## Features & DFA Modules

1. **Indian Mobile Number Validator (`mobile_number_dfa.py`)**
   - Validates Indian mobile numbers.
   - Supports optional prefix of `+91` or `0` followed by a 10-digit number starting with 6, 7, 8, or 9.
   
2. **Vehicle Registration Number Validator (`vehicle_number_dfa.py`)**
   - Validates Indian vehicle registration numbers.
   - Supports standard formats (e.g., `MH12AB1234`) and alphanumeric state codes (e.g., `DL3CAB1234`).
   - Rejects improper structures (e.g., `DL3A1234`).

3. **Date Validator (`date_validation_dfa.py`)**
   - Validates date strings in `DD-MM-YYYY` or `DD/MM/YYYY` formats.
   - Enforces calendar constraints, including leap year regulations.

## Project Structure
```
├── mobile_number_dfa.py     # Mobile number DFA logic
├── vehicle_number_dfa.py    # Vehicle registration number DFA logic
├── date_validation_dfa.py   # Date formatting and calendar validation
├── test_cases.py            # Diagnostic assertions for test compliance
├── main.py                  # Entrypoint script executing the tests
└── README.md                # Project documentation
```

## Running the Program
To run the validation test suites:
```bash
python main.py
