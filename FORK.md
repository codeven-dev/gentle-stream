# Herdr Music dependency fork

This fork is based on Gentleman-Programming/gentle-stream revision
`381290451544ad2ca3348a68a81b3056bdac73b7`.

It defers public `scipy.signal` imports in `synth.py`, `mastering.py`, and
`genres/dubstep.py` until audio processing functions run. Opening the remote
player interface therefore does not initialize the SciPy signal backend.
The synthesis functions and their arguments remain unchanged.

`Spectrum.COLORS` also allows a caller to set the spectrum palette per widget
instance. The original palette remains the default and other instances are
not affected. This lets Herdr Music provide its own theme without copying
the animation or modifying module globals.

`client.read_state()` reads one authenticated JSON snapshot without starting
audio or loading NumPy, SciPy, or the interface. The full player client loads
its numerical dependencies only when it is instantiated. Both paths share
the original connection and authentication handling.

`tests/test_startup.py` verifies interface imports and style validation in a
fresh process. Run the full test suite with warnings treated as errors:

```sh
uv sync --frozen
uv run pytest -q -W error
```

Herdr Music pins a commit from this fork. Do not edit installed files in
`.venv`. Future upstream updates should retain the startup regression test,
run the full suite, and repeat the Herdr integration checks before changing
the pinned revision.

The original project, attribution, and MIT license are retained. No changes
are published to the upstream repository by this fork.
