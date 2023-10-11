FROM python:3.11-slim as builder

# Install dependencies
WORKDIR /bot
COPY . .
RUN rm -rf /bot/src/.env && rm -rf /bot/.env

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

FROM python:3.11-slim as runner

WORKDIR /bot
COPY --from=builder /bot /bot

RUN ls /usr/local/lib/
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /bot/src
CMD ["python", "bot.py"]
