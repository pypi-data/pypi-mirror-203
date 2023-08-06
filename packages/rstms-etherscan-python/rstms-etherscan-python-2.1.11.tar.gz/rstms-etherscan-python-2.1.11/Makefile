# pyproject makefile

default: help

dev:
	pip install -e .[dev]

install:
	pip install -e .

uninstall:
	pip uninstall -y rstms-etherscan-python
	

include $(wildcard make/*.mk)
