.PHONY: run
run:
	python -m spelling_bee_answers.app

.PHONY: gen-readme-table
gen-readme-table:
	python -m spelling_bee_answers.gen_readme_table

.PHONY: stats
stats:
	python -m spelling_bee_answers.stats

.PHONY: format
format:
	black .

.PHONY: test
test:
	pytest .
