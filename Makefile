
PACKAGE = easypyplot

# Get git remote URL and change to HTTPS
REMOTE = $(shell git config --get remote.origin.url \
		 | sed 's|git@github.com:|https://github.com/|')

install:
	pip install --user git+$(REMOTE)#egg=$(PACKAGE)

uninstall:
	pip uninstall $(PACKAGE)

editable_install:
	pip install --user -e .

lint:
	pylint -r n $(PACKAGE)

clean:
	rm -rf build dist *.egg-info
	rm -f $(PACKAGE)/*.pyc

.PHONY: install uninstall editable_install lint clean
