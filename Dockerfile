FROM python:3.8.18-slim as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests --auto-remove \
    libgtk-3-0 libdbus-glib-1-2 libx11-xcb1 libxt6 bzip2 curl gcc g++ bzip2 libjpeg-dev zlib1g-dev
RUN curl -L -o /tmp/firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64" && \
    test -f /tmp/firefox.tar.bz2 && \
    tar -xjf /tmp/firefox.tar.bz2 -C /opt && \
    ln -s /opt/firefox/firefox /usr/bin/

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid 10001 \
    appuser
RUN mkdir -p /home/appuser/InstaPy && chown -R appuser:appuser /home/appuser

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY . .
EXPOSE 8000
CMD ["python", "_runn.py"]
