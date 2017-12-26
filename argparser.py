#!/usr/local/python-envs/Py3env/bin/python
import argparse

parser = argparse.ArgumentParser()
parser.parse_args()

parser.prog = "Commandline Calendar"
parser.description = "A simple utility to display a Calender."
parser.epilog = "Full documentation available at http://www.example.com"
parser.usage = "To view a simple calender"

parser.add_argument("month", help="The month")
parser.add_argument("year", help="The year")
parser.add_argument('-v','--verbose', help="Print calendar for the month",action="store_true")

parser.parse_args()
