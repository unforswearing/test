class View:
    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Rendering view: {self.name}")

if __name__ == "__main__":
    view = View("Main View")
    view.render()
