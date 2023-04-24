LINE_LENGTH := 88
SRC_DIR := .

.PHONY: run
run:
	@python -m spelling_bee_answers.scrapers.nyt

.PHONY: gen-days
gen-days:
	@python -m spelling_bee_answers.days

.PHONY: gen-stats
gen-stats:
	@python -m spelling_bee_answers.stats

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
	@pytest --cov=spelling_bee_answers $(SRC_DIR) && \
	coverage-badge -o assets/coverage.svg

.PHONY: clean
clean:
	@rm -rf \
		**/.pytest_cache \
		**/__pycache__ \
		.mypy_cache
