from .observer import Observer

class Subject:
    """
    Subject base class.

    Purpose:
        Manage a list of observers and provide attach, detach, and notify.

    
    """
    def __init__(self) -> None:
        """Start with an empty list of observers."""
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """Register an observer if it's not already attached."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Unregister an observer if present."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Send `message` to all observers.

        Notes:
            A failing observer will be skipped so others still receive updates.
        """
        for obs in list(self._observers):
            try:
                obs.update(message)
            except Exception:
                pass