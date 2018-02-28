class Resistor(object):
    def __init__(self, ohms):
        self._ohms = ohms
        self._voltage = 0
        self._current = 0

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError("%f ohms must be > 0" % ohms)
        self._ohms = ohms

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self._current = self._voltage / self._ohms


if __name__ == '__main__':
    r1 = Resistor(10)
    r1.voltage = 20
    print(r1._current)
    r1.ohms = -1