# Comparar dos números

**Nivel:** Intermedio · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="n1, n2" type="Real"/>
<output expression="&quot;Ingrese el primer número:&quot;"/>
<input variable="n1"/>
<output expression="&quot;Ingrese el segundo número:&quot;"/>
<input variable="n2"/>
<if expression="n1 &gt; n2">
    <then><output expression="&quot;El número &quot; &amp; n1 &amp; &quot; es mayor&quot;"/></then>
    <else>
        <if expression="n1==n2">
            <then><output expression="&quot;Los dos números son iguales&quot;"/></then>
            <else><output expression="&quot;El número &quot; &amp; n2 &amp; &quot; es mayor&quot;"/></else>
        </if>
    </else>
</if>
```

## Explicación

Lee dos números reales. Mediante condiciones anidadas determina si el primero es mayor, si ambos son iguales o si el segundo es mayor.

## Diagrama de flujo

Abre [4_If.fprg](./4_If.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.