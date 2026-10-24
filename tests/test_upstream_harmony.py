"""Answer development must preserve the harmony of the pinned upstream composer."""

from dataclasses import asdict
import hashlib
import json
from pathlib import Path

import pytest

from gentle_stream import genres
from gentle_stream.composer import Composer
from gentle_stream.style import Style


# Generated from the unmodified upstream source recorded in the fixture.
# Covers three form cycles, every genre, all modes in lo-fi, and two seeds.
REFERENCE = json.loads((Path(__file__).parent / "fixtures" / "upstream_harmony.json").read_text())


@pytest.mark.parametrize("case", REFERENCE["cases"],
                         ids=lambda case: f"{case['genre']}-{case['mode']}-{case['seed']}")
def test_answer_development_preserves_upstream_harmony_and_bass(case):
    style = Style(genre=case["genre"], mode=case["mode"])
    composer = Composer(style, case["seed"], REFERENCE["tonic_midi"], genres.get(style.genre).chord)
    harmony = []
    for bar in range(REFERENCE["bars"]):
        plan = asdict(composer.plan(bar))
        harmony.append({key: plan[key] for key in
                        ("section", "section_bar", "energy", "chord", "passing", "key_offset", "bass")})
    actual = hashlib.sha256(json.dumps(harmony, sort_keys=True).encode()).hexdigest()
    assert actual == case["sha256"]
