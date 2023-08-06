import subprocess

host = "www.google.com"
host = "192.168.1.13"

ping = subprocess.Popen(
    ["ping", "-n", "1", "-w", "6000", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()


print("Out:")
print(out)

print("Error:")
print(error)