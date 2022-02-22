SHELL := /bin/bash

create_environment:
	python3 -m venv env-address-book-manager

delete_environment:
	rm -rf env-address-book-manager

install:
	pip install --upgrade pip
	pip install -r requirements.txt
