import platform, subprocess

subprocess.Popen(["bash","sudo route add -net 192.168.1.0 netmask 255.255.255.0 gw 10.0.0.100"])

def ping(host_or_ip, packets=1, timeout=500):
    if platform.system().lower() == 'windows':
        command = ['ping', '-n', str(packets), '-w', str(timeout), host_or_ip]
        result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=0x08000000)
        return result.returncode == 0 and b'TTL=' in result.stdout
    else:
        command = ['ping', '-c', str(packets), '-w', str(timeout), host_or_ip]
        result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0


# while True:

#     if ping('192.168.1.1'):
#         pass
#     else:
#         command = ['route','add', '-net','192.168.1.0','netmask','255.255.255.0','gw','10.0.0.100']
#         result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=0x08000000)

if ping('192.168.1.1'):
    pass
else:
    command = ['route','add', '-net','192.168.1.0','netmask','255.255.255.0','gw','10.0.0.100']
    result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=0x08000000)
