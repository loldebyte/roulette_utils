.PHONY: test

test:
	pytest --cov=. --html=tests/reports/report.html --cov-report html:tests/cov -W error tests/ -vv
