# common - initialization, variables, functions

# set make variables from project files
project := $(shell tq -r .project.name pyproject.toml)
module := $(shell tq -r .tool.flit.module.name pyproject.toml)
version := $(shell cat VERSION)
src_dirs = $(module) tests 
python_src := $(foreach dir,$(src_dirs),$(shell find $(dir) -name \*.py) )
other_src := $(call makefiles) pyproject.toml
src := $(python_src) $(other_src)
makefiles = Makefile $(wildcard make/*.mk)
git_commit != git log -1 | awk '{print $$2; exit}'

# sanity checks
$(if $(project),,$(error failed to read project name from pyproject.toml))
$(if $(shell [ -d ../"$(project)" ] || echo X),$(error project dir $(project) not found))
$(if $(shell [ $$(readlink -e ../$(project)) = $$(readlink -e .) ] || echo X),$(error mismatch: $(project) != .))
$(if $(module),,$(error failed to read module name from pyproject.toml))
$(if $(shell [ -d "./$(module)" ] || echo missing),$(error module dir '$(module)' not found))
$(if $(shell ls $(module)/__init__.py),,$(error expected "__init__.py" in module dir '$(module)'))
$(if $(version),,$(error failed to read version from version.py))

names:
	@echo project=$(project)
	@echo module=$(module)
	@echo cli=$(cli)
	@echo version=$(version)
	@echo src_dirs=$(src_dirs)
	@echo python_src=$(python_src)
	@echo git_commit=$(git_commit)
	@echo wheel=$(wheel)

	
## list make targets with descriptions
help:	
	@set -e;\
	echo;\
	echo 'Target        | Description';\
	echo '------------- | --------------------------------------------------------------';\
	for FILE in $(call makefiles); do\
	  awk <$$FILE  -F':' '\
	    BEGIN {help="begin"}\
	    /^##.*/ { help=$$0; }\
	    /^[a-z-]*:/ { if (last==help){ printf("%-14s| %s\n", $$1, substr(help,4));} }\
	    /.*/{ last=$$0 }\
	  ';\
	done;\
	echo

short-help:
	@echo "\nUsage: make TARGET\n";\
	echo $$($(MAKE) --no-print-directory help | tail +4 | awk -F'|' '{print $$1}'|sort)|fold -s -w 60;\
	echo


#
# --- functions ---
#

# break with an error if there are uncommited changes
define gitclean =
	$(if $(and $(if $(ALLOW_DIRTY),,1),$(shell git status --porcelain)),$(error git status: dirty, commit and push first))
endef

# break if not in virtualenv (override with make require_virtualenv=no <TARGET>)
ifndef virtualenv
  virtualenv = $(if $(filter $(require_virtualenv),no),not required,$(shell which python | grep -E virt\|venv))
  $(if $(virtualenv),,$(error virtualenv not detected))
endif
# make clean targets

common-clean:
	rm -f .pyproject.toml.*
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -name '*~' -exec rm -f {} +
