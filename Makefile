export SHELL:=/bin/bash
.ONESHELL:


init: clean
	virtualenv .venv
	$(source .venv/bin/activate)
	pip install -r requirements/requirements.txt

clean:
	rm -rf .venv

init-poetry: clean
	pip install poetry
	poetry install 