from pkg_resources import resource_filename


def chord_svg() -> None:
    return resource_filename(__name__, 'chord.jinja2')


def strum_svg() -> None:
    return resource_filename(__name__, 'strum.jinja2')
