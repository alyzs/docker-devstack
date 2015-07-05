# docker-devstack
Development Stack

A server stack containing nginx/uwsgi/sshd.

Default version (latest):

    The default version runs under s6.


Alterate Version (supervisor):

    An alternate version installs and runs under supervisor.

    The sample scripts in /supervisor implements a hello app.

    To run the sample hellp app:

        docker run -p 80:80 alyz/devstack

    Then open http://localhost on any browser.
