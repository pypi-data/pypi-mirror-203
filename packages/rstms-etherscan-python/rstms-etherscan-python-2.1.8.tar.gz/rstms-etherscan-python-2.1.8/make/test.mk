# python test makefile
 
test_cases := $(if $(test),-k $(test),)

### regression test
test: fmt
	pytest $(test_cases)

### pytest with break to debugger
debug: fmt
	pytest -v --pdb $(test_cases)

test-clean:
	rm -f .coverage
	rm -rf .tox
