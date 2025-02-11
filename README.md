# 👁️ Ocularis Luna 🌙

Cálcula las fases de la luna dentro de un rango de fechas.

## ✨ Características

- 💻 Fácil de usar.
- 🎨 Paleta de colores amigable.
- 📚 Plataforma educativa.

## ⚡️ Requerimientos

**Python** con los siguientes paquetes:

- Flask
- Skyfield
- Matplotlib
- pip-tools

## ⚙️ Configuración

Es recomendable utilizar un **entorno virtual** de **Python**.

Es importante tener en cuenta que el procedimiento cambia dependiendo del sistema operativo. Aquí se detalla el proceso para los sisemas basados en **GNU/Linux**.

Para definir el **entorno virtual** hay que utilizar el siguiente comando:

```
python3 -m venv .venv
```

> **.venv** es un nombre genérico para entornos virtuales. Más información en la [documentación](https://docs.python.org/3/library/venv.html) oficial.

Para activar el entorno virtual:

```
source .env/bin/activate
```

Verificamos que utilizamos el **entorno virtual**:

```
which python
```

> A partir de aquí todo se reliza en el entorno virtual.

Ahora hay que instalar el paquete **pip-tools**, cuya función es instalar de una forma compatible los paquetes que vayamos a requerir. Para ello se usa el siguiente comando:

```
python3 -m pip install pip-tools
```

En el archivo **requirements**.in se encuentran los paquetes a instalar. Hay que preparar los paquetes para su instalación. Para esto hay que compilar el archivo, lo cual genera un archivo **requirements.txt**.

Esto se efectua con el comando:

```
pip-compile
```

> El archivo **requirements.txt** ya se ecnuentra compilado.

Luego se procede a sincronizar los cambios para instalar los paquetes. Lo cual se realiza con el comando:

```
pip-sync
```

> Más información sobre **pip-tools** en la [documentación](https://github.com/jazzband/pip-tools) oficial.

Con esto el entorno está listo para ejecutar el programa.

Para **desactivar el entorno virtual** hay que utilizar el siguiente comando:

```
deactivate
```
