"""
Password generator module.
Generates cryptographically secure passwords using secrets module.
"""

import secrets, string
from engine.models import PasswordType
from engine.models import PasswordConfig
from engine.validator import PasswordValidator

class PasswordGenerator:
    """
    Generates random passwords based on configuration.
    Uses secrets.randbelow for cryptographically secure randomness.
    """

    def __init__(self, config: PasswordConfig, validator: PasswordValidator):
        """
        Initialize generator with configuration.
    
        Args:
            config: PasswordConfig object containing all settings.
        """
        self._config = config
        self._validator = validator

    def _build_character_pool(self):
        """
        Build character pool based on configuration.
    
        Returns:
            String containing allowed characters.
    
        Raises:
            ValueError: If character pool is empty.
        """
        
        pool = ""
        
        if(self._config.use_lowercase):
            pool = pool + string.ascii_lowercase
        if(self._config.use_uppercase):
            pool = pool + string.ascii_uppercase
        if(self._config.use_digits):
            pool = pool + string.digits
        if(self._config.use_symbols):
            pool = pool + string.punctuation
        if(self._config.exclude_ambiguous):
            ambiguous = "0OIl1"

            clean_pool = ""
            for char in pool:
                if char not in ambiguous:
                    clean_pool = clean_pool + char
            pool = clean_pool
        if not pool:
            raise ValueError("The pool cannot be empty.")
        return pool
    
    def _generate_raw(self):
        pool = self._build_character_pool()
        pool_length = len(pool)

        result = ""

        for _ in range(self._config.length):
            index = secrets.randbelow(pool_length)
            result = result + pool[index]
        return result
    
    def generate(self):
        """
        Generate a password that meets configuration requirements.
    
        Returns:
            Valid password string.
    
        Note:
            This method uses retry mechanism with validator.
            Maximum attempts are limited to prevent infinite loops.
        """
        for _ in range(10):
            password = self._generate_raw()
            if self._validator.validate(password):
                return password

        raise RuntimeError("Could not generate valid password")