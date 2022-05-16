import time
import git

repo = git.Repo('~/')
repo.remotes.upstream.pull('master')

ARCH = "writeTest.txt"

n=0

while True:
    n=n+1
    with open(ARCH, 'a') as df:
        df.write(str(n))
        df.close()
    print("Prueba"+str(n))
    time.sleep(60)
