
class Band:
    def __init__(self, name=""):
        self.name = name
        self.bands = []

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} ({self.bands})"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, band):
        """Add an instrument to musician's collection."""
        self.bands.append(band)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        if not self.bands:
            return f"{self.name} needs an instrument!"
        return f"{self.bands[0]} is playing: {self.name}"
