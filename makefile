default:
	pip3 install poetry
	poetry config virtualenvs.in-project true
	make install
	make build
	make package-install

install:
	poetry install

build:
	rm -rf ./dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
