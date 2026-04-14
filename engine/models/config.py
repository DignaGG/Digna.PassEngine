"""
Password configuration dataclass.
Holds all settings for password generation and validation.
"""

from dataclasses import dataclass

@dataclass
class PasswordConfig:
    """
    Configuration container for password generator and validator.
    
    Attributes:
        length: Password length (default 12)
        use_uppercase: Include A-Z (default True)
        use_lowercase: Include a-z (default True)
        use_digits: Include 0-9 (default True)
        use_symbols: Include punctuation (default False)
        exclude_ambiguous: Remove 0, O, I, l, 1 (default True)
    """

    length: int = 12
    use_uppercase: bool = True
    use_lowercase: bool = True
    use_digits: bool = True
    use_symbols: bool = False
    exclude_ambiguous: bool = True