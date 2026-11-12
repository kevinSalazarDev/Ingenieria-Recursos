# Aprobado o suspendido

**Nivel:** Intermedio · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="nota" type="Real"/>
<output expression="&quot;Ingrese su nota:&quot;"/>
<input variable="nota"/>
<if expression="nota &gt;= 40">
    <then><output expression="&quot;Aprobado&quot;"/></then>
    <else><output expression="&quot;Suspendido&quot;"/></else>
</if>
```

## Explicación

Solicita una nota y comprueba si es mayor o igual a 40. Si se cumple la condición muestra «Aprobado»; de lo contrario, muestra «Suspendido».

## Diagrama de flujo

Abre [3_if.fprg](./3_if.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.