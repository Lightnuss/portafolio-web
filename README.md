# portafolio-web


Agregar token:
Settings -> Developer settings -> Personal access tokens (classic)

## Configurar usuario y correo de forma local:
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com


##Hacer clon del proyecto con una rama en especifico y el token
git clone -b <javier> https://<token>/LuisDiazDUOC-UC/seccion_005v.git

git add .
git commit -m ""
git push origin alumno1



#cambiar a rama "main" desde otra rama
git checkout main
#Unir rama principal a rama "alumno1" (Requiere paso anterior)
git merge alumno1
#enviar rama main ya unida con rama alumno1 a github
git push origin main

### VER RAMAS:
git log
### Ver ramas simplificado:
git log --oneline

### CREAR RAMA NUEVA DESDE TERMINAL (Se hace desde rama main)
git branch rama1
### Cambiar a rama creada en el paso anterior:
git checkout rama1

##Agregar token en caso que el repositorio lo haya creado con "git init":
git remote set-url origin https://<token>@github.com/LuisDiazDUOC-UC/repo_ejemplo_005v.git
