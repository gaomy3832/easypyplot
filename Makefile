
install:
	pip install --user

uninstall:
	pip uninstall easypyplot

editable_install:
	pip install --user -e .

lint:
	pylint -r n easypyplot

clean:
	rm -rf build dist *.egg-info
	rm -f easypyplot/*.pyc

.PHONY: install uninstall editable_install lint clean
