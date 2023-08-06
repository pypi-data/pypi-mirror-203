# pyproject makefile

default: help

dev:
	pip install -e .[dev]

install:
	pip install -e .

uninstall:
	pip uninstall -y rstms-etherscan-python
	
.PHONY: test
unitest:
	bash ./run_tests.sh $(API_KEY)

clean:
	$(MAKE) $(addsuffix -clean,$(notdir $(basename $(wildcard make/*.mk))))

include $(wildcard make/*.mk)
