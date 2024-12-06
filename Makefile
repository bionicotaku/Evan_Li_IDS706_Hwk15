install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py

format:
	black *.py

lint:
	ruff check *.py mylib/*.py test_*.py

run:
	python main.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

push:
	git config --global user.email "action@github.com" &&\
	git config --global user.name "GitHub Action" &&\
	git add . &&\
	git commit -m "Update" &&\
	git push
	
all: install format test lint run

# -t: tag
docker-build:
	docker build -t bionicotaku/ids706_individual .

# -v $(PWD):/app: mount the current directory to the container
docker-run:
	docker run -v $(PWD):/app bionicotaku/ids706_individual