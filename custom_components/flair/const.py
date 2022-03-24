"""My platform constants"""
from homeassistant.const import Platform


DOMAIN = "flair"

PLATFORMS = [
    Platform.CLIMATE,
    Platform.COVER,
    Platform.SENSOR,
    Platform.SELECT,
]

STRUCTURE_MODES = [
    "Heat",
    "Cool",
    "Auto",
    "Off",
]

SYSTEM_MODES = [
    "Auto",
    "Manual",
]
HOME_AWAY_MODE = [
    "Home",
    "Away",
]

ROOM_MODES = [
    "Active",
    "Inactive"
]

VENT_CLOSED = 0
VENT_HALF_OPEN = 50
VENT_OPEN = 100
