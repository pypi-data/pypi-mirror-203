from enum import Enum
import os
from os import path
from typing import Dict, Optional
from pydantic import Field

from .mytypes import NestingModel


class RpctaskConfig(NestingModel):
    """Configuration for `rpctask`"""
    correct_tolerance: float = 0.03
    """Acceptable margin for green color"""
    warning_tolerance: float = 0.05
    """Acceptable margin for yellow color"""


class PfdConfig(NestingModel):
    """configuration for `pfd`"""
    ias_never_exceed: float = 167.0
    """Never exceed speed (Vne) shown on IAS tape"""
    show_adi_target: bool = True
    """Display the attitude target after receiving trgt.att"""
    adi_target_roll: bool = True
    """Rotate attitude target indicator to show desired roll"""
    adi_target_yaw: bool = False
    """Move attitude target indicator to show desired yaw"""
    show_flightpath: bool = True
    """Show flightpath vector (FPV) indicator on ADI"""
    show_retrograde: bool = False
    """Show reverse flight path vector on ADI"""
    move_roll_ticks: bool = False
    """Move roll angle scale with horizon, keeping sideslip triangle in place"""
    sideslip_max: float = 15.0
    """Maximal displayed sideslip angle, in degrees"""


class ApproachConfig(NestingModel):
    """Ship approach configuration"""
    nominal_alt: float = 3
    """Altitude at which the scale is 1, in meters"""
    camera_height: float = 10
    """Position of camera above aircraft origin, in meters

    Larger values of this make the scale change less drastically at low altitude"""


class InstrumentsConfig(NestingModel):
    """Configuration for instruments visualisation, units etc."""
    speed_multiplier: float = 3600.0 / 1852.0
    """Scaling factor to change state velocity in meters per second to displayed IAS and GS, default for knots"""
    altitude_multiplier: float = 1 / 0.3048
    """Scaling factor to change state altitude in meters to displayed altitude, default for feet"""
    radio_altimeter_activation: float = 2500.0 * 0.3048
    """Activation height of radio altimeter above which it is not modeled, default 2500ft"""


class CASCategory(Enum):
    """Category (severity, type) of a message shown in CAS"""
    WARNING = 1
    """Red, blinking until acknowledged"""
    CAUTION = 2
    """Amber, blinking until acknowledged"""
    ADVISORY = 3
    """Green, blinking for a fixed time"""
    STATUS = 4
    """White messages"""


class CASEvent(NestingModel):
    """Event that can be displayed in CAS"""
    category: CASCategory
    """Category to put the message into"""
    text: str
    """Text to be shown"""


class CASConfig(NestingModel):
    """Configuration for Crew Alerting System, including events"""
    events: Dict[int, CASEvent] = {}
    """Dictionary of events by their integer id"""


class Config(NestingModel):
    """Root of configuration structure

    Every config field in this and children should be provided with defaults,
    that can be overriden by config files"""

    json_schema_url: Optional[str] = Field(alias='$schema', default=None)
    """Allow the `$schema` property for specifying JSON Schema URL"""
    rpctask = RpctaskConfig()
    pfd = PfdConfig()
    approach = ApproachConfig()
    instruments = InstrumentsConfig()
    cas = CASConfig()
    start_time: Optional[float] = None
    """Epoch time in seconds of starting the program (see `time.time()`)"""


def schema_location():
    root_path = path.abspath(path.dirname(__file__))
    data_path = path.join(root_path, 'data')
    os.makedirs(data_path, exist_ok=True)
    return path.join(data_path, 'lidia-config.json')


def write_schema():
    with open(schema_location(), 'w') as out:
        out.write(Config.schema_json(by_alias=True))
