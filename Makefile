PYTHON ?= python
APP_MODULE ?= app.main:app

.PHONY: install run test

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) -m uvicorn $(APP_MODULE) --reload

test:
	$(PYTHON) -m pytest
