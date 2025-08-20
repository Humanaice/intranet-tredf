from tredf.intranet import logger
from tredf.intranet.content.area import Area
from zope.lifecycleevent import ObjectAddedEvent


def _update_excluded_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    description = obj.description
    # Se Tiver uma descrição, o campo exclude_from_nav será False
    obj.exclude_from_nav = not bool(description)
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    # Update the exclude_from_nav field based on the description
    _update_excluded_from_nav(obj)
