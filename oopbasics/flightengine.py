class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("starting airbus engine")


class BoingEngine:
    def start(self):
        print("starting boing engine")


ae = AirbusEngine()
f1 = Flight(ae)
f1.startEngine()

b = BoingEngine()
f2 = Flight(b)
f2.startEngine()
