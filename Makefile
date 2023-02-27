clean:
	rm -rf .pytest_cache

test:
	pytest

black:
	black src

lint:
	pylint src