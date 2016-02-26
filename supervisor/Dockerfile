#
# Dockerfile for alyz/devstack
#

# Pull base image.
FROM alyz/devstack:latest

# Install supervisor
RUN apt-get install -y supervisor
COPY supervisor /supervisor

# set entrypoint to a passthru command
ENTRYPOINT [ "/usr/local/bin/spawnvp" ]

# Define default command.
CMD ["supervisord", "-n", "-c", "/supervisor/supervisord.conf"]
