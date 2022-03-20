"""Exceptions module contains all the needed custom execptions."""


class ValidationError(Exception):
    """Custom exception class for validation errors."""

    def __init__(self, value: int, message: str) -> None:
        """
        value: input value that caused the validation error.
        message: The error message which comes from the original exception.
        """
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        """String representaion for the valication error."""
        return f'{self.value} is invalid value for {self.message}'
