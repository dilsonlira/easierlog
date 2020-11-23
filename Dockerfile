FROM python:3.6-alpine
RUN python -m pip install --upgrade pip
RUN pip install flake8 pytest
COPY easylog/ easylog/
COPY tests/ tests/
CMD sh -c "flake8 easylog tests --count --exit-zero && pytest tests"
