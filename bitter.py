#!/usr/bin/env python
'''
File: bitter.py
Author: Spencer Rathbun
Date: 04/30/2012
Description: Visually demonstrate bitwise shifting on the command line, on the fly.
'''
import curses, curses.ascii

top = {"position":(6,18), "value":0}
bottom = {"position":(10,18), "value":0}
total = {"position":(0,0), "value":0}
currField = top
bitop = "&"

def printVals(stdscr):
	global currField, top, bottom, total
	total["value"] = eval("{:} {:} {:}".format(top["value"], bitop, bottom["value"]))
	stdscr.addstr("------------------\n")
	stdscr.addstr("|{:^16}| {:}\n".format(bin(top["value"])[2:], top["value"]))
	stdscr.addstr("------------------\n")
	stdscr.addstr("         {0}        \n".format(bitop))
	stdscr.addstr("------------------\n")
	stdscr.addstr("|{:^16}| {:}\n".format(bin(bottom["value"])[2:], bottom["value"]))
	stdscr.addstr("------------------\n")
	stdscr.addstr("          =       \n")
	stdscr.addstr("------------------\n")
	stdscr.addstr("|{:^16}| {:}\n".format(bin(total["value"])[2:], total["value"]))
	stdscr.addstr("------------------\n")
	stdscr.move(currField["position"][0], currField["position"][1])
	stdscr.cursyncup()

def switchField():
	global currField, top, bottom
	if currField == top:
		currField = bottom
	else:
		currField = top

def switchBitOp():
	global bitop
	ops = [ "&", "^", "|", "<<", ">>" ]
	current = ops.index(bitop)
	if current == len(ops)-1:
		bitop = ops[0]
	else:
		bitop = ops[current+1]

def doAction(key):
	if key == curses.ascii.TAB: switchField()
	elif curses.ascii.isdigit(key): currField["value"] += int(curses.ascii.unctrl(key))
	elif key == curses.ascii.SP: switchBitOp()
	elif key == ord('q'): return True # Exit the while()
	elif key == ord('Q'): return True # Exit the while()
	return False

def main(stdscr):
	stdscr.addstr("Inputs for this program:\n")
	stdscr.addstr("Q/q: quit\tTab: switch input box\n")
	stdscr.addstr("Numbers: add to input box\td: delete contents\n")
	stdscr.addstr("\n\n")
	printVals(stdscr)
	stdscr.refresh()
	while 1:
		c = stdscr.getch()
		if doAction(c):
			break
		stdscr.move(5,0)
		stdscr.clrtobot()
		printVals(stdscr)
		stdscr.refresh()


if __name__ == '__main__':
	curses.wrapper(main)
