VENV = ./venv

all: test qa

.PHONY: test
test: $(VENV)/bin/pytest
	$(VENV)/bin/pytest -v

.PHONY: qa
qa: $(VENV)/bin/mypy
	$(VENV)/bin/mypy *.py
