# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import datetime
import os
import pickle
import re
import signal
import threading

from ._base import _BaseIndicator, CheckMenuItemConfig, _ExternalBoolState, _StaticState
from ..shared import SocketMessage
from ..shared.ipc import NullClient, IClientIPC


class IndicatorManager(_BaseIndicator):
    def __init__(self, indic_name_to_phs_map: dict[str, threading.Event]):
        self.indic_name_to_phs_map = indic_name_to_phs_map
        super().__init__(
            "datetime",
            icon_name_default="es7s.png",
            label="es7s/indicators",
        )
        self._monitor_data_buf.append(
            pickle.dumps(
                SocketMessage(data=None, timestamp=2147483647),
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        )
        self._render_result("", icon=self._icon_name_default)

    def _make_socket_client(self, socket_topic: str, indicator_name: str) -> IClientIPC:
        return NullClient()

    def _restart(self, _):
        # should be run as a service and thus
        # expected to be restarted by systemd,
        # so simply perform a suicide:
        os.kill(os.getpid(), signal.SIGTERM)

    def _init_state(self):
        super()._init_state()
        self._state_map.update({
            CheckMenuItemConfig("Restart (shutdown)"): _StaticState(callback=self._restart)
        })
        self._state_map.update(
            {
                CheckMenuItemConfig(
                    re.sub("(?i)[^\w\s/]+", "", label).strip(),
                    separator_before=idx == 0,
                ): _ExternalBoolState(
                    callback=self._toggle_indic,
                    ext=phs,
                )
                for idx, (label, phs) in enumerate(self.indic_name_to_phs_map.items())
            }
        )

    def _toggle_indic(self, _, phs: threading.Event):
        if phs.is_set():
            phs.clear()
        else:
            phs.set()

    def _render(self, msg: SocketMessage[None]):
        self._render_result(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] #{self._state.tick_render_num}")
