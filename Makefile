.PHONY: run
run:
	python app.py

.PHONY: format
format:
	black .

.PHONY: test
test:
	pytest .
