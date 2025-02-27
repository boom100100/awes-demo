import click

from app.commands.groups import user_cli
from app.services import User



# call this CLI command as `flask user create <name> <name2>`:
# flask user create awes awes2
@user_cli.command('create') # the string value here represents the command_name
# choose whatever name you want for these arguments. 
# They map ordered to the function parameter names.
# Two args need two parameters, etc.
@click.argument('name') # arg1
@click.argument('name2') # arg2
# function name structure: verb_object
# and use the same name for argument mapping so it's not confusing
def create_user(name, name2): 
    print(name + name2)
    user = User()
    user.create()
