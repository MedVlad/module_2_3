import unittest
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# runner = TextTestRunner(verbosity=2)
# runner.run(runnerST)
