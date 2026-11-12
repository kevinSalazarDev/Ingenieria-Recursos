# Menú con Do While

**Nivel:** Intermedio · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="eleccionDelUsuario" type="Integer"/>
<do expression="eleccionDelUsuario !=3">
    <output expression="&quot;Menú del programa:&quot;"/>
    <output expression="&quot;1. Tarea 1&quot;"/>
    <output expression="&quot;2. Tarea 2&quot;"/>
    <output expression="&quot;3. Salir&quot;"/>
    <output expression="&quot;Por favor, seleccione una opción del menú:&quot;"/>
    <input variable="eleccionDelUsuario"/>
    <if expression="eleccionDelUsuario == 1"><then><output expression="&quot;Realizando la tarea 1........&quot;"/></then><else/></if>
    <if expression="eleccionDelUsuario == 2"><then><output expression="&quot;Realizando la tarea 2........&quot;"/></then><else/></if>
</do>
```

## Explicación

Presenta un menú con dos tareas y una opción para salir. El ciclo Do While ejecuta el menú al menos una vez y se repite mientras la opción elegida sea distinta de 3. Las opciones 1 y 2 muestran mensajes; otros valores no muestran una respuesta específica.

## Diagrama de flujo

Abre [8_Dowhile.fprg](./8_Dowhile.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.