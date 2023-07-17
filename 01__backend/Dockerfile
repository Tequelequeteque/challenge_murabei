FROM python:3.8-slim-bullseye

############################################
# Instalar as coisas que forem necessárias #
############################################

# Linux Packages
RUN apt-get update
RUN apt-get install -y postgresql-client
RUN apt-get install -y curl

# Packages install
COPY requirements/requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt

# Coping files
COPY codes /django
WORKDIR /django/

CMD ["bash", "/django/start_server.sh"]
