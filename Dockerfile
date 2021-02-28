FROM python:3.6-alpine
RUN python -m pip install --upgrade pip
RUN pip install flake8 pytest
COPY easierlog/ easierlog/
COPY tests/ tests/
CMD sh -c "flake8 easierlog tests --count --exit-zero && python -m pytest tests"
