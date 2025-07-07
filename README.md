# MF0965_3

- **Duración:** 3 horas
- **Lenguaje de desarrollo:** Python 3.x
- **Puntuación total:** 10 puntos

---

## Parte I: Teoría (2 puntos)

*Tiempo estimado 15 minutos*

Cada pregunta tipo test vale **0.25 puntos**. Cada pregunta erronea resta una acertada. Marca la respuesta correcta.

1. **¿Qué es el constructor en una clase?**
   - ☐Un método que se llama al destruir un objeto.
   - ☐Un método que inicializa el estado del objeto al ser creado.
   - ☐Un método para eliminar atributos de un objeto.
   - ☐Un método que permite heredar clases.

2. **¿Cuál de las siguientes afirmaciones describe mejor el Principio de Responsabilidad Única (SRP)?**
   - ☐ Una clase debe depender de abstracciones, no de concreciones.
   - ☐ Cada clase debe tener un solo motivo para cambiar.
   - ☐ Los objetos derivados deben poder sustituir a los objetos base.
   - ☐ Las entidades deben estar abiertas a extensión, pero cerradas a modificación.

3. **El Principio Open/Closed establece que…**

   - ☐ Las clases deben estar abiertas a herencia, pero cerradas a composición.
   - ☐ Los módulos deben poder ampliarse con nuevo comportamiento sin modificar su código fuente.
   - ☐ Cada clase sólo debe tener una responsabilidad.
   - ☐ Los métodos públicos deben tener sólo un parámetro.

4. **Según el Principio de Sustitución de Liskov (LSP), si `B` es subclase de `A`, entonces…**

   - ☐ `B` puede redefinir cualquier método de `A`, incluso cambiando sus parámetros.
   - ☐ Objetos de tipo `B` deben poder usarse en cualquier lugar donde se espere un `A` sin alterar el funcionamiento correcto.
   - ☐ `A` y `B` deben compartir la misma jerarquía de paquetes.
   - ☐ `B` debe hacer uso de polimorfismo paramétrico.

5. **Una tabla está en 1NF si…**
   - ☐ No tiene columnas multivaluadas ni grupos repetitivos.
   - ☐ Todos los atributos dependen funcionalmente de la clave primaria completa.
   - ☐ No existen dependencias transitivas.
   - ☐ Cada columna contiene valores atómicos y ningún conjunto de columnas repetitivo.

6. **¿En qué consiste el principio de encapsulación?**

   - ☐ En hacer todos los métodos y atributos de una clase públicos.
   - ☐ En permitir el acceso a los métodos y atributos de una clase solo a través de sus métodos.
   - ☐ En permitir que una clase herede de varias clases.
   - ☐ En permitir que una clase tenga solo un método.

7. **¿Qué es UML?**

   - ☐ Es un lenguaje para modelar bases de datos.
   - ☐ Es un lenguaje para modelar la estructura de una aplicación orientada a objetos.
   - ☐ Es un lenguaje para programar en orientación a objetos.
   - ☐ Es un lenguaje para modelar interfaces gráficas.

8. **¿Qué significa instanciación en POO?**

   - ☐ El proceso de crear un objeto de una clase.
   - ☐ El proceso de eliminar un objeto de la memoria.
   - ☐ El proceso de copiar un objeto a otro.
   - ☐ El proceso de cambiar los atributos de un objeto.

---

## Parte II: Problemas prácticos con Git

En esta parte debes demostrar tu capacidad para trabajar con control de versiones distribuido. Realiza los siguientes pasos **y registra al menos commit por cada uno**:

### **Servicio web ligero** (2 puntos)

*Tiempo estimado 20 minutos*

Usando **Flask**, implementa un pequeño servicio REST en `app.py` con un endpoint `/saludo/<nombre>` que devuelva JSON:

```json
{ "mensaje": "¡Hola, <nombre>!" }
```

Explica brevemente cómo arrancar la aplicación y probarla con `curl`.

---

### **Ejercicio: CRUD de Países con Tkinter** (6 puntos)

En este ejercicio vais a adaptar la aplicación original de gestión de clientes (“sakila customer”) para trabajar con las tablas `world.country` y `world.city` de la base de datos MySQL.
Sigue los siguientes pasos y organiza cada conjunto de cambios en un **commit independiente**.

---

#### Requisitos generales (Git)

- Mantener la **separación en capas** (UI, Service, Persistence).
- Cada cambio significativo debe ir en un **commit** aparte con mensaje descriptivo. **Cabe la posibiliodad de hacer más commits de los indicados**
- Prueba las operaciones de inserción y actualización en la base de datos real.
- Documenta brevemente en el README cómo ejecutar la aplicación y las dependencias necesarias.

#### Listado de países

*Tiempo estimado 20 minutos*

- Adaptar la capa de persistencia y la lógica de negocio para consultar la tabla `country`.

- La consulta SQL deberá devolver estos campos:

  1. `country.Code`
  2. `country.Name`
  3. `country.Population`

- Mostrar esos resultados en el `Treeview` de la UI.

> **Commit #1:** “Adapta la consulta a world.country de países”.

#### Capitales

*Tiempo estimado 20 minutos*

- Adaptar la capa de persistencia y la lógica de negocio para consultar la tabla `country` junto con la tabla `city` (capital).

- La consulta SQL deberá devolver estos campos:

  1. `country.Code`
  2. `country.Name`
  3. `country.Population`
  4. `city`.`Name` como Capital
  5. `city`.`POPULATION` como Población Capital

- Mostrar esos resultados en el `Treeview` de la UI.

> **Commit #2:** “Mostrar Pais y Capital”.

---

#### Panel de Alta / Edición de Países

*Tiempo estimado 30 minutos*

- Crear una nueva ventana (o diálogo) que sirva para **añadir** o **editar** un país.
- En esta ventana se deberán ver todos los campos del País

> **Commit #2:** “Crear panel de alta/edición de país”.

---

#### Conexión de botones “Añadir” / “Editar”

*Tiempo estimado 20 minutos*

- Modificar los botones de la UI principal para que:
  - Al pulsar **Añadir**, abra el formulario en modo “nuevo país”.
  - Al pulsar **Editar**, abra el mismo formulario rellenado con los datos del país seleccionado.
  - El panel de país tendrá un botón de `Guardar` con un callback que se le pasará como parámetro al instanciarse

> **Commit #4:** “Conectar botones Añadir/Editar al panel de país”.

#### Acción de “Añadir” / “Editar”

*Tiempo estimado 20 minutos*

- Definir un **callback** que se ejecute al pulsar “Guardar” y que invoque al `CountryService` para:
  - Insertar un nuevo registro en `country`
  - O actualizar los datos de un país existente
- Tras guardar los cambios, el `Treeview` deberá refrescarse automáticamente para reflejar la inserción o la actualización.

> **Commit #5:** “Guardar Añade/Editar los paises. Se refresca el listado”.

---
