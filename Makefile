install:
	python -m pip install -r requirements.txt

run:
	python run.py

test:
	python -m pytest

build:
	python -m compileall app services run.py

check:
	python -m pytest -q
	python -m compileall app services run.py

