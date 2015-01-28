#!/usr/bin/env python2

import os
from urlparse import urlparse

import click


CONNECTION_COMMANDS = {
    'postgres': 'PGPASSWORD={password} psql -U {username} -h {host} -d {database}',
    'mysql': 'MYSQL_PWD={password} mysql -u {username} -h {host} -D {database}',
    'sqlite': 'sqlite3 {database}'
}

def parse_db_url(database_url):
    """Parses the database_url and returns the command to connect to it."""

    # In-memory sqlite is a special case when it has this format
    if database_url == 'sqlite://:memory:':
        return 'sqlite3'

    parsed_url = urlparse(database_url)
    scheme = parsed_url.scheme

    command_format = CONNECTION_COMMANDS.get(scheme, None)
    if not command_format:
        raise ValueError('Scheme "{}" not recognized.'.format(scheme))

    if scheme in ['postgres', 'mysql']:
        scheme_valid = all((
            parsed_url.username,
            parsed_url.password,
            parsed_url.hostname,
            parsed_url.path
        ))
    else:
        scheme_valid = bool(command_format)

    if scheme_valid:
        return command_format.format(username=parsed_url.username,
                                     password=parsed_url.password,
                                     host=parsed_url.hostname,
                                     database=parsed_url.path[1:])
    else:
        raise ValueError('DATABASE_URL is invalid.')


@click.command()
@click.argument('database_url', envvar='DATABASE_URL')
@click.option('-args', 'db_args', help='Extra connection arguments', envvar='DB_ARGS')
@click.option('-command', 'db_command', help='Command to run on the database.')
def connect_to_database(database_url, db_args, db_command):
    """Connect to the DATABASE_URL argument, or environment variable."""
    try:
        connection_command = parse_db_url(database_url)
    except ValueError as e:
        print('Error: {}'.format(e))
        exit(1)

    if db_args:
        connection_command += ' {} '.format(db_args)

    if db_command:
        connection_command += " -c '{}'".format(db_command)

    os.system(connection_command)


if __name__ == '__main__':
    connect_to_database()
