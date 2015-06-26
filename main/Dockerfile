#
# Dockerfile for alyz/devstack
#

# Pull base image.
FROM alyz/devbase

# Install utilities
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y sudo rsync

# Install uwsgi nginx sshd
RUN apt-get install -y uwsgi  \
    && apt-get install -y python python3 \
    && apt-get install -y uwsgi-plugin-python uwsgi-plugin-python3 \
    && apt-get install -y python-paste python3-paste

RUN apt-get install -y nginx \
    && apt-get install -y openssh-server \
    && apt-get install -y supervisor

# Install python libraries and tools
RUN apt-get install -y python-webob python3-webob \
    && apt-get install -y python-gd python-imaging python-magic python-six python3-magic python3-six \
    && apt-get install -y python-crypto python3-crypto \
    && apt-get install -y poppler-utils

RUN mkdir -p /var/run/sshd
