# flake8: noqa
def make_title(text: str = "Sample Plugin"):
    return text.title()


def setup(registry):
    registry.entry("title", make_title)
