test:
	python3 -m unittest discover tests/

publish:
	python3 setup.py sdist bdist_wheel --universal
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

format:
	black .

coverage:
	coverage run -m unittest discover 
	coverage report -m
	coverage html