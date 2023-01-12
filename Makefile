.PHONY: run
run:
	python app.py

.PHONY: gen-readme-table
gen-readme-table:
	python gen_readme_table.py

.PHONY: format
format:
	black .

.PHONY: test
test:
	pytest .
