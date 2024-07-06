class System:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"System {self.name} starting...")

    def stop(self):
        print(f"System {self.name} stopping...")

if __name__ == "__main__":
    system = System("Main System")
    system.start()
    system.stop()
