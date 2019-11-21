"""
Program to read .elf file.
Author: Ximu Zhang
Date: 11/17/2019
"""

# import libraries
from __future__ import print_function
from elf_reader import *
from a2l_generator import *


def process_file(filename):
	"""
	:param filename: the path of the .elf file
	:return: None
	"""
	elf_file, elf_header_info = get_elf_header(filename)
	elf_section_info = get_section_info(elf_file)  # retrieve the section information
	global_symbol_set = get_global_symbols(elf_file)  # retrieve section info
	a2l_variable_section_write(global_symbol_set)


if __name__ == '__main__':
	file_path = '.\\input\\sample.elf'
	process_file(file_path)
