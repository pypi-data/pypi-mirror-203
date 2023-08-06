import subprocess

def test_tulp():
    command = "python tulp.py '2+2'"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert result.returncode == 0
    assert result.stdout.decode().strip() == '4'

