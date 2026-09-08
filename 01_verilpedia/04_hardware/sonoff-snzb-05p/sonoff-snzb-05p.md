# SONOFF SNZB-05P

- **Marca:** SONOFF
- **Nombre:** sensor Zigbee de fugas de agua
- **Modelo:** SNZB-05P
- **Variante adquirida:** sensor de fugas de agua y cable de detección
- **ID de variante en la tienda:** `46197343944945`
- **SKU de la variante:** `6920075779875`
- **Protocolo:** Zigbee 3.0
- **Integración recomendada:** Zigbee2MQTT con Home Assistant

## Alcance

Esta ficha documenta el **SONOFF SNZB-05P** y, en concreto, la presentación seleccionada en la URL de compra: **«Sensor de Fugas de Agua y Cable de Detección»**.

La tienda presenta dos opciones:

| Variante | ID de tienda | SKU |
| --- | --- | --- |
| Solo sensor de fugas de agua | `46197343912177` | `6920075741810` |
| Sensor de fugas de agua y cable de detección | `46197343944945` | `6920075779875` |

La denominación «Estándar» puede resultar ambigua, pero el identificador `variant=46197343944945` de la URL corresponde inequívocamente al kit con cable.

El sensor necesita una pasarela o un coordinador Zigbee. No se conecta directamente a Wi-Fi.

## Funciones

- Detección de fugas mediante las sondas inferiores.
- Detección de gotas mediante el diseño cóncavo de recogida.
- Detección extendida mediante el cable incluido.
- Alerta a partir de aproximadamente **0,5 mm** de líquido.
- Uso sobre superficies metálicas sin falsos positivos provocados únicamente por el metal, gracias a la elevación de las sondas.
- Sondas chapadas en oro para mejorar la resistencia a la corrosión.
- Protección IP67 del cuerpo del sensor.
- Aviso de batería baja y nivel porcentual de batería.
- Reenvío periódico de la alarma mientras persiste el agua.
- Actualizaciones de firmware OTA.
- Integración local con Zigbee2MQTT y ZHA.

El sensor únicamente detecta la presencia o ausencia de agua. No mide la cantidad, la profundidad, el caudal ni la localización exacta del punto mojado a lo largo del cable.

## Principio de detección

La alarma se activa cuando el agua cierra eléctricamente el circuito entre las sondas. El cuerpo incorpora:

- Sondas elevadas para detectar una lámina de agua de unos 0,5 mm.
- Una concavidad que recoge gotas para detectar goteos antes de que se forme un charco.
- Un contacto magnético para conectar el cable detector.

El cable trenzado detecta humedad en cualquier punto sensible de su longitud. Puede rodear una lavadora, un calentador, una tubería o cubrir el perímetro de una zona.

## Especificaciones técnicas

| Especificación | Valor |
| --- | --- |
| Modelo | SNZB-05P |
| MCU | EFR32MG22 |
| Alimentación | 3 V CC |
| Batería | 1 × CR2477, no recargable |
| Autonomía declarada | Hasta 5 años con 50 activaciones diarias |
| Protocolo | Zigbee 3.0 |
| Alcance declarado | Hasta 130 m en espacio abierto |
| Grado de protección | IP67 |
| Material de la carcasa | PC + ABS resistente a rayos UV |
| Dimensiones | 48 × 48 × 21,6 mm |
| Peso neto | 34,3 g sin batería |
| Temperatura de funcionamiento | −10 a 60 °C |
| Humedad de funcionamiento del sensor | 0–100 % HR |
| Humedad recomendada para el cable A4 | 0–80 % HR, sin condensación |
| Altitud de funcionamiento | Menos de 5000 m |
| Tiempo de emparejamiento | 180 s |
| Lugar de uso | Interiores |
| Norma indicada | EN 62368-1 |
| Certificaciones declaradas | CE, FCC, ISED y RoHS |

La autonomía es una estimación de laboratorio y variará con la calidad de la señal, la temperatura, las activaciones, las retransmisiones y la batería empleada.

## Contenido de esta presentación

- Sensor SONOFF SNZB-05P.
- Cable de detección de fugas de agua.
- Batería CR2477 instalada con lengüeta aislante, según el procedimiento de puesta en marcha.
- Guía rápida.

No se ha encontrado una longitud oficial inequívoca para el cable incluido en las fuentes consultadas. Debe medirse en la unidad recibida antes de documentarla.

## Ubicaciones recomendadas

- Debajo de fregaderos y lavabos.
- Junto a calentadores y acumuladores de agua.
- Cerca de lavadoras y lavavajillas.
- Próximo a bombas de achique o sumideros.
- Alrededor de tuberías y válvulas.
- En baños, cocinas, sótanos, bodegas y áticos.
- Bajo muebles o electrodomésticos donde una fuga pueda permanecer oculta.
- Cerca de una bañera para detectar desbordamientos.

Para un punto concreto puede utilizarse el sensor por sí solo. Para cubrir un perímetro, una zona amplia o un lugar estrecho resulta preferible el cable.

## Instalación física

### Sensor sin cable

1. Elige una superficie estable donde el agua probable pueda alcanzar las sondas.
2. Coloca el sensor horizontalmente con las sondas hacia el suelo.
3. Comprueba que la concavidad superior quede expuesta a posibles goteos.
4. Evita lugares donde pueda desplazarse, quedar enterrado o ser golpeado.
5. Realiza una prueba controlada con una pequeña cantidad de agua.

### Sensor con cable

1. Conecta el terminal del cable al contacto magnético del sensor.
2. Extiende el cable por la zona que se desea vigilar, sin tensarlo.
3. No tires, retuerzas ni dobles bruscamente el cable.
4. Evita colocarlo en una zona con condensación habitual o humedad ambiental superior a la recomendada.
5. Prueba varios puntos del cable con una pequeña cantidad de agua.
6. Seca completamente el cable después de cada prueba.

### Varios cables

SONOFF permite conectar varios cables detectores en serie y no declara un límite de longitud total. Una longitud grande puede dificultar localizar el punto exacto de la fuga, aumentar la exposición a humedad ambiental y complicar el diagnóstico; conviene probar toda la instalación después de cada ampliación.

Puede utilizarse un alargador USB Type-C común entre dos cables detectores. Un cable Type-C que se haya mojado en esta instalación no debe reutilizarse posteriormente para cargar dispositivos.

## Resistencia al agua y mantenimiento

El cuerpo tiene clasificación **IP67**, que implica protección frente al polvo y la inmersión temporal en las condiciones normalizadas del ensayo. No significa que esté diseñado para permanecer sumergido indefinidamente.

Después de una detección:

1. Corrige y seca la fuga.
2. Retira el sensor y seca las sondas y la carcasa.
3. Si se ha mojado el cable, déjalo secar por completo antes de reutilizarlo.
4. Comprueba que Home Assistant vuelva a mostrar el estado seco.
5. Ejecuta una prueba controlada antes de devolverlo a servicio.

Una humedad ambiental excesiva o la condensación pueden provocar falsas detecciones en el cable.

## Batería y seguridad

La CR2477 es una pila de botón de litio de 3 V y no debe recargarse.

- Mantén las pilas nuevas y usadas fuera del alcance de los niños.
- La ingestión puede causar quemaduras internas graves en unas dos horas y puede ser mortal.
- Si se sospecha ingestión o introducción en el cuerpo, solicita atención médica inmediata.
- No descargues la pila por la fuerza, la desmontes, la aplastes, la cortes, la incineres ni la calientes por encima de 60 °C.
- No utilices un tipo de batería distinto.
- Respeta la polaridad.
- Si la tapa no cierra de forma segura, deja de usar el producto, retira la pila y mantenla alejada de los niños.
- Retira la batería si el dispositivo no va a utilizarse durante mucho tiempo.
- Recicla la pila de acuerdo con la normativa local; no la arrojes a la basura doméstica ni al fuego.

### Sustitución

1. Gira y retira la tapa inferior.
2. Levanta la cubierta de la batería por ambos lados.
3. Sustituye la CR2477 respetando la polaridad.
4. Cierra completamente la cubierta y la tapa para conservar la protección física.
5. Verifica en Home Assistant que se actualiza el nivel de batería.
6. Realiza una prueba de fuga.

## Indicador y botón

### Indicador LED rojo

| Estado | Significado |
| --- | --- |
| Parpadeo lento durante 180 s | Modo de emparejamiento |
| Encendido durante 3 s y después apagado | Emparejamiento correcto |
| Deja de parpadear y se apaga | Fallo o tiempo agotado |
| Un destello rápido tras pulsar | No está añadido a una pasarela |
| Dos destellos rápidos tras pulsar | Está añadido, en línea y dentro de alcance |
| Parpadeo lento durante 30 s | Comunicación anómala |

### Botón

| Acción | Función |
| --- | --- |
| Pulsación breve | Comprueba la comunicación y el alcance Zigbee |
| Mantener pulsado 5 s | Entra en modo de emparejamiento durante 180 s |

Al encenderse por primera vez mediante la retirada de la lengüeta aislante entra en modo de emparejamiento.

## Integración prioritaria: Zigbee2MQTT

Zigbee2MQTT reconoce expresamente el **SONOFF SNZB-05P** y permite utilizarlo localmente, sin registrar una cuenta eWeLink.

### Requisitos

- Home Assistant.
- Zigbee2MQTT actualizado.
- MQTT configurado.
- Coordinador Zigbee compatible, por ejemplo ZBDongle-P o ZBDongle-E.

### Emparejamiento

1. Retira la tapa inferior y la lengüeta aislante de la batería.
2. Coloca el sensor cerca del coordinador.
3. En Zigbee2MQTT, activa **Permitir unirse**.
4. Mantén pulsado el botón durante cinco segundos.
5. Comprueba que el LED parpadea lentamente.
6. Espera a que la entrevista termine y se identifique como `SNZB-05P`.
7. Asígnale un nombre que incluya la ubicación.
8. Desactiva **Permitir unirse**.
9. Colócalo en la ubicación definitiva y pulsa brevemente el botón.
10. Dos destellos rápidos confirman que puede comunicarse con la red Zigbee.

### Entidades expuestas

| Propiedad | Descripción | Valores | Acceso |
| --- | --- | --- | --- |
| `water_leak` | Estado de fuga | `true` con agua, `false` en seco | Solo publicado |
| `battery` | Batería restante | 0–100 % | Lectura |
| `battery_low` | Aviso de batería casi agotada | `true`, `false` | Solo publicado |

Zigbee2MQTT también declara compatibilidad con **OTA**.

Ejemplo de mensaje publicado:

```json
{
  "water_leak": true,
  "battery": 96,
  "battery_low": false,
  "linkquality": 120
}
```

El valor `linkquality` es orientativo y depende de la red; no aparece entre las tres funciones específicas del dispositivo.

## Integración alternativa: ZHA

SONOFF declara compatibilidad con ZHA mediante ZBDongle-P o ZBDongle-E, incluyendo:

- Estado de fuga.
- Historial mediante Home Assistant.
- Automatizaciones locales.
- Actualización OTA.

Para añadirlo:

1. Ve a **Ajustes → Dispositivos y servicios → ZHA**.
2. Selecciona **Añadir dispositivo**.
3. Mantén pulsado el botón del sensor durante cinco segundos.
4. Espera a que ZHA complete la entrevista.
5. Nombra el dispositivo según su ubicación y prueba la detección.

## Automatizaciones recomendadas en Home Assistant

Una alarma de fuga debe utilizar varios canales y no depender únicamente de una notificación móvil.

Acciones recomendadas:

- Enviar una notificación crítica a varios teléfonos.
- Activar una sirena Zigbee local.
- Encender luces o hacerlas parpadear.
- Cerrar una válvula de agua motorizada.
- Apagar electrodomésticos afectados, si hacerlo es seguro.
- Repetir avisos mientras continúe la fuga.
- Alertar por batería baja o pérdida prolongada de disponibilidad.

### Ejemplo de alerta

Sustituye las entidades y el servicio de notificación:

```yaml
alias: Alerta de fuga de agua
triggers:
  - trigger: state
    entity_id: binary_sensor.snzb_05p_water_leak
    to: "on"
actions:
  - action: notify.mobile_app_telefono
    data:
      title: "Fuga de agua"
      message: "El sensor de la lavandería ha detectado agua."
  - action: switch.turn_on
    target:
      entity_id: switch.sirena_local
mode: single
```

### Ejemplo de batería baja

```yaml
alias: Batería baja del sensor de fugas
triggers:
  - trigger: state
    entity_id: binary_sensor.snzb_05p_battery_low
    to: "on"
actions:
  - action: notify.mobile_app_telefono
    data:
      title: "Batería baja"
      message: "Sustituye la CR2477 del sensor de fugas."
mode: single
```

Los identificadores reales pueden diferir. Deben seleccionarse desde la interfaz de automatizaciones de Home Assistant.

## Repetición de alarmas

Con firmware **V1.0.2 o posterior**, SONOFF indica que el sensor vuelve a transmitir la alarma cada **10 minutos** mientras continúe detectando agua. Esto reduce el riesgo de perder un único mensaje por una incidencia temporal de red.

No sustituye una prueba real ni garantiza la entrega de notificaciones externas. Conviene:

- Actualizar el firmware mediante OTA.
- Configurar escenas locales.
- Mantener varias rutas de aviso.
- Verificar periódicamente la batería y la cobertura.

## Uso con eWeLink

Pasarelas compatibles declaradas:

- ZBBridge.
- ZBBridge-P.
- ZBBridge-U.
- NSPanel Pro.
- iHost.

La matriz oficial distingue:

| Plataforma | Fuga | Historial | Escena local | OTA |
| --- | ---: | ---: | ---: | ---: |
| ZBBridge clásico | Sí | Sí | No | No |
| ZBBridge-P, ZBBridge-U, NSPanel Pro e iHost | Sí | Sí | Sí | Sí |
| Home Assistant con ZHA | Sí | Sí | Sí | Sí |
| Home Assistant con Zigbee2MQTT | Sí | Sí | Sí | Sí |
| SmartThings Hub V3/Aeotec V3 | Sí | Sí | Sí | No especificado |

SONOFF declara no compatibles las pasarelas Philips, Alexa, IKEA y Fritzbox.

En eWeLink puede consultarse el estado, la batería y el historial. El sensor puede actuar como condición de una escena —fuga o ausencia de fuga—, pero no como dispositivo que ejecute una acción.

Las alarmas locales de una pasarela compatible pueden seguir funcionando aunque falle Wi-Fi o Internet. Las notificaciones de la aplicación, el correo, SMS o IFTTT dependen de la pasarela, la conectividad y, en algunos casos, de un plan avanzado de eWeLink.

## Apple Home

El SNZB-05P no es un accesorio Matter nativo. SONOFF permite exponerlo a Apple Home mediante un Matter Bridge:

- ZBBridge-U.
- eWeLink CUBE en iHost.

Primero se añade el sensor al bridge Zigbee y después se incorpora el bridge a Apple Home mediante Matter. La disponibilidad exacta de batería, avisos y otros atributos dependerá del bridge y de la versión de Apple Home.

## Pruebas y mantenimiento periódico

Como mínimo:

1. Inspecciona mensualmente que el sensor y el cable no se hayan desplazado.
2. Pulsa brevemente el botón y comprueba que emite dos destellos.
3. Haz una prueba controlada con agua en las sondas y en varios puntos del cable.
4. Confirma que llegan todos los avisos y se ejecutan las escenas locales.
5. Seca completamente el conjunto y comprueba que vuelve al estado normal.
6. Revisa la batería y la disponibilidad en Home Assistant.
7. Repite la prueba después de actualizar firmware, cambiar el coordinador o modificar la red Zigbee.

## Solución de problemas

### Se desconecta con frecuencia

- Reduce la distancia al coordinador.
- Añade routers Zigbee alimentados por red.
- Evita obstáculos metálicos y fuentes de interferencia.
- Revisa el canal Zigbee y el Wi-Fi de 2,4 GHz.
- Pulsa brevemente el botón en la ubicación definitiva: dos destellos indican comunicación correcta.

### Aparece en línea después de retirar la batería

Los sensores alimentados por batería se comunican con poca frecuencia. La pasarela necesita esperar a que venza su tiempo de disponibilidad. SONOFF indica aproximadamente una hora con ZBBridge-P, pero otras plataformas pueden tardar varias horas.

### El cable genera falsos positivos

1. Comprueba que esté completamente seco.
2. Revisa si existe condensación.
3. Mantén la humedad ambiental dentro del intervalo recomendado de 0–80 % HR sin condensación.
4. Desconecta extensiones y prueba cada tramo por separado.
5. Inspecciona conectores, dobleces y daños.

### Faltan funciones después de añadirlo

Actualiza la aplicación y el firmware de la pasarela. Si se incorporó con una versión antigua, elimínalo, actualiza la pasarela y vuelve a emparejarlo. Con Home Assistant, actualiza Zigbee2MQTT o ZHA y reconfigura o entrevista nuevamente el dispositivo.

### No vuelve al estado seco

Seca las sondas, el cable completo, los terminales y la superficie. La humedad retenida en el trenzado o el conector puede mantener cerrado el circuito.

## Datos y privacidad

La declaración del Reglamento europeo de Datos indica que el SNZB-05P genera:

- Modelo y versión de firmware.
- Eventos de detección de agua.
- Porcentaje de batería.

SONOFF declara que la información del dispositivo ocupa hasta 128 bytes por evento y los parámetros de estado 4 bytes por evento. No se generan de manera continua ni en tiempo real. En el ecosistema eWeLink pueden almacenarse localmente y en la nube durante el ciclo de vida del dispositivo.

Los datos pueden consultarse o modificarse desde la aplicación, pero el documento indica que no pueden descargarse; el conjunto del dispositivo puede eliminarse. El contacto declarado para acceso, recuperación o borrado es `dpo@sonoff.tech`.

El uso directo con Zigbee2MQTT o ZHA evita registrar el sensor en la nube de SONOFF, aunque Home Assistant y MQTT conservarán los datos según la configuración local.

## Declaración UE de conformidad

La declaración UE identifica el modelo **SNZB-05P** y los SKU:

- `6920075741810`
- `6920075779851`
- `6920075779868`
- `6920075779875`

Declara conformidad con:

- Directiva de equipos radioeléctricos 2014/53/UE.
- Directiva RoHS 2011/65/UE.
- Directiva RAEE 2012/19/UE.

| Norma | Informe |
| --- | --- |
| EN 62368-1:2014+A11:2017 | CTC20240121S01 |
| EN 62479:2010; EN 50663:2017 | CTC20240121E03 |
| ETSI EN 301 489-1 V2.2.3; ETSI EN 301 489-17 V3.2.4 | CTC20240121E01 |
| ETSI EN 300 328 V2.1.1 | CTC20240121E02 |
| EN IEC 63000:2018 | Sin número de informe indicado |

El organismo notificado es **Nemko North America, Inc.**, certificado `1622-RED-240467`, número `1622`. La declaración fue emitida el **13 de junio de 2024** y firmada por **Stan Li**, responsable de certificación.

| Entidad | Datos |
| --- | --- |
| Fabricante | Shenzhen Sonoff Technologies Co., Ltd. |
| Dirección | 3F y 6F, edificio A, n.º 663, Bulong Road, Shenzhen, Guangdong, China |
| Representante autorizado en la UE | EUREP GmbH |
| Dirección UE | Unterlettenweg 1a, 85051 Ingolstadt, Alemania |
| Correo de asistencia | support@itead.cc |

El sensor y la batería deben entregarse en los sistemas de recogida correspondientes y no desecharse con residuos domésticos sin clasificar.

## Fuentes internas

- [Manual de usuario SNZB-05P V1.0](User-Manual-SNZB-05P-EN-V1.0.pdf) — especificaciones, elementos, instalación, cable detector, batería, seguridad y conformidad.
- [Guía rápida SNZB-05P V1.2](Quick-Guide-SNZB-05P-V1.2.pdf) — puesta en marcha y emparejamiento.
- [Declaración UE de conformidad](SONOFF_SNZB-05P_CE_DoC.pdf) — SKU, directivas, normas, ensayos y responsables.
- [Declaración del Reglamento europeo de Datos](SONOFF_SNZB-05P_Data_Rev.0.pdf) — datos generados, almacenamiento y derechos del usuario.

## Fuentes externas

- [Página comercial oficial del SONOFF SNZB-05P](https://sonoff.tech/es-es/products/sonoff-zigbee-water-leak-sensor-snzb-05p) — presentación adquirida, diseño, detección, cable, autonomía, especificaciones, casos de uso y preguntas frecuentes.
- [Centro de conocimiento oficial SNZB-05P](https://help.sonoff.tech/docs/snzb-05p) — especificaciones ampliadas, indicadores, pasarelas, instalación y solución de problemas; actualizado el 2 de febrero de 2026.
- [SONOFF SNZB-05P en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/SNZB-05P.html) — entidades, identificación y OTA; actualizado el 31 de mayo de 2026.
