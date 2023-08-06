# -*-coding:utf-8-*-
import click

from core.generate_app import GenerateAppManger


@click.group()
def cli():
    pass


@cli.command()
def clear():
    return click.clear()


@cli.command()
@click.option('--app_name', '-a', required=True, help='app name')
def cli(app_name: str):
    generate_app_manager = GenerateAppManger(app_name)
    generate_app_manager.run()




