def cmdissue(toissue, activesession):
     ssh_stdin, ssh_stdout, ssh_stderr = activesession.exec_command(toissue)
     return ssh_stdout.read().decode('UTF-8')

def userinput():
    our_commands = input("Please input commands
