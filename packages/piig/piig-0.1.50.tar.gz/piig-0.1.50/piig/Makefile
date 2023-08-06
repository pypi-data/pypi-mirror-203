# oo

FILES=nd.py haas.py __init__.py function.py axis.py main.py support.py ity.py gtype.py interp.py g.py iface.py ../examples/vicecenter.py
#DFILES=gcomp/main.py gcomp/support.py gcomp/ity.py gcomp/gtype.py gcomp/interp.py gcomp/nd.py gcomp/g.py gcomp/iface.py  ./tests/t20_vicecenter_test.py
#top:
#	sacpdb.py --cont ./makestdvars.py --regen


SRC=$(PWD)

REMOVE_PARENS=sed -e 's/([^()]*)//g'
REMOVE_G=sed -e 's:G55::g'

diff:
	$(REMOVE_PARENS) tests/golden/vicecenter.new >n
	$(REMOVE_PARENS) tests/golden/vicecenter.nc >o
	sdiff n o

diffs: n/vicecenter.nc
	- diff -U 10 -iwr o n
#	./ea.py	 sdiff -W -i  <($(REMOVE_PARENS) o7/o/O0001-PROBE-VICE-CENTER.NC) <($(REMOVE_PARENS) n/O0001-PROBE-VICE-CENTER.NC)
#	$(REMOVE_PARENS) o7/o/O0001-PROBE-VICE-CENTER.NC | $(REMOVE_G) > a
#	$(REMOVE_PARENS) n/O0001-PROBE-VICE-CENTER.NC | $(REMOVE_G) > b
#	sdiff -W -i  a b


n/vicecenter.nc: $(FILES)
	python ../examples/vicecenter.py
	cp  ../examples/vicecenter.nc n

.PHONY: deps
deps:	$(SRC)/stdg.py

$(SRC)/stdg.py: $(SRC)/makestdvars.py
	$(SRC)/makestdvars.py --regen

.PHONY:c
c:
	cp n/* o

ci:
	git add o/*
	ci

d:
	rm -f ../../_nc_/*

lint:


	pylama -l all

plint:
	(cd ..; pylint p2g)



kill:
	pkill -9 -f main.py
pdb:
	pdb -c c main.py

.PHONY:
t:
	(cd .. ; pytest )

t0:
	pytest ./tests.py::test_var_deref_addresses

tags:
	etags *.py


sacpdb:
	echo "s.py:671:1: warning: (binop_class)         :>>>(opname = |, gcode_name = OR, fn =  <lambda>)"
	sacpdb.sh main.py 

mypy:
#	(cd ..; 	mypy $(DFILES))
	mypy $(FILES)

pytype:
	pytype -k -j auto $(FILES)


t1:
	pytest

t2:
	(cd ..;make cover)

t3:
	pytest -cov ../tests
	coverage lcov



clean:
	rm -rf *.lcov *.log *cover *.nc .coverage .cov2emacs* .pytype z coverage.json
