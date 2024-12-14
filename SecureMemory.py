from m5.objects.ClockedObject import ClockedObject
from m5.params import *


class SecureMemory(ClockedObject):
    type = "SecureMemory"
    cxx_header = "bootcamp/secureMemory/SecureMemory.hh"
    cxx_class = "gem5::SecureMemory"

    cpu_side_port = ResponsePort(
        "ResponsePort para recibir pedidos del lado del cpu"
    )
    mem_side_port = RequestPort(
        "RequestPort para enviar pedidos del lado de la memoria"
    )

    metadata_cache_response_port = RequestPort(
        "Response side port, receives responses from the metadata cache"
    )

    inspection_buffer_entries = Param.Int(
        "Capacidad del buffer de Inspecciones"
    )

    response_buffer_entries = Param.Int("Capacidad del buffer de respuesta")
    latency = Param.Int("Latencia del modulo")
