"""
Password type enumeration.
Defines available password generation strategies.
"""

from enum import Enum

class PasswordType(Enum):
    """
    Represents different password complexity levels.
    NUMERIC: Only digits (0-9)
    ALPHANUMERIC: Letters and digits
    STRONG: Letters, digits, and symbols
    """
    
    NUMERIC = 1
    ALPHANUMERIC = 2
    STRONG = 3