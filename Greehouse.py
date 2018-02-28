
class Event(object):
    events = [] # static

    def __init__(self, action, time):
        self.action = action
        self.time = time
        Event.events.append(self)

    def __cmp__ (self):
        "So sort() will compare only on time."
        return self.time

    def run(self):
        print("%.2f: %s" % (self.time, self.action))

    @staticmethod
    def run_events():
        Event.events.sort(key=Event.__cmp__);
        for e in Event.events:
            e.run()
def create_mc(description):
    "Create subclass using the 'type' metaclass"
    class_name = "".join(x.capitalize() for x in description.split())
    def __init__(self, time):
        Event.__init__(self, description + " [mc]", time)
    globals()[class_name] = \
        type(class_name, (Event,), dict(__init__ = __init__))

def create_exec(description):
    "Create subclass by exec-ing a string"
    class_name = "".join(x.capitalize() for x in description.split())
    klass = """
class %s(Event):
    def __init__(self, time):
        Event.__init__(self, "%s [exec]", time)
""" % (class_name, description)
    exec (klass,globals())
    
    

if __name__ == "__main__":
    descriptions = ["Light on", "Light off", "Water on", "Water off",
                    "Thermostat night", "Thermostat day", "Ring bell"]
    initializations = "ThermostatNight(5.00); LightOff(2.00); \
        WaterOn(3.30); WaterOff(4.45); LightOn(1.00); \
        RingBell(7.00); ThermostatDay(6.00)"
    [create_mc(dsc) for dsc in descriptions]
    exec (initializations)
    [create_exec(dsc) for dsc in descriptions]
    exec (initializations)
    Event.run_events()
