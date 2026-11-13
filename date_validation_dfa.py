# DFA for Date Format Validation (DD-MM-YYYY or DD/MM/YYYY)

class DateValidationDFA:
    def validate(self, date_str: str) -> bool:
        # Format expected: DD-MM-YYYY or DD/MM/YYYY
        # We will parse and transition. If format satisfies, we also enforce calendar constraints.
        if len(date_str) != 10:
            return False
        
        # Transition verification for template: NN-NN-NNNN or NN/NN/NNNN
        separator = date_str[2]
        if separator not in ['-', '/']:
            return False
        
        for i, char in enumerate(date_str):
            if i in [2, 5]:
                if char != separator:
                    return False
            else:
                if not char.isdigit():
                    return False
                    
        day = int(date_str[0:2])
        month = int(date_str[3:5])
        year = int(date_str[6:10])
        
        if month < 1 or month > 12:
            return False
            
        # Simple leap year rule
        is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        days_in_month = [0, 31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if day < 1 or day > days_in_month[month]:
            return False
            
        return True
