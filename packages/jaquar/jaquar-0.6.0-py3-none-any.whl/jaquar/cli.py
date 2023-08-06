import os
import shutil
import jaquar
import click
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'), autoescape=True)

# Define the available commands using the `click` library.
@click.group()
def cli():
    pass

@cli.command()
@click.argument('project_name')
def create(project_name):
    """
    Create a new Jaquar project.
    """
    # Check if project directory already exists
    if os.path.exists(project_name):
        click.echo(f"Error: Directory '{project_name}' already exists")
        return
    
    # Create project directory and subdirectories
    os.makedirs(os.path.join(project_name, 'models'))
    os.makedirs(os.path.join(project_name, 'db'))
    os.makedirs(os.path.join(project_name, 'db', 'migrations'))
    os.makedirs(os.path.join(project_name, 'config'))
    os.makedirs(os.path.join(project_name, 'static'))
    os.makedirs(os.path.join(project_name, 'static', 'css'))
    os.makedirs(os.path.join(project_name, 'static', 'js'))
    os.makedirs(os.path.join(project_name, 'static', 'img'))
    os.makedirs(os.path.join(project_name, 'templates'))
    os.makedirs(os.path.join(project_name, 'views'))
    os.makedirs(os.path.join(project_name, 'tests'))

    # Copy files from template directory to project directory
    # Get the path to the template directory inside the jaquar package
    template_dir = os.path.join(os.path.dirname(jaquar.__file__), 'templates')

    # Create the project directory
    os.makedirs(project_name)

    # Copy files from template directory to project directory
    shutil.copy(os.path.join(template_dir, 'jq.py'), os.path.join(project_name, 'jq.py'))
    shutil.copy(os.path.join(template_dir, 'config', '__init__.py'), os.path.join(project_name, 'config', '__init__.py'))
    shutil.copy(os.path.join(template_dir, 'config', 'urls.py'), os.path.join(project_name, 'config', 'urls.py'))
    shutil.copy(os.path.join(template_dir, 'config', 'settings.py'), os.path.join(project_name, 'config', 'settings.py'))
    shutil.copy(os.path.join(template_dir, 'models', '__init__.py'), os.path.join(project_name, 'models', '__init__.py'))
    shutil.copy(os.path.join(template_dir, 'models', 'model.py'), os.path.join(project_name, 'models', 'model.py'))
    shutil.copy(os.path.join(template_dir, 'db', '__init__.py'), os.path.join(project_name, 'db', '__init__.py'))
    shutil.copy(os.path.join(template_dir, 'db', 'migrations', '__init__.py'), os.path.join(project_name, 'db', 'migrations', '__init__.py'))
    shutil.copy(os.path.join(template_dir, 'db', 'migrations', 'alembic.ini'), os.path.join(project_name, 'db', 'migrations', 'alembic.ini'))
    shutil.copy(os.path.join(template_dir, 'views', '__init__.py'), os.path.join(project_name, 'views', '__init__.py'))
    shutil.copy(os.path.join(template_dir, 'views', 'index.py'), os.path.join(project_name, 'views', 'index.py'))
    shutil.copy(os.path.join(template_dir, 'templates', 'index.html.jq'), os.path.join(project_name, 'templates', 'index.html.jq'))
    shutil.copy(os.path.join(template_dir, 'tests', 'test_index.py'), os.path.join(project_name, 'tests', 'test_index.py'))
    shutil.copy(os.path.join(template_dir, 'tests', 'test_model.py'), os.path.join(project_name, 'tests', 'test_model.py'))
    shutil.copy(os.path.join(template_dir, 'tests', 'test_urls.py'), os.path.join(project_name, 'tests', 'test_urls.py'))
    shutil.copy(os.path.join(template_dir, 'tests', 'test_views.py'), os.path.join(project_name, 'tests', 'test_views.py'))

    click.echo(f"New Jaquar project '{project_name}' created successfully.")

# Define the CLI entry point.
if __name__ == '__main__':
    cli()    



