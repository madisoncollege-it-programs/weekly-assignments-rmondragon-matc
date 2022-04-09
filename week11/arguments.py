#!/usr/bin/env python3

import argparse
import sys
parser = argparse.ArgumentParser(description='This is Ryley Mondragons Script.')

if len(sys.argv) == 1:
    print(parser.print_help())


parser.add_argument("echo", help="", )


parser.add_argument('-i', '--an-integer', dest='varInteger',  default=10, type=int,
help='Enter a simple integer')

parser.add_argument('-s', '--astring', dest='varString', default='hello', type=str,
help='Enter a simple string')

parser.add_argument('-d', '--afloat', dest='varFloat', default=10.0, type=float, 
help='Enter a simple float')

parser.add_argument('-t', action='store_true',
                    default=False,
                    dest='boolean_t',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false',
                    default=True,
                    dest='boolean_f',
                    help='Set a switch to false')

parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')




args = parser.parse_args()

print((parser.parse_args()).varInteger)
print((parser.parse_args()).varString)
print((parser.parse_args()).varFloat)
print('boolean_t        = {!r}'.format(args.boolean_t))
print('boolean_f        = {!r}'.format(args.boolean_f))

