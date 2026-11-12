# Rendimiento de combustible (MPG)

**Nivel:** Principiante · **Herramienta:** Flowgorithm

## Código del diagrama
```xml
<declare name="distancia, galones, mpg" type="Real"/>
<output expression="&quot;Ingrese la distancia a recorrer: &quot;"/>
<input variable="distancia"/>
<output expression="&quot;Ingrese los galones: &quot;"/>
<input variable="galones"/>
<assign variable="mpg" expression="distancia / galones"/>
<output expression="&quot;mpg sera: &quot; &amp; mpg"/>
```

## Explicación

Solicita la distancia recorrida y la cantidad de galones consumidos. Calcula el rendimiento dividiendo la distancia para los galones. Para evitar una división indefinida, ingresa una cantidad de galones distinta de cero.

## Diagrama de flujo

El diagrama editable está en [mpg.fprg](./mpg.fprg). Ábrelo con Flowgorithm para visualizarlo y ejecutarlo. El archivo mpg.png original se conservará en esta carpeta, sin enlazarlo en este Markdown.