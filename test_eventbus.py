# test_eventbus.py
"""
Tests for EventBus module.
"""

import unittest
from eventbus import EventBus

class TestEventBus(unittest.TestCase):
    """Test cases for EventBus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EventBus()
        self.assertIsInstance(instance, EventBus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EventBus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
