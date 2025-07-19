import os
import subprocess

def run_shell_script(script_path):
    if not os.path.exists(script_path):
        print(f"Script not found: {script_path}")
        return

    try:
        subprocess.run(['bash', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

if __name__ == "__main__":
    script = os.path.join("scripts", "harden.sh")
    run_shell_script(script)
