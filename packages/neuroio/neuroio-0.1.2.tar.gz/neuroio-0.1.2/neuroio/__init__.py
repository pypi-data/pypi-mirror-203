"""**neuroio-python**

A Python package for interacting with the NeuroIO API
"""
from .clients import AsyncClient, Client
from .listeners import EventListener

__version__: str = "0.1.2"

__all__ = ["__version__", "Client", "AsyncClient", "EventListener"]
