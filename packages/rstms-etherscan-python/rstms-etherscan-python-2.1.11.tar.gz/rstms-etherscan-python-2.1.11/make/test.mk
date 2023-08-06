# python test makefile
 
test_cases := $(if $(test),-k $(test),)

### regression test
test: fmt
	pytest $(test_cases)

### pytest with break to debugger
debug: fmt
	pytest -sv --pdb $(test_cases)

### check code coverage quickly with the default Python
coverage:
	coverage run --source $(module) -m pytest
	coverage report -m


.tox: $(filter-out $(module)/version.py,$(python_src))
	$(if $(DISABLE_TOX),@echo '<tox disabled>',tox)

### run tests wit tox
tox: .tox

tox-clean:
	rm -rf .tox

test-clean: tox-clean
	rm -f .coverage

test-sterile: test-clean
	find logs -type f -not -name README.md -exec rm -f '{}' +
