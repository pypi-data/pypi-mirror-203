from datetime import datetime
from email import utils
import typing

from jinja2 import (
    ChoiceLoader,
    Environment,
    FileSystemLoader,
    PackageLoader,
    pass_environment,
    select_autoescape,
)

render_engine_templates_loader = ChoiceLoader(
    [
        FileSystemLoader("templates"),
        PackageLoader("render_engine", "render_engine_templates"),
    ]
)


def to_pub_date(value: datetime):
    """
    Parse information from the given class object.
    """
    return utils.format_datetime(value)

@pass_environment
def format_datetime(env: Environment, value: str) -> datetime:
    """
    Parse information from the given class object.
    """
    return datetime.strftime(value, env.globals.get("DATETIME_FORMAT", "%d %b %Y %H:%M %Z"))


def url_for(value: str, site):
    if value in site.route_list:
        return site.route_list[value].url_for
    else:
        raise ValueError(f"{value} is not a valid route.")


engine = Environment(
    loader=render_engine_templates_loader,
    autoescape=select_autoescape(["xml"]),
    lstrip_blocks=True,
    trim_blocks=True,
)

engine.filters["to_pub_date"] = to_pub_date
engine.filters["format_datetime"] = format_datetime
