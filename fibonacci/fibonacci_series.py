# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, October 2020

"""This script is used to perform FibonacciSeries.

- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""

import os
import sys
import argparse
import itertools
import logging
from collections import Counter

class FibonacciSeries:

    """ Class FibonacciSeries"""

    def __init__(self, number):
        """The init function of the class FibonacciSeries.

        :param (parsed arg) number
        :type str
        :param (class instance) list_below_range
        :type list
        """

        self.number = number
        self.list_below_range = []
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)

    def find_fibonacci_series(self, number):
        """This method is used to find the series of fibonacci for the given number. This method
        will be called recursively.

        :param number
        :type int
        """

        if number == 0:
            return 2
        elif number == 1:
            return 3
        else:
            return (self.find_fibonacci_series(number - 1) + self.find_fibonacci_series(number - 2))

    def prepare_series_in_range(self):
        """This method is used to find the series of fibonacci numbers below the range of given
        number.
        """

        actual_series = []
        for idx in range(self.number):
            actual_series.append(self.find_fibonacci_series(idx))

        for idx, value in enumerate(actual_series):
            if actual_series[idx] < self.number:
                self.list_below_range.append(value)

    def prepare_combinations(self):
        """This method is used to prepare the combinations.

        max_width identifies maximum values in a combinations
        for ex: 11, 2 occurs 5 times i,e 2,2,2,2,2,1
        list_unique_values holds only unique values
        list_occurences holds the occurrences of fibonacci numbers in order
        list_fib_series holds the list of fibonacci numbers as per the occurrence
        list_sum_fib_numbers holds only those values whose sum matches the given number
        :rtype: list
        """

        max_width = int(self.number/2) + 1
        list_unique_values = list(set(self.list_below_range))
        list_occurences = []
        list_fib_series = []
        list_sum_fib_numbers = []

        # Find occurence of individual fibonacci number
        for idx, value in enumerate(list_unique_values):
            list_occurences.append(int(self.number/value))

        # Prepare the list of fibonacci number as per their occurrences
        for index in range(len(list_occurences)):
            list_fib_series.extend(
                [list_unique_values[index] for times in range(list_occurences[index])])

        for item in range(max_width):
            # Prepare combinations of all elements in the list list_fib_series
            combinations = list(itertools.permutations(list_fib_series, item))

            # Prepare combinations of series of fibonacci numbers whose sum matches the number
            for item_comb in combinations:
                if sum(list(item_comb)) == self.number:
                    list_sum_fib_numbers.append(list(item_comb))

        count_fibo_series = Counter([tuple(sorted(x)) for x in list_sum_fib_numbers])
        required_list = [list(k) for k, v in count_fibo_series.items() if v >= 1]

        self.logger.info('All possible combinations:')

        for item in required_list:
            self.logger.info(item)

        return required_list

    def run(self):
        """This method is used to handle the logic"""

        return_code = ''

        if self.number.isdigit():
            self.number = int(self.number)
            if self.number > 0 and self.number < 2:
                self.logger.info("Series is {}".format(self.find_fibonacci_series(self.number)))
            else:
                # Prepare series of fibonacci number in the range
                self.prepare_series_in_range()
                # Prepare combinations
                return_code = self.prepare_combinations()
        elif self.number.replace('.','',1).isdigit():
            self.logger.error("Entered value is float. Please enter integer number.")
            return_code = "Try again with valid integer"
        elif self.number.startswith('-'):
            #TODO:
            self.logger.error("Entered value is negative integer. Please enter integer number.")
            return_code = "Try again with valid integer"
        else:
            self.logger.error("Entered value is str. Please enter integer number.")
            return_code = "Try again with valid integer"
        return return_code

def main(parsed_number=""):
    """ This method is required because
        1. it can be called from fibonacci.py as a submodule
        2. it can be called standalone from command line.
    """
    parser = argparse.ArgumentParser(description="FibonacciSeries")
    parser.add_argument('-n', '--number', type=str, help='A valid number')

    logging.basicConfig(level=logging.DEBUG)

    parsed_number = str(parsed_number)
    if not parsed_number.strip():
        args = parser.parse_args()
        try:
            logging.info("Script is called directly {}".format(os.path.dirname(sys.argv[0])))
            submodule = FibonacciSeries(args.number)
            return submodule.run()
        except:
            logging.error("Error printing arguments")
    else:
        logging.info("Argument passed from fibonacci.py: number {}".format(parsed_number))

        args = parser.parse_args()
        args.number = parsed_number
        submodule = FibonacciSeries(args.number)
        return submodule.run()

if __name__ == '__main__':
    main()
