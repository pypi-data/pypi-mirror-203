# -*-coding:utf-8-*-
import click
from core.generate_app import GenerateApp


@click.group()
def cli():
    pass


@cli.command()
def clear():
    return click.clear()


@cli.command()
@click.option('--app_name', '-a', required=True, help='app name')
def cli(app_name: str):
    click.echo('hello_world')
    GenerateApp(app_name)



