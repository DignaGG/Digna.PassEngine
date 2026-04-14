"""
Password validator module.
Checks if generated password meets all security requirements.
"""

import string
from engine.models import PasswordConfig

class PasswordValidator:
    """
    Validates passwords against configuration rules.
    Returns True only if all requirements are satisfied.
    """
    def __init__(self, config):
        """
        Initialize validator with configuration.
    
        Args:
            config: PasswordConfig object containing validation rules.
        """

        config: PasswordConfig
        self._config = config

    def validate(self, password:str):
        """
        Check if password meets all configured criteria.
    
        Args:
            password: Password string to validate.
    
        Returns:
            True if password passes all checks, False otherwise.
    
        Checks performed:
            - Minimum length
            - Uppercase letter (if required)
            - Lowercase letter (if required)
            - Digit (if required)
            - Symbol (if required)
            - No ambiguous characters (if excluded)
        """
        if(len(password) < self._config.length):
            return False
        if(self._config.use_uppercase):
            has_upper = False

            for char in password:
                if char.isupper():
                    has_upper = True
                    break
            if not has_upper:
                return False
        if(self._config.use_lowercase):
            has_lower = False

            for char in password:
                if char.islower():
                    has_lower = True
                    break
            if not has_lower:
                return False
        if(self._config.use_digits):
            has_digits = False

            for char in password:
                if char.isdigit():
                    has_digits = True
                    break
            if not has_digits:
                return False
        if(self._config.use_symbols):
            has_symbols = False

            for char in password:
                if char in string.punctuation:
                    has_symbols = True
                    break
            if not has_symbols:
                return False
        if(self._config.exclude_ambiguous):
            for char in password:
                if char in "0OIl1":
                    return False
        return True