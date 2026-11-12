# Comprobar divisibilidad entre dos (archivo impar)

**Nivel:** Intermedio · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="n" type="Integer"/>
<output expression="&quot;Ingrese el número para comprobar si es divisible para 2&quot;"/>
<input variable="n"/>
<if expression="n % 2 == 0">
    <then><output expression="&quot;El número &quot; &amp; n &amp; &quot; sí es divisible para 2&quot;"/></then>
    <else><output expression="&quot;El número &quot; &amp; n &amp; &quot; no es divisible para 2&quot;"/></else>
</if>
```

## Explicación

El nombre sugiere comprobar números impares, pero el diagrama contiene la misma condición que 10_par.fprg: n % 2 == 0, con mensajes para ambos resultados. No se modifica el algoritmo ni se presenta como una solución diferente.

## Diagrama de flujo

Abre [10_impar.fprg](./10_impar.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.