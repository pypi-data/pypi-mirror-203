import os
import shutil
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
    shutil.copy('templates/jq.py', os.path.join(project_name, 'jq.py'))
    shutil.copy('templates/__init__.py', os.path.join(project_name, '__init__.py'))
    shutil.copy('templates/config/__init__.py', os.path.join(project_name, 'config', '__init__.py'))
    shutil.copy('templates/config/urls.py', os.path.join(project_name, 'config', 'urls.py'))
    shutil.copy('templates/config/settings.py', os.path.join(project_name, 'config', 'settings.py'))
    shutil.copy('templates/models/__init__.py', os.path.join(project_name, 'models', '__init__.py'))
    shutil.copy('templates/models/model.py', os.path.join(project_name, 'models', 'model.py'))
    shutil.copy('templates/db/__init__.py', os.path.join(project_name, 'db', '__init__.py'))
    shutil.copy('templates/db/migrations/__init__.py', os.path.join(project_name, 'db', 'migrations', '__init__.py'))
    shutil.copy('templates/db/migrations/alembic.ini', os.path.join(project_name, 'db', 'migrations', 'alembic.ini'))
    shutil.copy('templates/views/__init__.py', os.path.join(project_name, 'views', '__init__.py'))
    shutil.copy('templates/views/index.py', os.path.join(project_name, 'views', 'index.py'))
    shutil.copy('templates/templates/index.html.jq', os.path.join(project_name, 'templates', 'index.html.jq'))
    # shutil.copy('templates/tests/__init__.py', os.path.join(project_name, 'tests', '__init__.py'))
    shutil.copy('templates/tests/test_index.py', os.path.join(project_name, 'tests', 'test_index.py'))
    shutil.copy('templates/static/css/style.css', os.path.join(project_name, 'static', 'css', 'style.css'))
    shutil.copy('templates/static/js/script.js', os.path.join(project_name, 'static', 'js', 'script.js'))
    # shutil.copy('templates/static/img/logo.png', os.path.join(project_name, 'static', 'img', 'logo.png'))

    

    
    # Render README and manage.py templates and write to file
    template = env.get_template('README.md')
    with open(os.path.join(project_name, 'README.md'), 'w') as f:
        f.write(template.render(project_name=project_name))
    
    template = env.get_template('manage.py')
    with open(os.path.join(project_name, 'manage.py'), 'w') as f:
        f.write(template.render(project_name=project_name))
    
    click.echo(f"New Jaquar project '{project_name}' created successfully.")

# Define the CLI entry point.
if __name__ == '__main__':
    cli()
