# Ciclos For anidados

**Nivel:** Intermedio · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="N, i, j" type="Integer"/>
<declare name="dibujeCaracter" type="String"/>
<assign variable="dibujeCaracter" expression="&quot;*&quot;"/>
<output expression="&quot;Ingrese el número de filas&quot;"/>
<input variable="N"/>
<for variable="i" start="1" end="N" direction="inc" step="1">
    <for variable="j" start="1" end="N" direction="inc" step="1">
        <output expression="dibujeCaracter"/>
    </for>
    <output expression="&quot; &quot;"/>
</for>
```

## Explicación

Solicita un número y utiliza dos ciclos For anidados para repetir la impresión del carácter *. En el archivo original cada asterisco se imprime con salto de línea, por lo que no se forma una cuadrícula de columnas. Se conserva ese comportamiento.

## Diagrama de flujo

Abre [9_For_anidados_mal.fprg](./9_For_anidados_mal.fprg) con Flowgorithm para visualizar y ejecutar el diagrama. Todavía no hay una exportación SVG.