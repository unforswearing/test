import unittest
from label import Label
from system import System

class TestLabel(unittest.TestCase):
    def test_label_display(self):
        label = Label("Test Label")
        self.assertEqual(label.display(), None)  # Display method prints, returns None

class TestSystem(unittest.TestCase):
    def test_system_start_stop(self):
        system = System("Test System")
        self.assertEqual(system.start(), None)  # Start method prints, returns None
        self.assertEqual(system.stop(), None)   # Stop method prints, returns None

if __name__ == "__main__":
    unittest.main()
