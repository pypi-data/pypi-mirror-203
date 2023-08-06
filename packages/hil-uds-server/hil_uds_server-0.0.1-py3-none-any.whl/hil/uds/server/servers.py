'''
Copyright (c) 2023 by HIL Group
Author: notmmao@gmail.com
Date: 2023-04-16 10:46:39
LastEditors: notmmao@gmail.com
LastEditTime: 2023-04-16 15:32:48
Description: 

==========  =============  ================
When        Who            What and why
==========  =============  ================

==========  =============  ================
'''
import os 
from hil.core import Cantp, UdsServer
from hil.bus import load_bus
from hil.common import utils
from fastapi import FastAPI, APIRouter
from can.interface import Bus
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from .models import Ecu


class ConfigurableUdsServer(UdsServer):
    ecu: Ecu
    bus: Bus
    tp: Cantp
    config_file: str

    def __init__(self):
        '''
        Args:
            config_file (str): 配置文件路径
        '''
        super(ConfigurableUdsServer, self).__init__(None)

    def set_config_file(self, config_file: str):
        self.config_file = config_file
        self.reload()

    def reload(self):
        '''重新加载配置文件'''
        self.ecu = ecu = Ecu.parse_file(self.config_file)
        self.bus = bus = load_bus(ecu.channel)
        self.tp = Cantp(bus, ecu.rxid, ecu.txid)

    def service_default_handle(self, req_bytes: bytearray) -> bytearray:
        '''
        根据请求报文，返回响应报文

        Args:
            req_bytes (bytearray): 请求报文

        Returns:
            bytearray: 响应报文
        '''
        req = req_bytes.hex().upper()
        sid = req_bytes[0]
        print(f"req: {req}")
        if req in self.ecu.echo:
            resp = self.ecu.echo[req]
            if isinstance(resp, list):
                resp_bytes = bytearray(resp)
            else:
                req_bytes[0] = sid + 0x40
                resp_bytes = bytearray(req_bytes)
                resp_bytes.extend(resp.encode())
        else:
            # NRC 0x11
            resp_bytes = bytearray([0x7F, sid, 0x11])

        print(f"resp: {resp_bytes.hex()}")
        return resp_bytes


class AutoReloadUdsServer(ConfigurableUdsServer, FileSystemEventHandler):
    observer = Observer()

    def __init__(self):
        super().__init__()

    def start(self):
        path = os.path.dirname(os.path.abspath(self.config_file))
        self.observer.schedule(self, path=path, recursive=False)
        self.observer.start()
        super().start()

    def stop(self) -> None:
        self.observer.stop()
        return super().stop()


    @utils.debounce(1)
    def on_modified(self, event: FileSystemEvent):
        if event.src_path.endswith(self.config_file):
            print("on_modified")
            self.reload()


class RestfulUdsServer(AutoReloadUdsServer):
    app: FastAPI
    router: APIRouter

    def __init__(self):
        super(RestfulUdsServer, self).__init__()
        self.app = FastAPI()
        self.router = APIRouter()
        self.app.add_event_handler("startup", self.start)
        self.app.add_event_handler("shutdown", self.stop)
        self.router.add_api_route("/ecu", self.get_ecu, methods=["GET"])
        self.router.add_api_route("/ecu", self.set_ecu, methods=["POST"])
        self.router.add_api_route(
            "/ecu/did/{code}", self.get_ecu_did, methods=["GET"])
        self.router.add_api_route(
            "/ecu/did/{code}", self.set_ecu_did, methods=["POST"])
        self.router.add_api_route(
            "/ecu/echo/{code}", self.get_ecu_echo, methods=["GET"])
        self.router.add_api_route(
            "/ecu/echo/{code}", self.set_ecu_echo, methods=["POST"])
        self.app.include_router(self.router)

    def get_ecu(self):
        return self.ecu

    def set_ecu(self, ecu: Ecu):
        self.ecu = ecu
        return self.ecu

    def set_ecu_did(self, code: str, value: str):
        self.ecu.dids[code] = value
        return self.ecu

    def get_ecu_did(self, code: str):
        return self.ecu.dids[code]

    def get_ecu_echo(self, code: str):
        return self.ecu.echo[code]

    def set_ecu_echo(self, code: str, value: str):
        self.ecu.echo[code] = value
        return self.ecu
