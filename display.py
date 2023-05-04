import curses
from curses.textpad import Textbox
from enum import Enum
from http.client import GONE
import sys
if sys.platform == "linux":
    from getch import getch, getche
if sys.platform == "win32":
    from msvcrt import getch, getche 
    


class prop:
    
	def __init__(self, str_inp, prp_lvl, argProp):
		self.str_inp = str_inp
		self.level = prp_lvl
		self.argProp = argProp
	def dec_prop(self):
		pass 
	def get_level(self):
		pass
	
class prop_table:
	def __init__(self, prop_list = [prop(" ", 0, True), prop(" ", 0, False)]):
		self.lines = 0
		self.prop_list = prop_list
		self.cur_point = 0
	def __getitem__(self, num):
		return self.prop_list[num]
	def __setitem__(self, num, someProp: prop):
		self.prop_list[num] = someProp
	def print(self):
		for i in range(len(self.prop_list)):

			print("║ " + ("║ " * self.prop_list[i].level) + self.prop_list[i].str_inp)
			if i < (len(self.prop_list) - 1):
				if (self.prop_list[i].argProp and (not self.prop_list[i + 1].argProp)):
					print(("║ " * self.prop_list[i].level) + "╠═════════════════════════════════════")
	
	def insert(self, inp, index,  prpLvl, argLvl):
		self.prop_list.insert(index, prop(inp, prpLvl, argLvl))
	def length(self):
		return len(self.prop_list)
		
def get_stdinput():
	new_prpTbl = prop_table()
	new_prpTbl.print()
	inp = input()
	while inp.lower() != "stop":
		
		last_tab = new_prpTbl.length()
		if new_prpTbl.cur_point == last_tab:
			last_tab -= 1
			print("first")
			curlevel = new_prpTbl[last_tab].level
			curargLvl = new_prpTbl[last_tab].argProp
			if inp[:1] == "\t":
				new_prpTbl.prop_list.append(prop(inp[1:], curlevel + 1, True))
				new_prpTbl.prop_list.append(prop(" ", curlevel + 1, False))
			elif inp[:2] == "/b":
				new_prpTbl.prop_list.append(prop(inp[2:], curlevel - 1, curargLvl))
			else:
				new_prpTbl.prop_list.append(prop(inp, curlevel, curargLvl))
		else:
			print("second")
			
			new_prpTbl[new_prpTbl.cur_point].str_inp = inp

		new_prpTbl.print()
		new_prpTbl.cur_point += 1
		inp = input()
	quit()
		
def deb_std():
	##myPropTbl = prop_table([prop("bull shit", 0, True),prop("Bitches and assholes", 0, True), prop("mother fucker", 0, False), prop("Assumption: You are an ass", 1, True), prop("Assumption: You are a bitch", 1, True), prop("Conclusion: You are a faggot", 1, False),prop("Conclusion: You are a faggot", 0, False)])
	##myPropTbl.print()
    get_stdinput()
def deb_curses(stdscr):
	stdscr.nodelay(False)
	GO = True 
	inp = " "
	indx = 0
	while GO:
		
		print(str(inp))
		
		stdscr.addstr(indx, 0, "║ " + inp)
		
		
		inp = ""
		
		indx += 1
		ENTER = False
  
		while not ENTER:
			new_chr = stdscr.getch()
			if new_chr != 10:
				inp += chr(new_chr)
			else:
				ENTER = True
		if inp == "stop":
			GO = False
		if inp == "clear":
			stdscr.clear()

	exit()


def main(stdscr):
	print("Done")
	quit()



 
if __name__ == "__main__":
	deb = input("Debug (y/n)?")
	if deb.lower() == 'y':
		deb_type = input("Debug type? (1: Curses, 2: Normal Stdin)")
		if deb_type == "1":

			curses.wrapper(deb_curses)	
		elif deb_type == "2":
			deb_std()
      
	else:
		curses.wrapper(main)
