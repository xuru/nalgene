import click as click

from nalgene.commands.generate import parse


@click.group()
@click.option('--verbose', '-v', count=True, help="The verbosity of the output")
@click.pass_context
def cli(ctx, verbose):
    ctx.obj = {'verbose': verbose}


cli.add_command(parse)
