APP_NAME=fast-api-app

clean:
		find . -type f -name "*.py[co]" -delete
		find . -type d -name __pycache__ -delete
		find . -type d -name ".pytest_cache" -delete
		find . -type f -name ".coverage" -delete

install:
		pip install -r requirements.txt

test: install
		pip install pytest pytest-cov
		pytest --cov

lint: install
		pip install flake8
		flake8 .

docker-build:
		docker build --no-cache -t $(APP_NAME):latest .

docker-enter: docker-build
		docker run -it $(APP_NAME) /bin/sh \

run:
		docker-compose up
