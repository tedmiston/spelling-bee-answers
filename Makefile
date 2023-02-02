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
	black --line-length=120 .

.PHONY: format-dry-run
format-dry-run:
	black --diff --line-length=120 .

.PHONY: test
test:
	pytest .

.PHONY: run-mypy
run-mypy:
	# mypy -m spelling_bee_answers.scrapers.nyt -m spelling_bee_answers.days -m spelling_bee_answers.stats
	# todo: debug why exclude flag doesn't seem to be working - https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-exclude
	# mypy --strict --exclude='/spelling_bee_answers/tests/*\.py' spelling_bee_answers/*/**.py
	# mypy --strict --exclude='/spelling_bee_answers/tests/*' spelling_bee_answers/*/**.py
	# mypy --strict --exclude='/spelling_bee_answers/tests/' spelling_bee_answers/*/**.py
	# mypy --strict --exclude='/spelling_bee_answers/tests*' spelling_bee_answers/*/**.py
	# mypy --strict --exclude='/spelling_bee_answers/tests*' spelling_bee_answers/*/**.py
	# mypy --strict spelling_bee_answers/*.py spelling_bee_answers/scrapers/*.py
	# mypy --strict --exclude='/tests/' spelling_bee_answers/
	# mypy --strict --allow-untyped-calls --exclude='/tests/' spelling_bee_answers/
	mypy --strict --allow-untyped-calls --disallow-any-explicit --exclude='/tests/' spelling_bee_answers/
