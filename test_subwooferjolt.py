# test_subwooferjolt.py
"""
Tests for SubwooferJolt module.
"""

import unittest
from subwooferjolt import SubwooferJolt

class TestSubwooferJolt(unittest.TestCase):
    """Test cases for SubwooferJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SubwooferJolt()
        self.assertIsInstance(instance, SubwooferJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SubwooferJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
