EARTH_IN_SECONDS = 31557600
MERCURY_PERIOD = 0.2408467
VENUS_PERIOD = 0.61519726
MARS_PERIOD = 1.8808158
JUPITER_PERIOD = 11.862615
SATURN_PERIOD = 29.447498
URANUS_PERIOD = 84.016846
NEPTUNE_PERIOD = 164.79132

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        age = self.seconds / EARTH_IN_SECONDS
        return round(age,2)

    def on_mercury(self):
        age = self.seconds / (EARTH_IN_SECONDS * MERCURY_PERIOD)
        return round(age,2)

    def on_venus(self):
        age = self.seconds / (EARTH_IN_SECONDS * VENUS_PERIOD)
        return round(age,2)

    def on_mars(self):
        age = self.seconds / (EARTH_IN_SECONDS * MARS_PERIOD)
        return round(age,2)

    def on_jupiter(self):
        age = self.seconds / (EARTH_IN_SECONDS * JUPITER_PERIOD)
        return round(age,2)

    def on_saturn(self):
        age = self.seconds / (EARTH_IN_SECONDS * SATURN_PERIOD)
        return round(age,2)

    def on_uranus(self):
        age = self.seconds / (EARTH_IN_SECONDS * URANUS_PERIOD)
        return round(age,2)

    def on_neptune(self):
        age = self.seconds / (EARTH_IN_SECONDS * NEPTUNE_PERIOD)
        return round(age,2)
    
        
