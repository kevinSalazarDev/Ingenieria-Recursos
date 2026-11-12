# Ciclo While hasta SALIR

**Nivel:** Intermedio · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="name" type="String"/>
<assign variable="name" expression="&quot;&quot;"/>
<while expression="name != &quot;SALIR&quot;">
    <output expression="&quot;Ingrese el nombre de su amigo:&quot;"/>
    <input variable="name"/>
    <if expression="name !=&quot;SALIR&quot;">
        <then><output expression="&quot;El nombre de su amigo es:&quot; &amp; name"/></then>
        <else/>
    </if>
</while>
```

## Explicación

Solicita nombres repetidamente mientras el texto ingresado sea diferente de «SALIR». Cada nombre distinto de esa palabra se muestra en pantalla. La comparación debe coincidir con el texto de salida.

## Diagrama de flujo

Abre [6_while.fprg](./6_while.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.