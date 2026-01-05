FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

WORKDIR /usr/workspace

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps chromium firefox webkit

COPY . .

ENV BROWSER=chromium
ENV MARKER=smoke
ENV THREADS=1

ENV BROWSER=chromium
ENV MARKER=smoke
ENV THREADS=1

ENV PYTHONPATH=/usr/workspace
ENV PYTHONPATH="${PYTHONPATH}:/usr/workspace/stellarburgerPW"

CMD ["/bin/sh", "-c", "pytest stellarburgerPW/ -v -n ${THREADS} -m ${MARKER} --alluredir=allure-results"]

