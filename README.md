# Guía de Comandos Git para el Proyecto

## Configuración Inicial (Solo la primera vez)

### Clonar el repositorio

```bash
git clone https://github.com/usuario/nombre-repositorio.git
cd nombre-repositorio
```

### Configurar tu identidad

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

### Crear tu rama personal

```bash
git checkout -b tu-nombre
git push -u origin tu-nombre
```

---

## Comandos Diarios

### Al empezar a trabajar cada día

```bash
git checkout main
git pull origin main
git checkout tu-nombre
git merge main
```

### Guardar tu trabajo

```bash
# Ver qué archivos has modificado
git status

# Añadir todos los cambios
git add .

# Guardar con un mensaje descriptivo
git commit -m "Descripción de lo que has hecho"

# Subir a GitHub
git push origin tu-nombre
```

### Ver el trabajo de un compañero

```bash
# Traer todas las actualizaciones
git fetch origin

# Cambiar a la rama de tu compañero
git checkout rama-compañero
```

### Traer cambios de un compañero a tu rama

```bash
# Volver a tu rama
git checkout tu-nombre

# Integrar cambios de tu compañero
git merge rama-compañero

# Subir los cambios
git push origin tu-nombre
```

---

## Integrar tu Trabajo a Main

### Actualizar tu rama antes de integrar

```bash
git checkout main
git pull origin main
git checkout tu-nombre
git merge main
git push origin tu-nombre
```

### Opción 1: Pull Request (Recomendado)

1. Ve a GitHub
2. Crea un Pull Request de `tu-nombre` hacia `main`
3. Espera la aprobación del equipo
4. Haz merge desde GitHub

### Opción 2: Merge directo

```bash
git checkout main
git merge tu-nombre
git push origin main
```

---

## Resolución de Conflictos

### Cuando aparecen conflictos

```bash
# Ver archivos con conflictos
git status

# Abrir los archivos y buscar:
# <<<<<<< HEAD
# Tu código
# =======
# Código del compañero
# >>>>>>> rama-compañero

# Editar y quedarte con el código correcto
# Eliminar las marcas <<<<<<< ======= >>>>>>>

# Añadir los archivos resueltos
git add .

# Completar el merge
git commit -m "Conflictos resueltos"
git push origin tu-nombre
```

---

## Comandos Útiles

### Ver información

```bash
# Ver historial de cambios
git log --oneline --graph

# Ver todas las ramas (locales y remotas)
git branch -a

# Ver diferencias antes de guardar
git diff

# Ver cambios ya añadidos (después de git add)
git diff --staged
```

### Deshacer cambios

```bash
# Descartar cambios en un archivo (antes de git add)
git checkout -- nombre-archivo

# Quitar archivo del staging (después de git add)
git reset HEAD nombre-archivo

# Deshacer último commit (mantiene los cambios)
git reset --soft HEAD~1
```

### Actualizar

```bash
# Traer cambios de tu rama remota
git pull origin tu-nombre

# Traer info de todas las ramas sin fusionar
git fetch origin
```

---

## Flujo de Trabajo Recomendado

### Rutina diaria completa

```bash
# 1. Al empezar el día - Actualizar
git checkout main
git pull origin main
git checkout tu-nombre
git merge main

# 2. Mientras trabajas - Guardar progreso
git add .
git commit -m "mensaje descriptivo"
git push origin tu-nombre

# 3. Antes de terminar - Actualizar de nuevo
git checkout main
git pull origin main
git checkout tu-nombre
git merge main
```

### Comando rápido todo-en-uno

```bash
# Al empezar
git checkout main && git pull origin main && git checkout tu-nombre && git merge main

# Al guardar
git add . && git commit -m "descripción" && git push origin tu-nombre
```

---

## Ayuda Rápida

Si algo va mal:

```bash
# Ver en qué estado estás
git status

# Ver qué rama estás usando
git branch

# Volver a un estado estable
git checkout tu-nombre
git pull origin tu-nombre
```
