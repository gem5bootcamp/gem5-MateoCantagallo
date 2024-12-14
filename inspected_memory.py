from typing import (
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from m5.objects import (
    AddrRange,
    DRAMInterface,
    Port,
    SecureMemory,
    L1Cache,
    L2XBar,
)

from gem5.components.boards.abstract_board import AbstractBoard
from gem5.components.memory.memory import ChanneledMemory
from gem5.utils.override import overrides


class InspectedMemory(ChanneledMemory):
    def __init__(
        self,
        dram_interface_class: Type[DRAMInterface],
        num_channels: Union[int, str],
        interleaving_size: Union[int, str],
        size: Optional[str] = None,
        addr_mapping: Optional[str] = None,
        inspection_buffer_entries: int = 16,
        response_buffer_entries: int = 32,
    ) -> None:
        super().__init__(
            dram_interface_class,
            num_channels,
            interleaving_size,
            size=size,
            addr_mapping=addr_mapping,
        )
        self.metadata_caches = [L1Cache() for _ in range(num_channels)]
        self.inspectors = [
            SecureMemory(
                inspection_buffer_entries=inspection_buffer_entries,
                response_buffer_entries=response_buffer_entries,
                latency=2,
            )
            for _ in range(num_channels)
        ]
        self.xbar = L2XBar()

    @overrides(ChanneledMemory)
    def incorporate_memory(self, board: AbstractBoard) -> None:
        super().incorporate_memory(board)
        for inspector, ctrl, cache in zip(self.inspectors, self.mem_ctrl, self.metadata_caches):
            inspector.mem_side_port = self.xbar.cpu_side_ports
            inspector.metadata_cache_response_port = cache.cpu_side_port
            cache.mem_side_port = self.xbar.cpu_side_ports
            ctrl.port = self.xbar.mem_side_ports

    @overrides(ChanneledMemory)
    def get_mem_ports(self) -> Sequence[Tuple[AddrRange, Port]]:
        return [
            (ctrl.dram.range, inspector.cpu_side_port)
            for ctrl, inspector in zip(self.mem_ctrl, self.inspectors)
        ]
