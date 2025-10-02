# Hotel Pleno Mar Necochea – Sistema de Gestión

## Descripción general
Este repositorio contiene una aplicación desarrollada en Flask para administrar la operación básica de un hotel boutique: registro de habitaciones, clientes y reservas. La interfaz web ofrece vistas y formularios para crear y consultar información, mientras que un script de terminal permite interactuar con los mismos datos desde la línea de comandos.

La persistencia se realiza mediante archivos CSV ubicados en la carpeta `datos/`. Al iniciarse la aplicación se verifica que los archivos existan y, de no estar presentes, se crean con los encabezados apropiados.

## Componentes principales
- **`app.py`**: punto de entrada de Flask. Inicializa los archivos CSV, configura la clave de sesión y registra los *blueprints* de habitaciones, clientes y reservas.
- **`modelos.py`**: define las clases `Habitacion`, `Cliente` y `Reserva`, junto con funciones auxiliares para cargar y guardar información en los CSV.
- **`rutas/`**: contiene tres *blueprints* independientes (`habitaciones`, `clientes` y `reservas`) que encapsulan vistas, validaciones y operaciones de escritura.
- **`templates/`**: plantillas Jinja2 para renderizar la interfaz web. El archivo `base.html` define la estructura global, incluyendo navegación, mensajes flash, pie de página y el menú hamburguesa para pantallas pequeñas.
- **`static/`**: recursos estáticos como hojas de estilo e imágenes. El archivo `static/estilos.css` implementa la responsividad y las reglas visuales de la UI.
- **`main_terminal.py`**: menú interactivo de consola que utiliza las mismas funciones de modelos para operar sin la interfaz gráfica.

## Flujo funcional
1. **Inicio**: la ruta `/` carga `inicio.html`, un panel general para acceder al resto de las funciones.
2. **Habitaciones**:
   - `/habitaciones` lista las habitaciones y permite filtrarlas por estado.
   - `/habitaciones/agregar` crea nuevas habitaciones.
   - `/habitaciones/editar/<numero>` actualiza el estado de una habitación existente reescribiendo el CSV completo para reflejar los cambios.
3. **Clientes**:
   - `/clientes` muestra todos los clientes registrados.
   - `/clientes/agregar` registra un nuevo cliente.
   - `/clientes/editar/<id>` actualiza los datos de un cliente, persistiendo los cambios en bloque.
4. **Reservas**:
   - `/reservas` lista las reservas registradas.
   - `/reservas/agregar` valida que el cliente exista, evita solapamientos con reservas activas y guarda la nueva reserva.
   - `/reservas/cliente/<id_cliente>` presenta el historial de un cliente específico.
   - `/reservas/editar/<id_reserva>` (en revisión) debería permitir actualizar fechas, estado y total. Actualmente requiere correcciones para que los cambios se apliquen correctamente.
   - `/reservas/cancelar/<id_reserva>` marca una reserva como cancelada; esta ruta también necesita ajustes para guardar el estado actualizado y redirigir a la vista correcta.

## Persistencia en CSV
Cada entidad cuenta con funciones `cargar_*` y `guardar_*` que leen o escriben diccionarios serializados en los archivos CSV:
- `datos/habitaciones.csv`
- `datos/clientes.csv`
- `datos/reservas.csv`

El helper `inicializar_csv()` se ejecuta al iniciar la aplicación y crea los archivos con sus encabezados si aún no existen.

## Interfaz de usuario
- **Diseño responsive**: gracias a la hoja de estilos extendida, la interfaz se adapta a móviles, tabletas y escritorio. En anchos de hasta 768px la navegación se oculta detrás de un botón hamburguesa accesible que controla la visibilidad del menú.
- **Modo oscuro**: se conserva mediante `localStorage` a través de `base.html` y la clase `modo-oscuro` aplicada al cuerpo del documento.
- **Mensajes flash**: los *blueprints* emplean `flask.flash` para informar el resultado de operaciones al usuario.

## Uso desde la línea de comandos
El script `main_terminal.py` expone las mismas operaciones de alta y consulta directamente desde terminal. Para ejecutarlo:

```bash
python main_terminal.py
```

## Requisitos e instalación
1. Crear un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación Flask:

   ```bash
   export FLASK_APP=app.py  # En Windows: set FLASK_APP=app.py
   flask run
   ```

   La aplicación quedará disponible en `http://127.0.0.1:5000/`.

4. Para despliegues en producción se incluye un `Procfile` compatible con Gunicorn.

## Estructura de carpetas
```
├── app.py
├── main_terminal.py
├── modelos.py
├── rutas/
├── templates/
├── static/
├── datos/
├── requirements.txt
└── Procfile
```

## Tareas pendientes conocidas
- Corregir la lógica de edición y cancelación de reservas para actualizar correctamente los CSV y mensajes.
- Ajustar el comentario inicial en `modelos.py` para describir con precisión la responsabilidad del módulo.
- Incorporar pruebas automatizadas para la lógica que evita solapamientos de reservas.

Este README proporciona una visión completa de la lógica actual y áreas de mejora, facilitando la colaboración y el mantenimiento continuo del proyecto.
