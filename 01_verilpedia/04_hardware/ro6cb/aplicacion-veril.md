# Aplicación del equipo RO6CB en Veril

## Estado documental

El usuario ha comunicado que ha adquirido la variante RO6CB con bomba de refuerzo para el sistema RO/DI de Veril. En esta ficha se documenta el equipo RO anunciado; la recepción física, el inventario del paquete y la instalación todavía deben registrarse.

Los componentes comunicados del sistema DI y sus accesorios se documentan por separado en la [ficha del sistema DI](../di-ro/sistema-di.md). La resina, el montaje final y la aceptación mediante mediciones siguen pendientes. Esta ficha no afirma que el conjunto RO/DI esté completo ni operativo.

## Uso previsto

La aplicación prevista es producir agua de permeado mediante el equipo RO6CB con bomba y dividirla en dos ramas. La rama RO conservará el recorrido doméstico para agua de consumo; la rama DI tomará el permeado antes del postfiltro de carbón y del filtro remineralizador y lo conducirá a las dos carcasas T33. El agua destinada a Veril no atravesará el remineralizador.

El filtro remineralizador no se utilizará para el agua que vaya a entrar en la etapa DI. Añadir minerales antes de la desionización reduce la coherencia del proceso y puede consumir innecesariamente la resina. El agua que llegue al acuario o al depósito del ATO no llevará sal añadida.

## Esquema funcional previsto

```text
Red de agua fría → Manómetro → RO6CB con bomba → Membrana RO
                                               ├── Rechazo → Desagüe
                                               └── Permeado → Derivación con llaves
                                                            ├── Ruta RO → Depósito/postfiltro/remineralizador
                                                            │              → Grifo de cocina
                                                            └── Ruta DI → Llave DI → TDS 1 → T33 1 → TDS 2
                                                                         → T33 2 → TDS 3
                                                                         → Llave y tubo de llenado
                                                                         → Cubo GRAF del ATO o recipiente limpio
```

La ruta real de tuberías, el punto de toma del permeado, el almacenamiento y el rechazo se confirmarán con la unidad abierta. El lavado o purga propio del RO6CB se mantendrá conforme a su manual. No se añadirá una segunda purga independiente. El diseño no utilizará el postfiltro remineralizador ni el depósito doméstico como fuente de agua para Veril sin comprobar antes su recorrido hidráulico.

## Compatibilidad por comprobar

- Presión real de la toma de entrada
- Disponibilidad de una toma eléctrica segura para la bomba y su transformador
- Punto de conexión a agua fría
- Conexión al desagüe y espacio para el rechazo
- Ubicación estable, accesible y protegida frente a fugas
- Longitud, diámetro y estado de las tuberías incluidas
- Capacidad y presión del depósito suministrado
- Identificación de los presostatos, el solenoide, el restrictor y la bomba
- Acceso para cambiar los tres prefiltros, la membrana y los postfiltros
- Posibilidad de derivar el permeado antes de la remineralización

El montaje no se considerará aceptado por el mero hecho de que la bomba arranque o el depósito se llene. Será necesario comprobar fugas, rechazo, caudal de permeado, presión, parada automática y calidad del agua en cada punto relevante.

## Criterios de aceptación de la aplicación

- El equipo queda identificado como RO6CB o como la variante exacta que figure en su etiqueta
- La presión de entrada está dentro del límite de la variante con bomba
- No existen fugas en conexiones, vasos, membrana, depósito ni desagüe
- La bomba y los sistemas de presostato paran cuando corresponde
- El rechazo llega al desagüe sin retorno ni desbordamiento
- El permeado se puede tomar antes del postfiltro remineralizador
- El agua de salida del RO se mide y se registra antes de conectarla al sistema DI
- El sistema DI posterior se instala sin introducir la salida remineralizada
- Se conserva un punto de corte accesible para aislar el equipo
- El equipo queda protegido frente a derrames y se puede inspeccionar durante el funcionamiento

## Pendientes

- [ ] Recibir y desembalar el equipo
- [ ] Inventariar físicamente todos los componentes y sus referencias
- [ ] Fotografiar la etiqueta del equipo, la bomba, el transformador y los cartuchos
- [ ] Medir la presión de entrada en el punto de instalación
- [ ] Definir y montar la conexión de entrada, rechazo y permeado
- [ ] Confirmar el punto de derivación anterior al remineralizador
- [ ] Separar la rama RO de consumo y la rama DI mediante llaves independientes
- [ ] Colocar la llave de aislamiento de la rama DI antes de TDS 1
- [ ] Confirmar el funcionamiento del lavado o purga propio del RO6CB
- [ ] Instalar la llave y el tramo de tubo para llenar el cubo GRAF del ATO
- [ ] Registrar el primer enjuague y los vaciados completos
- [ ] Medir TDS o conductividad en la entrada, el permeado y, posteriormente, la salida RO/DI
- [ ] Instalar las dos carcasas T33 con resina mixta en serie
- [ ] Registrar la operación de instalación y sus resultados

## Relación con la configuración

El agua RO/DI se utilizará para la reposición por evaporación y para preparar agua salada en los cambios posteriores. La configuración concreta del ATO y su depósito se documenta en el [D-D H2Ocean Compact ATO](../dd-h2ocean-compact-ato/dd-h2ocean-compact-ato.md) y en el [barril GRAF de 15 l](../dd-h2ocean-compact-ato/graf-barril-agroalimentario-15l.md).

La compra del equipo RO6CB no acredita todavía que Veril disponga de agua RO/DI utilizable. Esa condición quedará cubierta cuando se complete el sistema DI, se instale el conjunto y se acepten sus mediciones.

## Fuentes

- [Ficha del equipo RO6CB](ro6cb.md)
- [Configuración química de Veril](../../../02_configuracion/01_dimensiones/05_quimica.md)
- [Procedimiento de cambios de agua](../../../03_pendientes/operacion-recurrente/cambios-agua.md)
