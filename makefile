init:
	pyenv versions --bare | grep -q "^3.12.6$$" || pyenv install 3.12.6
	pyenv virtualenvs --bare | grep -q "^store$$" || pyenv virtualenv 3.12.6 store
	PYENV_VERSION=store python -m pip install -r req_3-12-6.txt
	PYENV_VERSION=store python manage.py makemigrations
	PYENV_VERSION=store python manage.py migrate

run:
	PYENV_VERSION=store python manage.py runserver

clean:
	rm -rf venv instance
	find . -type d -name "__pycache__" -exec rm -rf {} +

css:
	tailwind -i static/styles.css -o static/output.css -w
