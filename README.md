# docker-devstack
Development Stack

A server stack containing nginx/uwsgi/sshd.

Default version (latest):

    The default version runs under s6.


Example (s6):

    The sample scripts in /services implements a hello app.

    To run the sample hellp app:

        docker run -p 80:80 alyz/devstack:s6

    Then open http://localhost on any browser.

Alterate Example (supervisor):

    An alternate version installs and runs under supervisor.

    The sample scripts in /supervisor implements a hello app.

    To run the sample hellp app:

        docker run -p 80:80 alyz/devstack:supervisor

    Then open http://localhost on any browser.
