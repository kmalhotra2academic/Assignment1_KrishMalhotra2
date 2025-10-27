class Observer:
    """
    Observer interface.

    Purpose:
        Any class that wants notifications implements `update(message)`.

    """
    def update(self, message: str) -> None:
        """Handle a notification message from a Subject."""
        raise NotImplementedError("Observer.update must be implemented.")