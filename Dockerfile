FROM python:3.11.5-slim-bullseye

WORKDIR /app

# Installing Speedtest ookla CLI
RUN apt-get update; \
    apt-get install -y wget; \
    wget -nv -O /tmp/speedtest.tgz "https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-x86_64.tgz"; \
    tar zxvf /tmp/speedtest.tgz -C /tmp; \
    cp /tmp/speedtest /usr/local/bin; \
    chown -R speedtest:speedtest /app; \
    rm -rf /tmp/*

# Installing dependencies
RUN pip install --user poetry
ENV PATH="/root/.local/bin:${PATH}"

COPY poetry.lock /app/
COPY pyproject.toml /app/

RUN poetry install

# Copy core project
COPY src /app/src