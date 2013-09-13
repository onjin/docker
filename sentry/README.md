redis dockerfile
================
Build:

    docker build -t="onjin/sentry" .

Run:

    # install sentry
    docker run -t -i -e SENTRY_DBHOST=192.168.1.1 -e SENTRY_DBNAME=sentry -e SENTRY_DBUSER=sentry -e SENTRY_DBPASS=sentry onjin/sentry

    # run
    docker run -e SENTRY_DBHOST=192.168.1.1 -e SENTRY_DBNAME=sentry -e SENTRY_DBUSER=sentry -e SENTRY_DBPASS=sentry -p :7365 onjin/sentry start

Env variables:
 * SENTRY_DBHOST default '127.0.0.1'
 * SENTRY_DBUSER default 'sentry'
 * SENTRY_DBNAME default 'sentry'
 * SENTRY_DBPASS default ''
 * SENTRY_WORKERS default 3
