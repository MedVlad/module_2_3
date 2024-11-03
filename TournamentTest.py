import unittest
from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results = tour.start().copy()
        MaxKey = max(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[MaxKey] == 'Ник')

    def test2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results = tour.start().copy()
        MaxKey = max(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[MaxKey] == 'Ник')

    def test3(self):
        tour = Tournament(90, self.runner1,self.runner2, self.runner3)
        TournamentTest.all_results = tour.start().copy()
        MaxKey = max(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[MaxKey] == 'Ник')

    def testLogic(self):
        #for i in range(90):
            TournamentTest.all_results = {}.copy()
            self.runner1 = Runner('Усэйн', 10)
            self.runner2 = Runner('Андрей', 9)
            self.runner3 = Runner('Ник', 3)
            tour = Tournament(7, self.runner1, self.runner2, self.runner3)
            TournamentTest.all_results = tour.start().copy()
            MaxKey = max(TournamentTest.all_results)
            self.assertTrue(TournamentTest.all_results[MaxKey] == 'Ник', f"ошибка ")



    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    unittest.main()
