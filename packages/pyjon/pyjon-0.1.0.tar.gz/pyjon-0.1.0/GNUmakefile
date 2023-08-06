# Copyright (c) 2023, Justin Béra (@just1not2) <me@just1not2.org>
# Apache License 2.0 (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0.txt


default: build

.PHONY: build
build: env
	env/bin/python3 -m build

env:
	python3 -m venv env
	env/bin/python3 -m pip install --upgrade pip
	env/bin/python3 -m pip install -r dev-requirements.txt

.PHONY: upload
upload:
	env/bin/python3 -m twine upload dist/*
