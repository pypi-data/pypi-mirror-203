
# This is a command file for our CLI. Please keep it clean.
#
# - If it makes sense and only when strictly necessary, you can create utility functions in this file.
# - But please, **do not** interleave utility functions and command definitions.

import click

from os import getcwd
from pathlib import Path
from click import Context
from typing import Any, Dict, Optional

from tinybird.feedback_manager import FeedbackManager
from tinybird.client import DoesNotExistException, TinyB

from tinybird.tb_cli_modules.cli import cli
from tinybird.tb_cli_modules.common import _get_setting_value, coro, validate_kafka_auto_offset_reset, \
    validate_kafka_bootstrap_servers, validate_kafka_key, validate_kafka_schema_registry_url, validate_kafka_secret, \
    echo_safe_humanfriendly_tables_format_smart_table
from tinybird.tb_cli_modules.exceptions import CLIConnectionException


@cli.group()
@click.pass_context
def connection(ctx: Context) -> None:
    """Connection commands.
    """


@connection.group(name="create")
@click.pass_context
def connection_create(ctx: Context) -> None:
    """Connection Create commands.
    """


@connection_create.command(name="kafka", short_help='Add a Kafka connection')
@click.option('--bootstrap-servers', help="Kafka Bootstrap Server in form mykafka.mycloud.com:9092")
@click.option('--key', help="Key")
@click.option('--secret', help="Secret")
@click.option('--connection-name', default=None, help="The name of your Kafka connection. If not provided, it's set as the bootstrap server")
@click.option('--auto-offset-reset', default=None, help="Offset reset, can be 'latest' or 'earliest'. Defaults to 'latest'.")
@click.option('--schema-registry-url', default=None, help="Avro Confluent Schema Registry URL")
@click.option('--sasl-mechanism', default=None, help="Authentication method for connection-based protocols. Defaults to 'PLAIN'")
@click.pass_context
@coro
async def connection_create_kafka(
    ctx: Context,
    bootstrap_servers: str,
    key: str,
    secret: str,
    connection_name: Optional[str],
    auto_offset_reset: Optional[str],
    schema_registry_url: Optional[str],
    sasl_mechanism: Optional[str]
) -> None:
    """
    Add a Kafka connection

    \b
    $ tb connection create kafka --bootstrap-server google.com:80 --key a --secret b --connection-name c
    """

    bootstrap_servers and validate_kafka_bootstrap_servers(bootstrap_servers)
    key and validate_kafka_key(key)
    secret and validate_kafka_secret(secret)
    schema_registry_url and validate_kafka_schema_registry_url(schema_registry_url)
    auto_offset_reset and validate_kafka_auto_offset_reset(auto_offset_reset)

    if not bootstrap_servers:
        bootstrap_servers = click.prompt("Kafka Bootstrap Server")
        validate_kafka_bootstrap_servers(bootstrap_servers)
    if not key:
        key = click.prompt("Key")
        validate_kafka_key(key)
    if not secret:
        secret = click.prompt("Secret", hide_input=True)
        validate_kafka_secret(secret)
    if not connection_name:
        connection_name = click.prompt(f"Connection name (optional, current: {bootstrap_servers})", default=bootstrap_servers)

    obj: Dict[str, Any] = ctx.ensure_object(dict)
    client: TinyB = obj['client']

    result = await client.connection_create_kafka(
        bootstrap_servers,
        key,
        secret,
        connection_name,
        auto_offset_reset,
        schema_registry_url,
        sasl_mechanism)

    id = result['id']
    click.echo(FeedbackManager.success_connection_created(id=id))


@connection_create.command(name="bigquery", short_help='Add a BigQuery connection')
@click.option('--no-validate', is_flag=True, help="Do not validate GCP permissions during connection creation")
@click.pass_context
@coro
async def connection_create_bigquery(
    ctx: Context,
    no_validate: bool
) -> None:
    """
    Add a BigQuery connection

    \b
    $ tb connection create bigquery
    """

    obj: Dict[str, Any] = ctx.ensure_object(dict)
    client: TinyB = obj['client']

    gcp_account_details: Dict[str, Any] = await client.get_gcp_service_account_details()

    connection_created: bool = False

    while True:
        response = click.prompt(FeedbackManager.prompt_bigquery_account(service_account=gcp_account_details['account']),
                                type=click.Choice(['y', 'N'], case_sensitive=False), default='N', show_default=True, show_choices=True)

        if response in ('n', 'N'):
            click.echo(FeedbackManager.info_cancelled_by_user())
            break

        if no_validate or await client.check_gcp_read_permissions():
            connection_created = True
            break
        else:
            click.echo('\n')
            click.echo(FeedbackManager.error_bigquery_improper_permissions())

    if connection_created:
        with open(Path(getcwd(), 'bigquery.connection'), 'w') as f:
            f.write('TYPE bigquery\n')
        click.echo(FeedbackManager.success_connection_created(id='bigquery'))


@connection.command(name="rm")
@click.argument('connection_id')
@click.option('--force', default=False, help="Force connection removal even if there are datasources currently using it")
@click.pass_context
@coro
async def connection_rm(
    ctx: Context,
    connection_id: str,
    force: bool
) -> None:
    """Remove a connection.
    """

    obj: Dict[str, Any] = ctx.ensure_object(dict)
    client: TinyB = obj['client']

    try:
        await client.connector_delete(connection_id)
    except DoesNotExistException:
        raise CLIConnectionException(FeedbackManager.error_connection_does_not_exists(connection_id=connection_id))
    except Exception as e:
        raise CLIConnectionException(FeedbackManager.error_exception(error=e))
    click.echo(FeedbackManager.success_delete_connection(connection_id=connection_id))


@connection.command(name="ls")
@click.option('--connector', help="Filter by connector")
@click.pass_context
@coro
async def connection_ls(
    ctx: Context,
    connector: str
) -> None:
    """List connections.
    """

    from tinybird.connectors import DataConnectorSettings, DataSensitiveSettings

    obj: Dict[str, Any] = ctx.ensure_object(dict)
    client: TinyB = obj['client']

    connections = await client.connections(connector=connector)
    columns = []
    table = []

    click.echo(FeedbackManager.info_connections())

    if not connector:
        sensitive_settings = []
        columns = ['service', 'name', 'id', 'connected_datasources']
    else:
        sensitive_settings = getattr(DataSensitiveSettings, connector)
        columns = ['service', 'name', 'id', 'connected_datasources'] + [setting.replace('tb_', '') for setting in getattr(DataConnectorSettings, connector)]

    for connection in connections:
        row = [_get_setting_value(connection, setting, sensitive_settings) for setting in columns]
        table.append(row)

    column_names = [c.replace('kafka_', '') for c in columns]
    echo_safe_humanfriendly_tables_format_smart_table(table, column_names=column_names)
    click.echo('\n')
