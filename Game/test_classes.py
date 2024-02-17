import unittest
from classes import *

class Test_Ship_Class(unittest.TestCase):
    def test_get_health(self):
        class_1 = Ship()
        expected_output_1 = 75
        output_1 = class_1.get_health()
        self.assertEqual(expected_output_1, output_1)
        
        class_2 = Ship()
        expected_output_2 = 50
        class_2.health = 50
        output_2 = class_2.get_health()
        self.assertEqual(expected_output_2, output_2)
        
    def test_function1(self):
        player_1 = Player(Ship())
        computer_1 = Computer(Tank())
        expected_output_1 = computer_1.health - 25
        player_1.weapon.function1(player_1, computer_1)
        output_1 = computer_1.health
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Tank())
        computer_2 = Computer(Ship())
        expected_output_2 = player_2.health - 25
        computer_2.weapon.function1(player_2, computer_2)
        output_2 = player_2.health
        self.assertEqual(expected_output_2, output_2)
    
    def test_function2(self):
        player_1 = Player(Ship())
        computer_1 = Computer(Tank())
        expected_output_1 = computer_1.health - 45
        player_1.weapon.function2(player_1, computer_1, 1)
        output_1 = computer_1.health
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Tank())
        computer_2 = Computer(Ship())
        expected_output_2 = player_2.health - 45
        computer_2.weapon.function2(player_2, computer_2, 1)
        output_2 = player_2.health
        self.assertEqual(expected_output_2, output_2)
        
        player_3 = Player(Ship())
        computer_3 = Computer(Tank())
        expected_output_3 = computer_3.health
        player_3.weapon.function2(player_3, computer_3, 2)
        output_3 = computer_3.health
        self.assertEqual(expected_output_3, output_3)
        
        player_4 = Player(Tank())
        computer_4 = Computer(Ship())
        expected_output_4 = player_4.health
        computer_4.weapon.function2(player_4, computer_4, 2)
        output_4 = player_4.health
        self.assertEqual(expected_output_4, output_4)
        
class Test_Tank_Class(unittest.TestCase):
    def test_get_health(self):
        class_1 = Tank()
        expected_output_1 = 100
        output_1 = class_1.get_health()
        self.assertEqual(expected_output_1, output_1)
        
        class_2 = Tank()
        expected_output_2 = 50
        class_2.health = 50
        output_2 = class_2.get_health()
        self.assertEqual(expected_output_2, output_2)
        
    def test_function1(self):
        player_1 = Player(Tank())
        computer_1 = Computer(Plane())
        expected_output_1 = computer_1.health - 20
        player_1.weapon.function1(player_1, computer_1)
        output_1 = computer_1.health
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Plane())
        computer_2 = Computer(Tank())
        expected_output_2 = player_2.health - 20
        computer_2.weapon.function1(player_2, computer_2)
        output_2 = player_2.health
        self.assertEqual(expected_output_2, output_2)
        
    def test_function2(self):
        player_1 = Player(Tank())
        computer_1 = Computer(Ship())
        expected_output_1 = computer_1.health - 35
        player_1.weapon.function2(player_1, computer_1)
        output_1 = computer_1.health
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Ship())
        computer_2 = Computer(Tank())
        expected_output_2 = player_2.health - 35
        computer_2.weapon.function2(player_2, computer_2)
        output_2 = player_2.health
        self.assertEqual(expected_output_2, output_2)
        
        player_3 = Player(Tank())
        computer_3 = Computer(Ship())
        expected_output_3 = True
        player_3.weapon.function2(player_3, computer_3)
        output_3 = player_3.weapon.skip
        self.assertEqual(expected_output_3, output_3)
        
        player_4 = Player(Ship())
        computer_4 = Computer(Tank())
        expected_output_4 = True
        computer_4.weapon.function2(player_4, computer_4)
        output_4 = computer_4.weapon.skip
        self.assertEqual(expected_output_4, output_4)
        
        player_5 = Player(Tank())
        computer_5 = Computer(Ship())
        player_5.weapon.skip = True
        expected_output_5 = computer_5.health
        player_5.weapon.function2(player_5, computer_5)
        output_5 = computer_5.health
        self.assertEqual(expected_output_5, output_5)
        
        player_6 = Player(Tank())
        computer_6 = Computer(Ship())
        player_6.weapon.skip = True
        expected_output_6 = False
        player_6.weapon.function2(player_6, computer_6)
        output_6 = player_6.weapon.skip
        self.assertEqual(expected_output_6, output_6)
        
        player_7 = Player(Ship())
        computer_7 = Computer(Tank())
        computer_7.weapon.skip = True
        expected_output_7 = False
        computer_7.weapon.function2(player_7, computer_7)
        output_7 = computer_7.weapon.skip
        self.assertEqual(expected_output_7, output_7)
        
class Test_Plane_Class(unittest.TestCase):
    def test_get_health(self):
        class_1 = Plane()
        expected_output_1 = 50
        output_1 = class_1.get_health()
        self.assertEqual(expected_output_1, output_1)
        
        class_2 = Plane()
        expected_output_2 = 50
        class_2.health = 50
        output_2 = class_2.get_health()
        self.assertEqual(expected_output_2, output_2)
        
    def test_function1(self):
        player_1 = Player(Plane())
        computer_1 = Computer(Ship())
        expected_output_1 = player_1.health + 20
        player_1.weapon.function1(player_1, computer_1)
        output_1 = player_1.health
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Ship())
        computer_2 = Computer(Plane())
        expected_output_2 = computer_2.health + 20
        computer_2.weapon.function1(player_2, computer_2)
        output_2 = computer_2.health
        self.assertEqual(expected_output_2, output_2)
        
    def test_function2(self):
        player_1 = Player(Plane())
        computer_1 = Computer(Ship())
        expected_output_1 = computer_1.health - 35
        player_1.weapon.function2(player_1, computer_1)
        output_1 = computer_1.health
        self.assertEqual(expected_output_1, output_1)
        
        player_2 = Player(Ship())
        computer_2 = Computer(Plane())
        expected_output_2 = player_2.health - 35
        computer_2.weapon.function2(player_2, computer_2)
        output_2 = player_2.health
        self.assertEqual(expected_output_2, output_2)

if __name__ == "__main__":
    unittest.main()