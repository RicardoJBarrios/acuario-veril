# Normas de edición de la implementación de Veril

## Alcance

- Documentar únicamente decisiones, pendientes, fuentes de diseño y criterios de aceptación de la implementación vigente de Veril
- Mantener la explicación general de cada dimensión en las fichas de `fichas/dimensiones/`
- Enlazar las dimensiones en lugar de repetir sus definiciones, fundamentos o debates generales
- Mantener separadas las responsabilidades de espacio, hidráulica, iluminación, biología, química y procesamiento, aunque roca y sustrato se documenten conjuntamente en la ficha espacial
- Utilizar `configuracion.md` como documento integrador de las decisiones entre dimensiones, sin convertirlo en una repetición de sus fichas
- Mantener puntos de aplicación para las siete dimensiones; cuando una dimensión no requiera una ficha independiente, enlazar claramente sus documentos propietarios
- No convertir estas fichas en recomendaciones reutilizables para otros acuarios

## Contenido de las fichas

- Describir la configuración concreta, sus medidas, posiciones, materiales, equipos y condiciones previstas
- Conservar como pendientes las mediciones, pruebas y decisiones que aún no se hayan ejecutado
- Enlazar las fichas propietarias de hardware, productos, biología, ciclado y dimensiones cuando sean necesarias
- Documentar los criterios de aceptación observables para cada decisión
- Mantener las decisiones de población y organismos concretos en sus fichas propias, salvo cuando afecten directamente a la ocupación del display y a la implementación de Veril
- Documentar la aplicación concreta de Química mediante las fichas de parámetros y los planes operativos, y la de Procesamiento mediante sus fichas de dimensión, hardware y ciclado o maduración
- Mantener el ciclado en `ciclado/` y la maduración en `maduracion/` como documentación operativa separada; `veril/` solo define las condiciones que esos planes deben comprobar

## Redacción y comprobación

- No presentar una decisión de Veril como regla universal
- No repetir explicaciones generales de procesamiento, comunidad, organización física o espacio
- Usar enlaces internos relativos
- Escribir en español correcto y conservar las unidades documentadas
- Comprobar los enlaces y ejecutar `git diff --check` antes de terminar
