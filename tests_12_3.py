from unittest import TextTestRunner
from suite_12_3 import runnerST

runner = TextTestRunner(verbosity=2)
runner.run(runnerST)
