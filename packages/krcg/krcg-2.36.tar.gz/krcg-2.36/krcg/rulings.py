"""Rulings parsing.
"""
from typing import Generator, Tuple
import pkg_resources
import re
import warnings
import yaml


class Ruling:
    """Simple class representing a ruling."""

    def __init__(self):
        self.cards = []
        self.text = ""
        self.links = {}


class RulingReader:
    """Reader to load KRCG YAML rulings files."""

    def __init__(self):
        self.links = yaml.safe_load(
            pkg_resources.resource_string("rulings", "rulings-links.yaml")
        )

    def __iter__(self):
        """Yield Ruling instances"""
        for card, rulings in yaml.safe_load(
            pkg_resources.resource_string("rulings", "cards-rulings.yaml")
        ).items():
            for ruling in rulings:
                ret = Ruling()
                ret.cards = [_card_id_name(card)]
                ret.text = ruling
                if not ret.text or not isinstance(ret.text, str):
                    warnings.warn(f"absent or misformed text in '{card}' ruling")
                try:
                    ret.links = dict(self._get_link(ret.text))
                except KeyError:
                    warnings.warn(f"Ruling: link not found for `{card}`")
                    raise
                yield ret
        for ruling in yaml.safe_load(
            pkg_resources.resource_string("rulings", "general-rulings.yaml")
        ):
            ret = Ruling()
            ret.cards = [_card_id_name(card) for card in ruling["cards"]]
            ret.text = ruling["ruling"]
            if not ret.text or not isinstance(ret.text, str):
                warnings.warn(
                    f"absent or misformed text in general ruling for {ret.cards}"
                )
            try:
                ret.links = dict(self._get_link(ret.text))
            except KeyError:
                warnings.warn(f"Ruling: link not found for general ruling `{ret.text}`")
                raise
            yield ret

    def _get_link(self, text: str) -> Generator:
        """Yield (reference, link) tuples from rulink text."""
        references = re.findall(r"\[[a-zA-Z]+\s[0-9-]+\]", text)
        if not references:
            warnings.warn(f"no reference in ruling: {text}")
        for reference in references:
            yield reference, self.links[reference[1:-1]]


def _card_id_name(text: str) -> Tuple[int, str]:
    """Decode (id, name) from YAML "id|name" format."""
    card_id, card_name = text.split("|")
    card_id = int(card_id)
    return card_id, card_name
