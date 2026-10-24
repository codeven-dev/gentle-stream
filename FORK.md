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
densities. Answer development uses a separate deterministic random generator,
so the additional variations preserve the upstream harmonic choices, section
energy and bass plans. This behavior applies to every registered genre.

`Style.lead_register` selects `low`, `mid`, or `high`, independently of genre.
The default is `mid`, preserving the original melody range; `low` and `high`
are one octave below and above it. The schema, validator, saved styles and model prompt carry
the setting. The counter-melody follows the same range, preserving its relation
to the lead. Presets without the field preserve the upstream range. Explicit
saved register choices are retained.

Brightness follows each genre's original master low-pass settings. The earlier
shared ceiling has been removed to preserve the native character of every
genre. No additional filter, worker or model call is introduced.

Tests exercise the register, active phrase development, native tone response
and upstream harmony across all ten genres. They establish functional
contracts; listening comparisons are needed to assess musical preference.

The default output adapter queries device capabilities. Mono outputs receive
the average of both internal stereo channels through a reusable callback
buffer; stereo and multichannel devices retain the original stereo path.
Device names and system routing are not changed. Startup errors sent through
the readiness pipe are also flushed to the daemon log for diagnosis.

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
