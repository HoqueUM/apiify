###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import baml_py
from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import Dict, Generic, List, Optional, TypeVar, Union, Literal

from . import types
from .types import Checked, Check

###############################################################################
#
#  These types are used for streaming, for when an instance of a type
#  is still being built up and any of its fields is not yet fully available.
#
###############################################################################

T = TypeVar('T')
class StreamState(BaseModel, Generic[T]):
    value: T
    state: Literal["Pending", "Incomplete", "Complete"]


class Article(BaseModel):
    title: Optional[str] = None
    date: Optional[str] = None
    author: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None

class Atrribute(BaseModel):
    attribute: Optional[str] = None
    value: Optional[str] = None

class Metadata(BaseModel):
    part: Optional[str] = None
    tag: Optional[str] = None
    content: Optional[str] = None
    attributes: List["Atrribute"]

class PageData(BaseModel):
    model_config = ConfigDict(extra='allow')

class Resume(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    experience: List[Optional[str]]
    skills: List[Optional[str]]
