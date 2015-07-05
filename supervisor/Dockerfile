#
# Dockerfile for alyz/devstack
#

# Pull base image.
FROM alyz/devenv

# Install uwsgi nginx sshd supervisord
RUN apt-get install -y uwsgi  \
    && apt-get install -y uwsgi-plugin-python uwsgi-plugin-python3 \
    && apt-get install -y nginx \
    && apt-get install -y openssh-server \
    && apt-get install -y supervisor

RUN mkdir -p /var/run/sshd

COPY supervisor /supervisor

expose 80
expose 22

# Define default command.
ENTRYPOINT []
CMD ["supervisord", "-n", "-c", "/supervisor/supervisord.conf"]
