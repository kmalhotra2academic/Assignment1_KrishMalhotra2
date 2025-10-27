class Observer:
    """
    Observer interface.

    Purpose:
        Defines a single method, `update(message)`, that a Subject calls
        when something important happens.

    Methods:
        update(message): Handle a notification sent by a Subject.
    """
    def update(self, message: str) -> None:
        """Receive notification message from a Subject."""
        raise NotImplementedError("Observer.update must be implemented.")