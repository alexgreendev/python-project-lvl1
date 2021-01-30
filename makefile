default:
	pip3 install poetry
	poetry config virtualenvs.in-project true
	make install
	make build
	make package-install

activate-env:
	pyenv activate brain-games-package-3.8.2

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
