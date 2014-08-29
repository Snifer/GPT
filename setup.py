# Verificador de dependencias

import subprocess

def main():
    import subprocess
    import os
    try:
        subprocess.call(["nmap", "--version"])
    except OSError as error:
        if error.errno = os.errno.ENOENT:
        print 'Nmap no se tiene instalado... O se encuentra en otro directorio. Porfavor instalar, o especificar el directorio en ~/gpt.conf'
        os.exit()


if __name__ == "__main__":
    main()
