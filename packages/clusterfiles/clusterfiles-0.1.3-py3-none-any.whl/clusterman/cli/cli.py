import click
from clusterman.main.mainline import send_message
import flask


@click.group
def clusterman():
    pass


@clusterman.command
@click.argument("src")
@click.argument("dest")
@click.argument("metadata", default="")
@click.option("--recrawl", type=int, default=3600)
def add_map(src, dest, recrawl, metadata):
    try:
        parsed_metadata = {
            name: value
            for name, value in (
                x.split("=", maxsplit=1)
                for x in metadata.split("&")
            )
        }
        if send_message(
            'cli.add_local_map',
            'add_local_map',
            {
                'source_root': src,
                'target_root': dest,
                'metadata': parsed_metadata,
                'recrawl_interval': recrawl
            }
        ):
            print("Local map added")
    except ValueError as ex:
        print(str(ex))


@clusterman.command
def sync_all():
    try:
        if send_message('cli.sync_all', 'sync_all'):
            print("Synchronizations for all datasets queued")
    except ValueError as ex:
        print(str(ex))


@clusterman.command
def pull_config():
    try:
        if send_message('cli.sync_all', 'reload'):
            print("Configuration pull complete")
    except ValueError as ex:
        print(str(ex))


@clusterman.command
def vacuum():
    try:
        if send_message('cli.vacuum', 'vacuum'):
            print("Vacuum complete")
    except ValueError as ex:
        print(str(ex))


@clusterman.command
def cron_sync():
    try:
        if send_message('cli.sync_all', 'check_sync'):
            print("Scheduled syncs queued")
    except ValueError as ex:
        print(str(ex))


@clusterman.command
@click.argument("source_file")
@click.option("--force", type=bool, default=False, is_flag=True)
def sync_file(source_file, force):
    try:
        if send_message('cli.sync_all', 'sync', {"source": source_file, "force": force}):
            print(f"{source_file} queued for sync")
    except ValueError as ex:
        print(str(ex))


@clusterman.command
def create_db():
    try:
        if send_message('cli.create_db', 'create_db'):
            print("Databases created")
    except ValueError as ex:
        print(str(ex))
