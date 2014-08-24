#!/bin/bash

# Use this script to regenerate the database.
#
# CAUTION: All existing data (including migrations) will be deleted


# TODO: Add user prompt to abort


# Find the install dir
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DB_DIR="$DIR/../proj/"
MIGRATION_DIR="$DB_DIR/crowded/migrations"

# Delete DB file
rm -rf "$DB_DIR/db.sqlite3"
rm -rf "$MIGRATION_DIR"

# Regen the database, prompt to create superuser
python "$DB_DIR/manage.py" syncdb

# Apply the table migrations
python "$DB_DIR/manage.py" schemamigration crowded --initial
python "$DB_DIR/manage.py" migrate crowded --fake
