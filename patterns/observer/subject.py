from patterns.observer.observer import Observer

class Subject:
    """
    Subject base class.

    Purpose:
        Keeps a list of observers and provides three simple operations:
        attach, detach, and notify.

    Attributes:
        _observers (list[Observer]): Registered listeners.
    """
    def __init__(self) -> None:
        """Start with an empty list of observers."""
        self._observers: list[Observer] = []

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
        Errors:
            If an observer raises during update, we skip it so others still run.
        """
        for obs in self._observers:
            try:
                obs.update(message)
            except Exception:
                pass