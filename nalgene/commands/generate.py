import os

import click

from nalgene.generate import generate_from_file


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.pass_context
def parse(ctx, filename):
    """
    Parse nlg files into generated intents
    """
    filename = os.path.realpath(filename)
    base_dir = os.path.dirname(filename)
    filename = os.path.basename(filename)

    # test_json = json.load(open('test2.json'))
    # root_context = Node('%').add(parse_dict(test_json))

    generate_from_file(base_dir, filename)  # , root_context)

    # else:
    #     filename = sys.argv[1]
    #     base_dir = os.path.dirname(os.path.realpath(__file__))
    #     combined = os.path.join(base_dir, filename)
    #     base_dir = os.path.dirname(combined)
    #     filename = os.path.basename(combined)

    #     def generate(): return generate_from_file(base_dir, filename, Node('%'))
