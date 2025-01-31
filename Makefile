# Project makefile

# working directories and files
#
TOPDIR		:=$(shell pwd)
SRC			:=$(TOPDIR)/pdf2docxnogui
BUILD		:=$(TOPDIR)/build
DOCSRC		:=$(TOPDIR)/doc
TEST		:=$(TOPDIR)/test
CLEANDIRS	:=.pytest_cache pdf2docxnogui.egg-info dist

# pip install sphinx_rtd_theme

.PHONY: src doc test clean

src:
	@python setup.py sdist --formats=gztar,zip && \
	python setup.py bdist_wheel

doc:
	@if [ -f "$(DOCSRC)/Makefile" ] ; then \
	    ( cd "$(DOCSRC)" && make html MODULEDIR="$(SRC)" BUILDDIR="$(BUILD)" ) || exit 1 ; \
	fi

test:
	@pytest -v "$(TEST)/test.py" --cov="$(SRC)" --cov-report=xml

clean:
	@if [ -e "$(DOCSRC)/Makefile" ] ; then \
	    ( cd "$(DOCSRC)" && make $@ BUILDDIR="$(BUILD)" ) || exit 1 ; \
	fi
	@for p in $(CLEANDIRS) ; do \
	    if [ -d "$(TOPDIR)/$$p" ];  then rm -rf "$(TOPDIR)/$$p" ; fi ; \
	done
	@if [ -d "$(BUILD)" ];  then rm -rf "$(BUILD)" ; fi
	@if [ -d "$(DOCTARGET)" ];  then rm -rf "$(DOCTARGET)" ; fi