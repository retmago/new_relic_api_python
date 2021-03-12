import setuptools

#Si tienes un readme
#with open("README.md", "r") as fh:
#    long_description = fh.read()



setuptools.setup(
     name='py_logs_newrelic',  #nombre del paquete
     version='0.1', #versión
     #scripts=['push_logs.py'] , #nombre del ejecutable
     author="Jose Silva", #autor
     author_email="jsilva2018.95@gmail.com", #email
     description="Un paquete para poder enviar mensajes a la api de new relic", #Breve descripción
     #long_description=long_description,
   #long_description_content_type="text/markdown", #Incluir el README.md si lo has creado
     url="https://github.com/retmago/new_relic_api_python", #url donde se encuentra tu paquete en Github
     packages=setuptools.find_packages(), #buscamos todas las dependecias necesarias para que tu paquete funcione (por ejemplo numpy, scipy, etc.)
     classifiers=[
         "Programming Language :: Python :: 3"
     ],
 ) #aquí añadimos información sobre el lenguaje usado, el tipo de licencia, etc.