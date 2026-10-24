# Herdr Music dependency fork

This fork is based on Gentleman-Programming/gentle-stream revision
`381290451544ad2ca3348a68a81b3056bdac73b7`.

It defers public `scipy.signal` imports in `synth.py`, `mastering.py`, and
`genres/dubstep.py` until audio processing functions run. Opening the remote
player interface therefore does not initialize the SciPy signal backend.
That import change does not alter the synthesis functions or their arguments.

`Spectrum.COLORS` also allows a caller to set the spectrum palette per widget
instance. The original palette remains the default and other instances are
not affected. This lets Herdr Music provide its own theme without copying
the animation or modifying module globals.

`client.read_state()` reads one authenticated JSON snapshot without starting
audio or loading NumPy, SciPy, or the interface. The full player client loads
its numerical dependencies only when it is instantiated. Both paths share
the original connection and authentication handling.

The shared composer now develops contrasting answers while retaining the motif
head and harmonic cadences. New rhythms reach active melody bars even at sparse
densities. This behavior applies to every registered genre.

`Style.lead_register` selects `low`, `mid`, or `high`, independently of genre.
The default is `low`; `mid` preserves the original melody range, and `high` is
one octave above it. The schema, validator, saved styles and model prompt carry
the setting. The counter-melody follows the same range, preserving its relation
to the lead. Existing presets without the field use the new low default.

The existing master low-pass now also follows a shared brightness ceiling from
1 kHz to 18 kHz. A genre can retain a darker native tone; setting brightness to
one retains its original full-brightness cutoff at the standard sample rate.
This adds no filter, worker or model call. Genre voices, rhythm scheduling and
master-character settings remain separate.

Tests exercise the register, active phrase development and rendered tone
response across all ten genres. These are measured improvements to the
procedural engine, not a claim to match a professionally produced recording.

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
