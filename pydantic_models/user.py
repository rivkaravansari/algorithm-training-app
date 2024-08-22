from pydantic_models.base import Base
from pydantic import field_validator, EmailStr
import re


class User(Base):
    username: str
    password: str
    email: EmailStr

    @field_validator("username")
    def validate_username(cls, username):
        """ Validate the username according to rules."""
        if len(username) < 3 or len(username) > 20:
            raise ValueError('Username must be between 3 and 20 characters long')
        if not re.match(r'^[A-Za-z][A-Za-z0-9_]*$', username):
            raise ValueError('Username must start with a letter and contain only letters, numbers, and underscores')
        return username

    @field_validator('password')
    def validate_password(cls, password):
        """Validate the password according to security rules."""
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', password):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', password):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError('Password must contain at least one special character')
        return password
