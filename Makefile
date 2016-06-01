default: test

init:
	@pip3 install -r requirements.txt

syntax:
	@pep8 .

test:
	@python3 -m unittest discover tests/
