import unittest
from poker_hand import get_combination, get_correct_cards_set


class CombinationTest(unittest.TestCase):

    def test_get_combination(self):
        self.assertEqual(get_combination(get_correct_cards_set('9C JC QC KC AC')), 'Flush')
        self.assertEqual(get_combination(get_correct_cards_set('9C JC QC KC 9D')), 'Pair')
        self.assertEqual(get_combination(get_correct_cards_set('AC JC QC KC AD')), 'Pair')
        self.assertEqual(get_combination(get_correct_cards_set('2C 2S QC KC 9D')), 'Pair')
        self.assertEqual(get_combination(get_correct_cards_set('10H JD QD KS AC')), 'Straight')
        self.assertEqual(get_combination(get_correct_cards_set('2C 3C 4C 5C AC')), 'Straight Flush')
        self.assertEqual(get_combination(get_correct_cards_set('6S 7S 8S 9S 10S')), 'Straight Flush')
        self.assertEqual(get_combination(get_correct_cards_set('10C 7D 8S 9H 6C')), 'Straight')
        self.assertEqual(get_combination(get_correct_cards_set('2C 3D 4S 5H AC')), 'Straight')
        self.assertEqual(get_combination(get_correct_cards_set('AC 3D 9C 5C 6C')), 'High Card')
        self.assertEqual(get_combination(get_correct_cards_set('AC 2H 3D 4C 5C')), 'Straight')
        self.assertEqual(get_combination(get_correct_cards_set('AC QC QC 10C AC')), 'Flush')
        self.assertEqual(get_combination(get_correct_cards_set('10H JH QH KH AH')), 'Royal Flush')
        self.assertEqual(get_combination(get_correct_cards_set('JS QS AS KS 10S')), 'Royal Flush')
        self.assertEqual(get_combination(get_correct_cards_set('10S 10D 10C KD AD')), 'Three of a Kind')
        self.assertEqual(get_combination(get_correct_cards_set('AC 10D 10C AS AD')), 'Full House')
        self.assertEqual(get_combination(get_correct_cards_set('AC 2D 2C AS AD')), 'Full House')
        self.assertEqual(get_combination(get_correct_cards_set('2C 10D 10C 2S 2D')), 'Full House')
        self.assertEqual(get_combination(get_correct_cards_set('10C JS AC 10D AH')), 'Two Pairs')
        self.assertEqual(get_combination(get_correct_cards_set('10C 10S 10D 10D AH')), 'Four of a Kind')
        self.assertEqual(get_combination(get_correct_cards_set('AC AS 10D AD AH')), 'Four of a Kind')
        self.assertEqual(get_combination(get_correct_cards_set('9C JC QH KC AC')), 'High Card')
        self.assertEqual(get_combination(get_correct_cards_set('10C AS 10H AD AC')), 'Full House')
        self.assertEqual(get_combination(get_correct_cards_set('10H AC QD KS JH')), 'Straight')