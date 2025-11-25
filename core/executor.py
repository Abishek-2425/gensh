import subprocess

def execute_command(cmd: str):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[red]Command failed:[/red] {e}")
