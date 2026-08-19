# Sicce Shark SKIMMER 300

- **Fabricante:** Sicce
- **Modelo:** Shark SKIMMER 300
- **Código:** `SHSKM300E`
- **Tipo:** skimmer interno para acuario marino

## Ficha normalizada

| Campo | Valor |
| --- | --- |
| `hardware_id` | `Sicce_Shark_Skimmer_300` |
| `category` | `aquarium` |
| `vendor` | `Sicce` |
| `model` | `Shark SKIMMER 300` |
| `hardware_kind` | `physical` |
| `physical_type` | `protein_skimmer` |
| `rated_power` | 5 W |
| `air_flow` | hasta 180 L/h |
| `mounting` | soporte magnético para cristal de hasta 15 mm |
| `environment` | acuario marino |
| `connectivity` | ninguna |
| `software` | no aplicable |

## Especificaciones

| Parámetro | Valor declarado |
| --- | --- |
| Potencia | 5 W |
| Longitud de cable | 2,2 m |
| Dimensiones | 83 × 125 × 243 mm |
| Aire máximo | 180 L/h |
| Cristal máximo | 15 mm |
| Profundidad de inmersión | 130–150 mm |
| Volumen de copa | 260 ml |
| Bomba/impulsor | conjunto interno específico del skimmer |
| Entrada de agua | regulable |
| Funcionamiento | espumación a contracorriente |
| Compatibilidad con ozono | sí, según fabricante |
| Accesorio | cepillo de limpieza incluido |

## Capacidad orientativa

La documentación comercial diferencia la capacidad según la carga:

| Tipo de sistema | Volumen máximo declarado |
| --- | ---: |
| Carga biológica baja | 300 L |
| Carga biológica media | 200 L |
| Carga biológica alta | 100 L |

Estas cifras proceden de la tabla técnica del manual. Son orientativas: el rendimiento depende de carga orgánica, nivel de agua, salinidad, ajuste de aire y mantenimiento.

## Construcción

- Diseño interno compacto
- Cuerpo opaco para limitar el crecimiento de algas en el interior
- Soporte magnético resistente al agua
- Copa desmontable
- Entrada de agua regulable
- Impulsor autolimpiante optimizado para espumación

## Software y conectividad

No incorpora firmware, aplicación ni conexión de red. Su funcionamiento es electromecánico. Un enchufe externo permite conmutar alimentación, pero no mide nivel, aire, caudal ni llenado de copa.

La integración prevista del enchufe con Home Assistant y Zigbee2MQTT está documentada en [Integración del Sicce Shark SKIMMER 300](home-assistant-zigbee2mqtt.md).

## Instalación

1. Instálalo verticalmente en un nivel de agua estable
2. Mantén libre la toma de aire y accesible la copa
3. Ajusta progresivamente entrada y aire durante el rodaje
4. Deja espacio para extraer y desmontar el cuerpo
5. Evita que el cable forme un camino de agua hacia la toma eléctrica
6. Desconecta la alimentación antes de introducir las manos
7. No lo instales junto a una bomba de circulación que altere su flujo interno

### Funcionamiento temporal sin copa

La copa es desmontable y el motor puede producir circulación y aireación sin ella, pero el Shark SKIMMER 300 no tiene un modo de funcionamiento sin recogida documentado por Sicce. El manual describe la copa como el destino de la espuma concentrada y de los contaminantes; el fabricante también la identifica como una pieza específica de «cup & cover».

Por tanto, puede utilizarse sin copa únicamente como medida temporal de intercambio gaseoso durante el ciclado, con el rebose dirigido al sump y vigilancia de salpicaduras, espuma, nivel y acumulación de sal. En ese estado no se debe considerar que el equipo esté retirando materia orgánica de forma controlada. No se dejará funcionando sin copa sin supervisión ni se utilizará así como instalación normal de maduración.

La prioridad será mantener retorno y agitación superficial suficientes. Si el funcionamiento sin copa produce espuma inestable, salpicaduras, microburbujas persistentes o cambios de nivel, se detendrá y se utilizará otra forma de aireación.

Tras aditivos, acondicionadores, adhesivos o cambios de salinidad puede producir espuma inestable o desbordamiento.

Debe alimentarse mediante una instalación protegida por diferencial de 30 mA como máximo. Solo puede trabajar sumergido, con líquidos de hasta 35 °C. El cable es de tipo Z: si se daña, el manual ordena sustituir la bomba completa, no reparar el cable.

## Mantenimiento

- Vacía y limpia la copa con frecuencia
- Limpia la toma de aire, Venturi, rotor y cámara
- Elimina depósitos calcáreos siguiendo el manual
- Revisa tubos, juntas y cable
- No utilices el cable para levantar el equipo

## Fuente interna

- [Manual oficial Shark SKIMMER 150/300](./sicce-shark-skimmer-manual.pdf)

## Fuente externa

- [Sicce: Shark SKIMMER](https://www.sicce.com/es/products/protein-skimmer-pumps/shark-skimmer.html)

## Fecha de revisión

Ficha verificada el **27 de julio de 2026**.
