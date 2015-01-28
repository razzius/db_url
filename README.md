`db_cli` provides the `db` command-line utilty for connecting to databases.

Install via pip:

```
$ pip install db_cli
```

## Use with mysql, postgres, sqlite

```
$ export DATABASE_URL='sqlite://'
$ db
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
```

## Designed for use with PAAS

```
$ export DATABASE_URL=`heroku config:get DATABASE_URL`
$ db
psql (9.4.0, server 9.3.3)
SSL connection (protocol: TLSv1.2, cipher: DHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

d6p6s3877j3em=>
```

If you pass `db` an argument it'll connect to that url.

```
$ db mysql://b19db:38c4f@us-cdbr-iron-east-01.cleardb.net/heroku_9044793
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 23587215
Server version: 5.5.40-log MySQL Community Server (GPL)

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

## Options

If you want to run a command on the database, use the `-command` flag:

```
$ db -command '\dt+'
                         List of relations
Schema |               Name                |   Type   |     Owner
public | django_session                    | table    | eesufvsvxmwbll
public | django_site                       | table    | eesufvsvxmwbll
...
```

Set optional connection arguments via the `-args` flag or the environment variable `DB_ARGS`:

```
$ db -args '-qtA'
d6p6s3877j3em=>
$ export DB_ARGS='-qtA --variable=PROMPT1="> "'
$ db
>
```

Run a commands with args

```
$ db -args '-tA' -command '\dt+'
public|django_session|table|eesufvsvxmwbll|1240 kB|
public|django_site|table|eesufvsvxmwbll|40 kB|
```
