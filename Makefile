VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt


install:
	make $(VENV)/bin/activate
