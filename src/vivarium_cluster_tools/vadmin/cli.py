import click

from vivarium_cluster_tools.vadmin import utilities, log_parser, repositories


@click.group()
def vadmin():
    """Utility for performing ``vivarium`` administrative tasks."""
    pass


@vadmin.command()
@click.argument('logs-directory', type=click.Path(exists=True, file_okay=False))
@click.option('--result-directory', '-o', type=click.Path(exists=True, file_okay=False),
              help='The directory into which to write the summary of the parsed logs. '
                   'Defaults to given logs directory if not given.')
@click.option('-v', 'verbose', count=True, help='Configure logging verbosity.')
def parse(logs_directory, result_directory, verbose):
    """Parse and summarize the worker_logs from a ``psimulate`` command.

    Given a worker logs directory from a previous run, a summary hdf will be
    created in the ``result_directory`` (which defaults to the given logs
    directory unless otherwise specified) with two keys: 'worker_data', which
    includes a summary line for each worker log in the directory and 'sim_data',
    which includes a summary line for each simulation job run by a worker.
    """
    utilities.configure_master_process_logging_to_terminal(verbose)
    if not result_directory:
        result_directory = logs_directory
    log_parser.parse_log_directory(logs_directory, result_directory)


@vadmin.group()
def oauth():
    pass


@oauth.command()
@click.argument('service', type=click.Choice(['stash', 'github']))
def create(service):
    print(f'creating oauth token for {service}')


@oauth.command()
@click.argument('service', type=click.Choice(['stash', 'github']))
def remove(service):
    print(f'creating oauth token for {service}')


@oauth.command()
def display():
    print(f'Displaying OAuth tokens')
