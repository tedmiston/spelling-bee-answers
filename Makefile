LINE_LENGTH := 88

.PHONY: run
run:
	python -m spelling_bee_answers.scrapers.nyt

.PHONY: gen-days
gen-days:
	python -m spelling_bee_answers.days

.PHONY: gen-stats
gen-stats:
	python -m spelling_bee_answers.stats

.PHONY: format
format:
	black --line-length=$(LINE_LENGTH) .

.PHONY: format-dry-run
format-dry-run:
	black --diff --line-length=$(LINE_LENGTH) .

# see `setup.cfg` for flake8 config
.PHONY: lint
lint:
	flake8 .

.PHONY: test
test:
	pytest .
