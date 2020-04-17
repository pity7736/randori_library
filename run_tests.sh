#!/usr/bin/env bash
pytest -s -vvv --cov=library --cov-report term-missing tests
