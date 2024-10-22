"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Create a new generator, starting at the given number."""
        self.start = start
        self.next = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"


    def generate(self):
        """Return the next sequential number."""
        current = self.next
        self.next += 1
        return current

    def reset(self):
        """Reset the serial number back to the original start number."""
        self.next = self.start

