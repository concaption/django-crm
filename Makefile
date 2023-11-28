setup:
	chmod +x ./setup.sh &&\
		./setup.sh
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:
	python -m pytest -vv --cov=main test_*.py &&\
		python -m pytest --nbval notebook.ipynb
format:
	black ./**/*.py
	black *.py
lint:
	pylint --disable=R,C *.py
	black --check ./**/*.py
refactor: format lint
deploy:
	# deploy goes here
run:
	python manage.py makemigrations\
		&& python manage.py migrate\
		&& python manage.py runserver
all: install lint test format deploy
