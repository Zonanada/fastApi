FROM python:3.10-slim

USER root

WORKDIR /app

COPY ./main_tests.py /app/main_test.py
COPY ./test_dishes.py /app/test_dishes.py
COPY ./test_menu.py /app/test_menu.py
COPY ./test_submenu.py /app/test_submenu.py


RUN apt -y update && apt -y upgrade
RUN pip install --upgrade pip
RUN pip install pytest requests


CMD pytest -s -v main_test.py