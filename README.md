# Simulador de Créditos Educativos

## Descripción

Este programa permite a los estudiantes conocer con claridad su compromiso financiero y planificar sus pagos de manera adecuada. La simulación calcula la cantidad que el estudiante debe pagar mientras estudia y el monto que debe cancelar después de finalizar su periodo de estudios. La información para la realización de este programa fue extraida directamente de la página del [ICETEX](https://web.icetex.gov.co/es/creditos/tu-eliges).

## Entradas

El programa recibe los siguientes datos de entrada:

- **Tipo de crédito**: Puede ser:
  - "Mediano Plazo - 30%"
  - "Mediano Plazo - 60%"
  - "Corto Plazo - 100%"
- **Valor total de la carrera**: Costo total de los estudios en pesos colombianos.
- **Duración en años**: Tiempo estimado de duración del programa de estudios.

## Proceso

El programa sigue estos pasos:

1. Se selecciona el tipo de crédito.
2. Se aplican las reglas según el tipo de crédito elegido:

   - **Mediano Plazo - 30%**:
     - El estudiante paga el 30% del costo total mientras estudia.
     - Al finalizar, debe pagar el 70% restante en un tiempo equivalente a **1.5 veces** la duración de la carrera.
     - IPC + 9% que equivale al 1,15% mes vencido (14,67% efectivo anual). La tasa efectiva anual del 14,67% es equivalente al 13,77% Nominal Anual Mes Vencido. 

   - **Mediano Plazo - 60%**:
     - El estudiante paga el 60% mientras estudia.
     - Al finalizar, debe pagar el 40% restante en un tiempo equivalente a **1.5 veces** la duración de la carrera.
     - IPC + 7%, que equivale al 0,99%mes vencido (12,56% efectivo anual). La tasa efectiva anual del 12,56% es equivalente al 11,89% Nominal Anual Mes Vencido. 

   - **Corto Plazo - 100%**:
     - El estudiante paga el **100%** del costo total durante el periodo de estudio.
     - IPC + 7%, que equivale al 0,99%mes vencido (12,56% efectivo anual). La tasa efectiva anual del 12,56% es equivalente al 11,89% Nominal Anual Mes Vencido. 

3. Se calculan los montos a pagar en cada etapa según la selección del usuario.

## Salidas

El programa genera los siguientes resultados:

- **Pago durante el periodo de estudios**: Cantidad total a pagar mientras el estudiante cursa la carrera.
- **Pago posterior al periodo de estudios**: Monto total restante a pagar después de finalizar los estudios.

## Ejemplo de Uso

Si un estudiante selecciona el crédito **"Mediano Plazo - 30%"** para una carrera de **5 años** con un costo de **50,000,000 COP**:

- **Pago durante los estudios**:  
  *30% de 50,000,000 = 15,000,000 COP + intereses*
- **Pago después de los estudios**:  
  *70% de 50,000,000 = 35,000,000 COP + intereres*
- **Tiempo para pagar el saldo restante**:  
  *5 años * 1.5 = 7.5 años*

Este programa permite a los estudiantes conocer con claridad su compromiso financiero y planificar sus pagos de manera adecuada.
