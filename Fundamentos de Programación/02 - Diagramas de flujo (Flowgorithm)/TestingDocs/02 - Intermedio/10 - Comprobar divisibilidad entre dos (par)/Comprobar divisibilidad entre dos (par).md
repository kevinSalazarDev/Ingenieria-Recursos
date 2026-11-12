# Comprobar divisibilidad entre dos (archivo par)

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

Solicita un entero y evalúa si el residuo de dividirlo para 2 es cero. Informa si es divisible para 2. El contenido coincide exactamente con el archivo 10_impar.fprg; se conservan ambos originales por separado.

## Diagrama de flujo

Abre [10_par.fprg](./10_par.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.