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
	black --line-length=88 .

.PHONY: test
test:
	pytest .
