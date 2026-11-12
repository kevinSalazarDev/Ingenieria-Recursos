# Ciclo While infinito

**Nivel:** Intermedio · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="bucleNumero" type="Integer"/>
<assign variable="bucleNumero" expression="0"/>
<while expression="True">
    <assign variable="bucleNumero" expression="bucleNumero+1"/>
    <output expression="&quot;Este bucle se ejecutará por siempre...&quot; &amp; bucleNumero"/>
</while>
```

## Explicación

Inicializa un contador en cero y ejecuta un ciclo cuya condición es True. En cada iteración incrementa el contador y lo muestra. No contiene una condición de salida: detén manualmente la ejecución desde Flowgorithm.

## Diagrama de flujo

Abre [7_while_infinito.fprg](./7_while_infinito.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.