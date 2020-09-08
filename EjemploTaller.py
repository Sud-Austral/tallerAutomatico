import datetime
import time
import git


def GuardarHora():
    f = open('tallerAutomatico/holamundo.txt','wb')
    hora = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S \n")
    f.write(hora.encode())
    f.close()
    
    
def GuardarRepositorio():
    repoLocal = git.Repo(r'C:\Users\limc_\Laboratorio\Taller\tallerAutomatico')
    repoLocal.git.add(".")
    repoLocal.git.commit(m='Commit del taller')
    origin = repoLocal.remote(name='origin')
    origin.push()
    
def Global():
    while True:
        print("Comenzo...")
        try:
            GuardarHora()
            print("Guardo la hora correctamente")
        except:
            print("Fallo en guardar hora")
        try:
            GuardarRepositorio()
            print("Guardo correctamente")
        except:
            print("Fallo en guardar")
        time.sleep(5)