# python dist makefile

wheel = dist/$(module)-$(version)-py2.py3-none-any.whl

$(wheel): $(src) pyproject.toml
	flit build

wheel: $(wheel) $(if $(DISABLE_TOX),,tox)

dist: wheel

dist-clean:
	find dist -not -name README.md -not -name dist -exec rm -f '{}' +
	rm -rf build *.egg-info .eggs wheels
