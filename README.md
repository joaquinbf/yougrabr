# WishPyStock

# Descargar el proyecto

Este proyecto se puede descargar haciendo clic en el botón `Clone or Download` y luego `Download ZIP`. Previo a trabajar, descomprimir el archivo `.zip` descargado. 



## Notas de instalación con Docker.

Para asegurar la portabilidad de la aplicación y su desarrollo, se puede utilizar Docker. Los siguientes vídeos pueden ser de ayuda para entender que es docker, como instalarlo y usarlo.

- [¿Que es Docker?](https://www.youtube.com/watch?v=hQgvt-s-AHQ)
- [Un entorno movil con Docker](https://www.youtube.com/watch?v=0rOTx8DYH_E)

Para su instalación recomendamos:

- Guías oficiales para Windows
  - [Directamente desde la pagina](https://www.docker.com/products/docker-desktop)

- Guías oficiales para linux
  - [Instalacion usando repositorios](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)
  - [Post instalacion en linux (muy recomendado)](https://docs.docker.com/install/linux/linux-postinstall/)
- Guías no oficiales para Windows y Linux.
  - [¿Como se instala (windows 10)?](https://www.youtube.com/watch?v=BK-C2RofmTE) 
  - [¿Como se instala (ubuntu)?](https://www.youtube.com/watch?v=Q5YtjXoCfPs)
- [¿Como se uso para el desarrollo de la aplicacion?](https://www.youtube.com/watch?v=YENw-bNHZwg&t=1464s)

> Nota: En Windows, instalar Docker junto con su compatibilidad con contenedores linux, ya que la mayoría de la aplicación fue desarrollada en ese entorno. Acorde a esto, debe hacer un switch al modo de compatibilidad con contenedores linux. Esto ultimo se puede hacer desde el sub menú de configuración de Docker en la barra de tareas

En primer lugar, instalar Docker y asegurarse de que se este ejecutando (esto depende de su SO pero se puede probar mediante el comando `docker run hello-world`).

## Notas de desarrollo con VSCODE y Docker

Para continuar el desarrollo de la aplicación es importante tener el editor de código [Visual Studio Code](https://code.visualstudio.com/). Es una herramienta profesional que sera de mucha ayuda para la gestión de archivos y contenedores. Esta disponible para todos los sistemas operativos y su [instalación](https://www.youtube.com/watch?v=zbycB-Yetb0) es muy sencilla.

Junto a VSCode, es necesario tener algunas extensiones que nos van a facilitar en gran medida el proceso de creación y mantenimiento de contenedores. En primer lugar accedemos a la sección de extensiones e instalamos `Docker` de Microsoft y `Remote Development` tambien de Microsoft.

![](https://www.mclibre.org/consultar/informatica/img/vscode/vsc-perso-idioma-1.png)

![](https://josejuansanchez.org/curso-docker/images/installdockerextension.png)



Después abrimos una nueva ventana de VSCode y movemos la carpeta de la aplicación al editor. Inmediatamente nos aparecerá un mensaje que comunica la existencia de un archivo `devcontainer` y nos da la opción de `reopen folder in a container` , es decir, reabrir la carpeta en un contendedor. Hacer clic sobre esa opción y esperar unos minutos a que se cree el container. 

Una vez terminada la operación, podemos abrir una terminal (barra superior `Terminal > New Terminal` ) y notar que la dirección sobre la se encuentra no es la de la carpeta sino otra. Esto indica que ya estamos dentro del contenedor, donde podemos ejecutar la aplicación mediante el comando

```powershell
python3 app.py
```

Abrir un navegador y colocar en la barra superior la dirección `http://127.0.0.1:4000/` y podremos ver el primera pagina de la app.

Una vez creado el container, no es necesario volver a crearlo. Se puede acceder a el mediante la sección `remote explorer` y abriendo el container adecuado.

![](https://code.visualstudio.com/assets/docs/remote/containers/containers-explorer-python.png)





## Notas de instalación con Pipenv (Opcional).

> Aclaración: Esta modalidad tiene ciertos pre requisitos:
>
> - Contar con python3: Se puede saber si esta instalado mediante el comando `python3 –version` y debe aparecer el mensaje `python 3.*.*`
> - Contar con pip3: Se puede saber si esta instalado mediante el comando `pip3 --version` y debe aparecer el mensaje `pip 9.*.*`
>
> Esto se puede hacer en cualquier SO mediante la guia en la pagina [oficial de python](https://www.python.org/) o el siguiente [video tutorial](https://www.youtube.com/watch?v=9fNKy9zOPkg)

Para ejecutar la aplicación en un browser se debe instalar pipenv mediante el comando:

```
pip install pipenv
```

Luego iniciar el entorno virtual con el comando:
```
pipenv shell
```

Finalmente con el siguiente quedan instaladas todos los módulos necesarios para la aplicación.
```
pipenv install --ignore-pipfile
```

## Notas de desarrollo con Pipenv (Opcional).

Para sistematizar el desarrollo de la aplicación y facilitar el flujo de trabajo, se utiliza pipenv como gestor de paquetes. 

https://pipenv-es.readthedocs.io/es/latest/

En general, instalar pipenv se puede lograr mediante el comando:

```
pip install pipenv
```

Para crear un entorno desde cero se debe ejecutar el comando (idem para iniciar un entorno ya creado):

```
pipenv shell
```

Esto genera un entorno virtual donde nada de lo que se instala quedara de forma permanente en el sistema en que se este ejecutando la aplicación.

Todos los paquetes que se quieran instalar y que sean necesarios para la aplicación en si, se deben instalar mediante el comando:

```
pipenv install <paquete>
```

Si por otro lado, se quiere instalar un modulo solo para el desarrollo, se puede hacer mediante el comando:

```
pipenv install <paquete> --dev
```

Entonces para instalar todos los módulos necesarios (tanto de la aplicación como de desarrollo), se debe ejecutar el comando 

```
pipenv install
```

El comando `pipenv lock` hace un registro de las versiones de los distintos módulos usados y los guarda en el archivo `Pipfile.lock`. Esta es una excelente practica para evitar problemas al momento de desplegar la aplicación. 

Entonces, si se desea instalar lo que se haya registrado en el archivo `Pipfile.lock` y no lo que se marca en el archivo `Pipfile` se debe ejecutar el comando:

```
pipenv install --ignore-pipfile
```

Para salir del entorno virtual, simplemente se debe ejecutar el comando `exit`

## Notas de ejecución con Pipenv (Opcional).

Ejecutar el siguiente comando para iniciar el entorno (si ya se esta ejecutando el entorno, entonces saltear el paso)

```
pipenv shell
```

Finalmente se ejecuta el comando en python

```
python app.py
```

y luego abrir un explorador en la dirección `localhost:4000`. Esto mismo se indica en la terminal al momento de ejecutar la aplicación.
