# DFA for Indian Mobile Number Validation
# Rules:
# 1. Can start with optionally '+91' or '0'
# 2. Must be followed by a 10-digit number starting with 6, 7, 8, or 9

class MobileNumberDFA:
    def __init__(self):
        # States: 
        # q0: start
        # q1: read '+'
        # q2: read '+9'
        # q3: read '+91' or '0'
        # q4: read first digit (6-9) of 10-digit number
        # q5-q13: reading remaining 9 digits
        # q13 is the only accepting state
        self.num_states = 14

    def validate(self, number: str) -> bool:
        state = 0
        digit_count = 0
        
        for char in number:
            if state == 0:
                if char == '+':
                    state = 1
                elif char == '0':
                    state = 3
                elif char in '6789':
                    state = 4
                    digit_count = 1
                else:
                    return False
            elif state == 1:
                if char == '9':
                    state = 2
                else:
                    return False
            elif state == 2:
                if char == '1':
                    state = 3
                else:
                    return False
            elif state == 3:
                if char in '6789':
                    state = 4
                    digit_count = 1
                else:
                    return False
            elif state == 4:
                if char.isdigit():
                    digit_count += 1
                    if digit_count == 10:
                        state = 13
                else:
                    return False
            elif state == 13:
                # Already completed 10 digits, any extra character makes it invalid
                return False
        
        return state == 13
