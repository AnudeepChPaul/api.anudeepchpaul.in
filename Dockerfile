# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

ADD . /app
# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "manage"]
#CMD ["sh", "-c", "flask run --no-debugger --no-reload --host 0.0.0.0 --port 5000"]
