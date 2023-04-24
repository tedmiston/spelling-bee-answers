LINE_LENGTH := 88
SRC_DIR := .
PROJECT := spelling_bee_answers

.PHONY: run
run:
	@python -m $(PROJECT).scrapers.nyt

.PHONY: gen-days
gen-days:
	@python -m $(PROJECT).days

.PHONY: gen-stats
gen-stats:
	@python -m $(PROJECT).stats

.PHONY: format
format:
	@./scripts/format.sh $(SRC_DIR) $(LINE_LENGTH) 0

.PHONY: format-dry-run
format-dry-run:
	@./scripts/format.sh $(SRC_DIR) $(LINE_LENGTH) 1

# see `setup.cfg` for flake8 config
.PHONY: lint
lint:
	@flake8 $(SRC_DIR)
	@shellcheck scripts/*

.PHONY: test
test:
	@pytest --cov=$(PROJECT) $(SRC_DIR) && \
	coverage-badge -o assets/coverage.svg

.PHONY: clean
clean:
	@rm -rf \
		**/.pytest_cache \
		**/__pycache__ \
		.mypy_cache
