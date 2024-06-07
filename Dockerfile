FROM python:3.9.13-slim-bullseye

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN set -eux; mkdir -p /app/files

# Install build dependencies
RUN apt-get update; \
    apt-get install -y bash curl gcc libffi-dev libpq-dev openssl jq ca-certificates tzdata wget; \
    apt-get clean \
    apt-get update; \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"

# Setup timezone
ENV TZ=America/Argentina/Cordoba
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Installing Speedtest ookla CLI
RUN wget -nv -O /tmp/speedtest.tgz "https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-x86_64.tgz"; \
    tar zxvf /tmp/speedtest.tgz -C /tmp; \
    cp /tmp/speedtest /usr/local/bin; \
    chown -R speedtest:speedtest /app; \
    rm -rf /tmp/*

# Work arround for rust build not suported on arm
# https://github.com/pyca/cryptography/issues/6347

# Install script dependencies
RUN pip install --upgrade pip
RUN pip install --user poetry
ENV PATH="/root/.local/bin:${PATH}"

# COPY poetry.lock /app/
COPY pyproject.toml /app/

RUN poetry install --sync

# Copy core project
COPY src /app/src
