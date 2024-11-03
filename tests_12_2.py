import unittest
from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results = tour.start().copy()
        MaxKey = max(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[MaxKey] == 'Ник')

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results = tour.start().copy()
        MaxKey = max(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[MaxKey] == 'Ник')

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test3(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results = tour.start().copy()
        MaxKey = max(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[MaxKey] == 'Ник')



    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")



if __name__ == "__main__":
    unittest.main()
