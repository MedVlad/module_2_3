import logging
import unittest
from unittest import TestCase
from rt_with_exceptions import Runner


class RunnerTest(TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding="UTF-8",
                            format="%(asctime)s | %(levelname)s | %(message)s")
    def test_run1(self):

        try:
            runner2 = Runner(1, 10)
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
           logging.warning("Неверный тип данных для объекта Runner")
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_walk1(self):
        try:
            runner1 = Runner('runner1', -5)
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        except ValueError:
            logging.warning("Неверная скорость для Runner")


if __name__ == "__main__":
    unittest.main()
