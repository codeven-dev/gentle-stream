"""Opening the remote player's interface must not initialize the DSP backend."""

import os
from pathlib import Path
import subprocess
import sys


def test_remote_player_interface_and_style_validation_do_not_load_scipy():
    source = Path(__file__).resolve().parents[1] / "src"
    result = subprocess.run(
        [sys.executable, "-c", """
import sys
from gentle_stream.app import StreamApp
from gentle_stream.client import PlayerClient
from gentle_stream.bridge import genre_lines
from gentle_stream.style import Style

style = Style.from_dict({'genre': 'dubstep', 'bpm': 95})
assert style.genre == 'dubstep' and style.bpm == 95
assert 'dubstep' in genre_lines()
assert 'scipy.signal' not in sys.modules, 'The remote interface initialized the DSP backend'
"""],
        env=os.environ | {"PYTHONPATH": str(source)},
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stderr
