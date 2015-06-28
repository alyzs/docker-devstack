# docker-devstack
Development Stack

A server stack containing nginx/uwsgi/sshd running inside supervisor.

The sample scripts in /supervisor implements a hello app.

To run the sample hellp app:

    docker run -p 80:80 alyz/devstack

Then open http://localhost on any browser.
