from app.commands.user_group import user_cli

command_groups = [
    user_cli,
]

def add_commands(app):
    for command_group in command_groups:
        app.cli.add_command(command_group)
