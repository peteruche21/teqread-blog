FROM python:3.8.5-slim

ENV APP_HOME /app 
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR ${APP_HOME}

COPY . ./

RUN python3 -m venv $VIRTUAL_ENV

RUN pip install pip --upgrade
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["./scripts/entrypoint.sh"]