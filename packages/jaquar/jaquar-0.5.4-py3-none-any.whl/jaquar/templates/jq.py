from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import click
from models.model import Base, engine

from config.urls import urls
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'), autoescape=True)

class Jaguar:
    def __init__(self, urls):
        self.urls = urls
        
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        response = Response('Not Found', status=404)
        for path, view_func in self.urls.items():
            if request.path == path:
                context = view_func()
                template_name = context.pop('_template')
                template = env.get_template(template_name)
                html = template.render(**context)
                response = Response(html, status=200, content_type='text/html')
        return response


app = Jaguar(urls)

# Define the available commands using the `click` library.
@click.group()
def cli():
    pass

@cli.command()
@click.option('--drop', is_flag=True, help='Drop all tables')
def initdb(drop):
    """
    Initialize the database.
    """
    if drop:
        Base.metadata.drop_all(bind=engine)
        click.echo('All tables dropped.')
    Base.metadata.create_all(bind=engine)
    click.echo('All tables created.')

@cli.command()
def migrate():
    """
    Run database migrations.
    """
    with click.progressbar(range(100), label='Migrating database') as progress_bar:
        for i in progress_bar:
            # Your migration code here
            curr_progress = i + 1
            progress_bar.label = 'Migrating database: %d%%' % curr_progress
    click.echo('Migrations run successfully.')
    # Retrieve a list of all tables that were migrated
    migrated_tables = Base.metadata.tables.keys()
    # Print the list of migrated tables
    click.echo('The following tables were migrated:')
    for table in migrated_tables:
        click.echo(table)
@cli.command()
def runserver():
    """
    Start the application server.
    """
    run_simple('localhost', 8080, app)
@cli.command()
def lstables():
    """
    List all tables in the database.
    """
    # Add migration code here
    click.echo(print(Base.metadata.tables.keys()))
# Define the CLI entry point.
if __name__ == '__main__':
    cli()
