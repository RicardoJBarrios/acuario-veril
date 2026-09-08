# SONOFF iPlug Zigbee S60ZBTPF

- **Marca:** SONOFF
- **Nombre comercial:** SONOFF iPlug Zigbee Smart Plug
- **Modelo:** S60ZBTPF
- **Variante:** toma europea tipo E/F
- **Protocolo:** Zigbee 3.0
- **Integración recomendada:** Zigbee2MQTT con Home Assistant

## Alcance

Esta ficha documenta el **SONOFF S60ZBTPF**, la variante europea de 16 A de la serie S60 Zigbee. No debe confundirse con:

- **S60TPF:** versión Wi-Fi de aspecto similar.
- **S60ZBTPG:** versión Zigbee con toma británica tipo G, limitada a 13 A y 3250 W.
- **S60ZBTPFR2:** revisión incluida junto al S60ZBTPF en la declaración UE de conformidad.

El dispositivo necesita un coordinador o una pasarela Zigbee. No se conecta directamente a una red Wi-Fi y no funciona de manera autónoma como dispositivo inteligente.

## Funciones principales

- Encendido y apagado remoto.
- Medición instantánea de tensión, corriente y potencia.
- Consumo acumulado e histórico de energía.
- Protección configurable contra sobrecargas.
- Programaciones, cuentas atrás y modo pulso.
- Comportamiento configurable después de un corte eléctrico.
- Indicador de red desactivable.
- Actualizaciones de firmware OTA.
- Funcionamiento como **router o repetidor Zigbee** alimentado permanentemente.
- Integración directa con Zigbee2MQTT y ZHA.
- Integración con eWeLink mediante una pasarela SONOFF compatible.

## Funcionamiento local y red Zigbee

El S60ZBTPF actúa como router Zigbee y amplía la cobertura de la malla para otros dispositivos. SONOFF declara que puede admitir hasta **64 dispositivos finales** como repetidor, aunque la capacidad y estabilidad reales dependen del coordinador, la topología, las interferencias y el firmware.

Con Zigbee2MQTT o ZHA, el control, las mediciones y las automatizaciones pueden permanecer dentro de la red local. No se necesita eWeLink ni la nube de SONOFF. Una caída de Internet no impide el control local siempre que Home Assistant, el coordinador y la red local sigan operativos.

> La función de router no convierte el enchufe en coordinador: sigue siendo necesario un coordinador Zigbee conectado a Home Assistant o una pasarela.

## Especificaciones técnicas

| Especificación | S60ZBTPF |
| --- | --- |
| MCU | TLSR8656 |
| Entrada | 250 V~, 50/60 Hz, máximo 16 A |
| Carga máxima | 4000 W, carga resistiva |
| Tipo de toma | E/F; admite clavijas C, E y F compatibles |
| Protocolo | Zigbee 3.0 |
| Banda de radio | 2405–2480 MHz |
| Potencia de radio CE | ≤ 10 dBm |
| Consumo en espera | < 1 W |
| Material | PC V-0 según la página y el centro de ayuda |
| Dimensiones | 50 × 50 × 61,5 mm |
| Peso neto | 79 g según la ficha web actual |
| Color | Blanco |
| Lugar de uso | Interiores |
| Temperatura de funcionamiento | −10 a 40 °C |
| Humedad de funcionamiento | 5–95 % HR, sin condensación |
| Altitud máxima indicada | Menos de 2000 m |
| Certificaciones declaradas | CE y RoHS |

El manual V1.1 indica **83 g** y describe el material únicamente como PC, mientras que la página actual y el centro de ayuda indican **79 g** y PC V-0. Se conservan como preferentes los datos web más recientes, dejando constancia de la discrepancia.

## Cargas adecuadas y no recomendadas

SONOFF recomienda utilizar cargas resistivas dentro de los valores nominales. Ejemplos habituales:

- Lámparas y monitores.
- Cafeteras, arroceras y hervidores.
- Calefactores resistivos que no superen la potencia permitida.
- Cargadores de teléfonos o tabletas.

No se recomienda:

- Conectar aires acondicionados, frigoríficos, lavadoras u otras cargas inductivas de motor con corrientes de arranque elevadas.
- Cargar vehículos eléctricos.
- Conectar una regleta al enchufe, ya que facilita superar inadvertidamente su carga máxima.

Los 16 A y 4000 W son límites máximos para cargas resistivas, no una recomendación de uso continuo con cualquier tipo de aparato.

## Seguridad eléctrica

Antes del enchufe debe existir una protección de **16 A**:

- Interruptor magnetotérmico o automático en miniatura (**MCB**), o
- Interruptor diferencial con protección contra sobrecorriente integrada (**RCBO**).

Advertencias del fabricante:

1. Existe riesgo de descarga eléctrica. No es un juguete y está destinado al uso por adultos.
2. Solo debe utilizarse en interiores y en climas moderados.
3. No debe cubrirse con periódicos, manteles, cortinas u objetos que impidan la ventilación.
4. No deben colocarse cerca llamas abiertas, como velas.
5. Debe mantenerse una separación mínima de 20 cm entre la antena y el cuerpo durante el uso normal.
6. El límite máximo de corriente y potencia permanece activo por seguridad aunque no se haya habilitado la protección de sobrecarga configurable.

## Elementos e indicadores

### Botón

| Acción | Resultado |
| --- | --- |
| Pulsación breve | Enciende o apaga la salida |
| Mantener pulsado 5 segundos | Entra en modo de emparejamiento o restablece los ajustes de fábrica |

Al encenderse por primera vez entra automáticamente en modo de emparejamiento durante **180 segundos**.

### Indicador de red azul

| Estado | Significado |
| --- | --- |
| Encendido fijo | Conexión normal con la pasarela o coordinador |
| Parpadeo lento | Modo de emparejamiento |
| Parpadeo rápido | Conexión anómala con la pasarela |
| Parpadeo rápido y continuo | Bloqueo por protección contra sobrecarga |

### Indicador de alimentación rojo

| Estado | Significado |
| --- | --- |
| Encendido | La salida está activada |
| Apagado | La salida está desactivada |

## Integración prioritaria: Zigbee2MQTT

Zigbee2MQTT reconoce explícitamente el modelo **SONOFF S60ZBTPF**. Esta es la opción prioritaria porque mantiene la operación local y expone el conjunto más detallado de medición, configuración y protección sin depender de una pasarela SONOFF.

### Requisitos

- Home Assistant.
- Zigbee2MQTT actualizado.
- Un coordinador compatible, por ejemplo SONOFF ZBDongle-P o ZBDongle-E.
- MQTT configurado entre Zigbee2MQTT y Home Assistant.

### Emparejamiento

1. Conecta el S60ZBTPF a una toma cercana al coordinador.
2. En Zigbee2MQTT, activa **Permitir unirse**.
3. Si el indicador azul no parpadea lentamente, mantén pulsado el botón durante cinco segundos.
4. Espera a que se complete la entrevista y aparezca como `S60ZBTPF`.
5. Asigna un nombre descriptivo y desactiva **Permitir unirse**.
6. Trasládalo a su ubicación definitiva y comprueba el enlace y las mediciones.

Si no se incorpora, actualiza Zigbee2MQTT y el firmware del coordinador, reinicia la incorporación y repite el restablecimiento cerca del coordinador.

### Entidades expuestas por Zigbee2MQTT

| Propiedad | Función | Unidad o valores | Acceso |
| --- | --- | --- | --- |
| `state` | Estado y control del relé | `ON`, `OFF`, `TOGGLE` | Lectura y escritura |
| `energy` | Energía total acumulada | kWh | Publicada |
| `current` | Corriente instantánea | A | Lectura |
| `voltage` | Tensión instantánea | V | Lectura |
| `power` | Potencia activa instantánea | W | Lectura |
| `energy_yesterday` | Energía de ayer | kWh | Lectura |
| `energy_today` | Energía de hoy | kWh | Lectura |
| `energy_month` | Energía del mes | kWh | Lectura |
| `power_on_behavior` | Estado después de recuperar la alimentación | `off`, `on`, `toggle`, `previous` | Lectura y escritura |
| `network_indicator` | Activa o desactiva el indicador azul de red | `true`, `false` | Lectura y escritura |
| `inching_control_set` | Modo pulso con cambio automático de estado | Objeto compuesto | Escritura |
| `outlet_control_protect` | Activa la protección de la salida | `true`, `false` | Lectura y escritura |
| `overload_protection` | Límites de potencia, tensión y corriente | Objeto compuesto | Lectura y escritura |

Zigbee2MQTT también permite calibrar y limitar los decimales mostrados para energía, corriente, tensión y potencia. Las calibraciones son correcciones porcentuales y se aplican en el siguiente informe.

### Control mediante MQTT

Sustituye `FRIENDLY_NAME` por el nombre asignado y publica en:

`zigbee2mqtt/FRIENDLY_NAME/set`

Encender:

```json
{"state":"ON"}
```

Apagar automáticamente después de cinco minutos, si el firmware admite el temporizador Zigbee estándar:

```json
{"state":"ON","on_time":300}
```

Restaurar el estado anterior después de un corte:

```json
{"power_on_behavior":"previous"}
```

Desactivar el indicador azul:

```json
{"network_indicator":false}
```

Configurar modo pulso:

```json
{
  "inching_control_set": {
    "inching_control": "ENABLE",
    "inching_time": 30,
    "inching_mode": "ON"
  }
}
```

El tiempo de pulso admite valores entre **0,5 y 3599,5 segundos**.

### Protección contra sobrecarga

Zigbee2MQTT expone:

| Parámetro | Intervalo |
| --- | --- |
| Potencia máxima | 0,1–4000 W |
| Potencia mínima opcional | 0,1–4000 W |
| Tensión máxima opcional | 165–277 V |
| Tensión mínima opcional | 165–277 V |
| Corriente máxima | 0,1–17 A |
| Corriente mínima opcional | 0,1–17 A |

La potencia y corriente máximas son obligatorias dentro del objeto de configuración; los límites inferiores y de tensión son opcionales y tienen su propio selector de activación.

Ejemplo meramente orientativo para una carga de hasta 10 A:

```json
{
  "outlet_control_protect": true,
  "overload_protection": {
    "max_power": 2300,
    "enable_min_power": "DISABLE",
    "min_power": 0.1,
    "enable_max_voltage": "ENABLE",
    "max_voltage": 253,
    "enable_min_voltage": "ENABLE",
    "min_voltage": 207,
    "max_current": 10,
    "enable_min_current": "DISABLE",
    "min_current": 0.1
  }
}
```

Los umbrales deben adaptarse al aparato y a la instalación. No amplían la capacidad nominal del enchufe ni sustituyen las protecciones del cuadro eléctrico.

### Actualizaciones OTA

Zigbee2MQTT declara compatibilidad con actualizaciones OTA. Antes de actualizar:

- Mantén el enchufe alimentado y con buena cobertura.
- No desconectes el coordinador ni reinicies Zigbee2MQTT.
- Evita controlar una carga crítica durante el proceso.

## Integración alternativa: ZHA

SONOFF declara compatibilidad con Home Assistant mediante ZHA usando ZBDongle-P o ZBDongle-E. La matriz oficial atribuye a ZHA:

- Encendido y apagado.
- Monitorización de energía.
- Protección contra sobrecarga.
- Estado al recuperar la alimentación.
- Actualizaciones OTA.

No atribuye a ZHA la configuración del modo pulso. Las entidades exactas pueden variar según la versión de Home Assistant y el firmware del dispositivo.

El emparejamiento se realiza desde **Ajustes → Dispositivos y servicios → ZHA → Añadir dispositivo**, manteniendo pulsado el botón cinco segundos si no entra automáticamente en modo de unión.

## Uso con pasarelas SONOFF y eWeLink

Pasarelas recomendadas por el manual:

- ZBBridge-P.
- ZBBridge-U.
- NSPanel Pro.
- iHost.

La compatibilidad funcional oficial no es idéntica:

| Pasarela o plataforma | Encendido | Energía | Sobrecarga | Modo pulso | Estado tras corte | OTA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| ZBBridge clásico | Sí | No | No | No | No | No |
| ZBBridge-P, ZBBridge-U, NSPanel Pro e iHost | Sí | Sí | Sí | Sí | Sí | Sí |
| Amazon Echo con Zigbee | Sí | No | No | No | No | No |
| SmartThings Hub V3 o Aeotec equivalente | Sí | No | No | No | No | No |
| Home Assistant con Zigbee2MQTT | Sí | Sí | Sí | Sí | Sí | Sí |
| Home Assistant con ZHA | Sí | Sí | Sí | No | Sí | Sí |

SONOFF indica que no son compatibles las pasarelas Philips ni determinadas pasarelas-router Zigbee alemanas. Si el dispositivo no se añade, recomienda actualizar primero el firmware de la pasarela.

### Funciones de eWeLink

Con una pasarela SONOFF plenamente compatible, eWeLink ofrece:

- Consumo de ayer, hoy y del mes actual.
- Corriente, tensión y potencia en tiempo real.
- Consulta y exportación de seis meses de consumo.
- Horarios, cuenta atrás y ciclos recurrentes.
- Protección por umbrales y restauración remota.
- Compartición del dispositivo.
- Escenas por estado, potencia y energía diaria o mensual.
- Avisos de estado y consumo.
- Aviso cinco minutos después de quedar fuera de línea.
- Historial de operaciones de los últimos tres meses.
- Estado al recuperar la alimentación y modo pulso.
- Sincronización mediante cuenta con Alexa, Google Home, IFTTT, SmartThings y Alice.

La mención de «control LAN» en el centro de ayuda describe una función de eWeLink, pero este dispositivo Zigbee se comunica con su pasarela, no directamente con el router IP.

## Apple Home

El S60ZBTPF no es un accesorio Matter nativo. Puede incorporarse a Apple Home mediante un **Matter Bridge**, por ejemplo:

- ZBBridge-U compatible.
- eWeLink CUBE ejecutado en iHost.

El flujo general consiste en añadir primero el enchufe Zigbee al bridge, habilitar el bridge Matter, incorporarlo a Apple Home con su código Matter y exponer el dispositivo. Las funciones visibles en Apple Home pueden ser más limitadas que en Zigbee2MQTT o eWeLink; la monitorización detallada de energía y la configuración de protecciones no deben darse por supuestas.

## Temporizadores y ausencia de conexión

- Si el enchufe pierde la conexión Zigbee con la pasarela, los temporizadores alojados en ella no se ejecutan.
- Si la pasarela conserva la conexión Zigbee pero pierde Internet, SONOFF indica que los temporizadores continúan funcionando.
- Con Home Assistant, el resultado depende de que Home Assistant, Zigbee2MQTT o ZHA, MQTT cuando corresponda y el coordinador continúen operativos.

Para automatizaciones críticas conviene comprobar el comportamiento real y no depender exclusivamente de servicios en la nube.

## Restablecimiento

Hay dos métodos indicados:

1. Mantener pulsado el botón durante cinco segundos.
2. Eliminar el dispositivo de la pasarela y después restablecerlo.

El mismo gesto de cinco segundos activa el emparejamiento, por lo que después de un restablecimiento deberá volver a incorporarse a la red.

## Solución de problemas

### Se apaga aunque la protección configurable esté desactivada

Los límites máximos internos de corriente y potencia permanecen activos por seguridad. Si se superan, el enchufe corta la salida para reducir el riesgo de sobrecalentamiento o incendio.

### El indicador azul parpadea rápidamente

La conexión con la pasarela es anómala. Revisa:

- Alimentación y estado del coordinador.
- Cobertura y calidad de enlace.
- Canal Zigbee e interferencias Wi-Fi.
- Disponibilidad de routers Zigbee intermedios.
- Firmware de la pasarela y del dispositivo.

### El indicador azul parpadea rápida y continuamente

El dispositivo está bloqueado por protección contra sobrecarga. Desconecta la carga, comprueba su consumo y la instalación, y solo después restablece o reactiva la salida.

### La televisión no vuelve a encenderse con su mando

Cuando el S60ZBTPF apaga la salida, elimina completamente la alimentación del televisor. Primero hay que volver a encender el enchufe y después utilizar el mando.

### No aparecen todas las entidades

1. Actualiza Zigbee2MQTT o Home Assistant/ZHA.
2. Comprueba que se haya completado la entrevista.
3. Reconfigura el dispositivo desde la plataforma.
4. Verifica que se identifica exactamente como `S60ZBTPF`.
5. Revisa si el firmware ofrece una actualización OTA.

## Datos y privacidad

La declaración del Reglamento europeo de Datos de SONOFF indica que el producto genera:

- Información del dispositivo: firmware, identificador y modelo.
- Estado operativo: estado del indicador y del canal.

Según ese documento, estos datos no se generan continuamente ni en tiempo real y pueden almacenarse localmente y en servidores durante el ciclo de vida del dispositivo. En la aplicación pueden consultarse o modificarse, pero no descargarse; el conjunto de datos del dispositivo puede eliminarse.

El titular declarado es Shenzhen Sonoff Technologies Co., Ltd. y el contacto para acceso, recuperación o borrado es `dpo@sonoff.tech`. El uso de eWeLink u otros servicios crea datos adicionales sujetos a las condiciones del proveedor correspondiente.

Esta descripción se refiere al ecosistema SONOFF/eWeLink. Si el S60ZBTPF se utiliza directamente con Zigbee2MQTT o ZHA, no es necesario registrar el dispositivo en la nube de SONOFF.

## Declaración UE de conformidad

La declaración incluye los modelos **S60ZBTPF** y **S60ZBTPFR2**, con SKU **6920075743005**, y declara conformidad con:

- Directiva de equipos radioeléctricos 2014/53/UE.
- Directiva RoHS 2011/65/UE.
- Directiva RAEE 2012/19/UE.

Normas e informes principales:

| Norma | Informe |
| --- | --- |
| ETSI EN 301 489-1 V2.2.3; ETSI EN 301 489-17 V3.2.4; EN 55032:2015/A11:2020; EN 55035:2017/A11:2020 | LCSA08124135EA |
| ETSI EN 300 328 V2.2.2 | LCSA08124135EB |
| EN 62479:2010; EN 50663:2017 | LCSA08124135EC |
| IEC 62368-1:2018; EN IEC 62368-1:2020+A11:2020 | LCSA12183115S |
| EN IEC 63000:2018 | WTX24X04095342R1C |

La declaración fue emitida en Shenzhen el **28 de noviembre de 2024** y firmada por **Stan Li**, responsable de certificación.

| Entidad | Datos |
| --- | --- |
| Fabricante | Shenzhen Sonoff Technologies Co., Ltd. |
| Dirección | 3F y 6F, edificio A, n.º 663, Bulong Road, Shenzhen, Guangdong, China |
| Representante autorizado en la UE | SONOFF TECHNOLOGY Deutschland GmbH |
| Dirección UE | Breite Str. 22, 40213 Düsseldorf, Alemania |
| Correo de asistencia | support@itead.cc |

El producto es un residuo de aparato eléctrico y electrónico y no debe eliminarse con residuos domésticos sin clasificar. Debe entregarse en un punto autorizado de recogida RAEE.

## Fuentes internas

- [Manual de usuario S60ZBTPF V1.1](User-Manual-S60ZBTPF-EN-V1.1.pdf) — funcionamiento, especificaciones, pasarelas, seguridad, radiofrecuencia, emparejamiento y restablecimiento.
- [Guía rápida S60ZBTPF V1.1](Quick-Guide-S60ZBTPF-V1.1.pdf) — instalación y puesta en marcha.
- [Declaración UE de conformidad S60ZBTPF/S60ZBTPFR2](SONOFF_S60ZBTPF-S60ZBTPFR2_CE_DoC.pdf) — directivas, normas, ensayos, SKU y responsables.
- [Declaración del Reglamento europeo de Datos](SONOFF_S60ZBTPF_Data_Rev.0.pdf) — datos generados, almacenamiento, acceso y contacto del titular.

## Fuentes externas

- [Página comercial oficial del SONOFF iPlug Zigbee S60](https://sonoff.tech/es-es/products/sonoff-iplug-zigbee-smart-plug-s60-series) — características, variantes, ejemplos, especificaciones e integración.
- [Centro de conocimiento oficial S60ZBTPF](https://help.sonoff.tech/docs/s60zbtpf) — funciones, compatibilidad por pasarela, instalación, preguntas frecuentes y solución de problemas; actualizado el 2 de febrero de 2026.
- [SONOFF S60ZBTPF en Zigbee2MQTT](https://www.zigbee2mqtt.io/devices/S60ZBTPF.html) — entidades, OTA, calibración, protección y comandos MQTT; actualizado el 31 de mayo de 2026.
