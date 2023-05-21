# actividad4
# Jorge Omar López Gemigninai A01769675
# Fernando Reséndiz Bautista A01769659
# Carlos Eduardo Jiménez Santiago A01769960

#  El siguiente código simula el comportamiento de la comunicación entre servidor-cliente con el uso de sockets para el envío y recepción de información. 
# La entrada recibida desde la terminal es de tipo parser, con banderas para que se reciba --walltime, --mempeak, --cpu, --task(el código postal a procesar), todas las banderas son necesarias.
# Asimismo el servidor recibe todas las peticiones durante un minuto completo y las ordena dependiendo a la cantidad de recursos que requiere cada una de las peticiones hechas, dandole prioridad a las que menos
# recursos necesitan
# En caso de que se ingrese un código postal que no se encuentre en el csv el programa lanza el mensaje indicando que ese código postal no se encuentra en el csv y los que sí, los procesa danto respuesta.
# Un ejemplo de entrada sería la siguiente considerando que se debe --walltime 3600 --mempeak 12gb --cpu 12 --task "ZipCode: 35801".
