class Label:
    def __init__(self, text):
        self.text = text

    def display(self):
        print(f"Label: {self.text}")

if __name__ == "__main__":
    label = Label("Sample Label")
    label.display()
