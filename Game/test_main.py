import unittest
from main import *

class Test_Main(unittest.TestCase):
    def test_validate_input_and_convert(self):
        input_1 = "1"
        expected_output_1 = "Ship"
        output_1 = validate_input_and_convert(input_1)
        self.assertEqual(expected_output_1, output_1)
        
        input_2 = "2"
        expected_output_2 = "Plane"
        output_2 = validate_input_and_convert(input_2)
        self.assertEqual(expected_output_2, output_2)
        
        input_3 = "3"
        expected_output_3 = "Tank"
        output_3 = validate_input_and_convert(input_3)
        self.assertEqual(expected_output_3, output_3)
        
    def test_computerSelection(self):
        player_1 = Player(Ship())
        unexpected_output_1 = "Ship"
        output_1 = computerSelection(player_1)
        self.assertNotEqual(unexpected_output_1, output_1)
        
        player_2 = Player(Plane())
        unexpected_output_2 = "Plane"
        output_2 = computerSelection(player_2)
        self.assertNotEqual(unexpected_output_2, output_2)
        
        player_3 = Player(Tank())
        unexpected_output_3 = "Tank"
        output_3 = computerSelection(player_3)
        self.assertNotEqual(unexpected_output_3, output_3)
        
    def test_player_skip(self):
        player_1 = Player(Tank())
        expected_output_1 = True
        player_1.weapon.skip = True
        output_1 = player_skip(player_1)
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Tank())
        expected_output_2 = False
        player_2.weapon.skip = False
        output_2 = player_skip(player_2)
        self.assertEqual(expected_output_2, output_2)
        
    def test_computer_skip(self):
        computer_1 = Computer(Tank())
        expected_output_1 = True
        computer_1.weapon.skip = True
        output_1 = computer_skip(computer_1)
        self.assertEqual(expected_output_1, output_1)
        
        computer_2 = Computer(Tank())
        expected_output_2 = False
        computer_2.weapon.skip = False
        output_2 = computer_skip(computer_2)
        self.assertEqual(expected_output_2, output_2)
        
    def test_computer_attack(self):
        player_1 = Player(Ship())
        computer_1 = Computer(Tank())
        expected_output_1 = 1
        output_1 = computer_attack(player_1, computer_1, 1)
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Ship())
        computer_2 = Computer(Tank())
        expected_output_2 = 2
        output_2 = computer_attack(player_2, computer_2, 2)
        self.assertEqual(expected_output_2, output_2)
        
    def test_validate_attack_options(self):
        player_1 = Player(Ship())
        computer_1 = Computer(Tank())
        expected_output_1 = 1
        output_1 = validate_attack_options("1", player_1, computer_1)
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Ship())
        computer_2 = Computer(Tank())
        expected_output_2 = 2
        output_2 = validate_attack_options("2", player_2, computer_2)
        self.assertEqual(expected_output_2, output_2)

if __name__ == "__main__":
    unittest.main()