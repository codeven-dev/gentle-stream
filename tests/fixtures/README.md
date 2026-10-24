# Upstream harmony reference

`upstream_harmony.json` was generated from the unmodified `src/` tree of
Gentleman-Programming/gentle-stream commit
`381290451544ad2ca3348a68a81b3056bdac73b7`, using the same Python and NumPy
environment as the fork tests.

Each case uses `Style(genre=..., mode=...)` with the upstream defaults,
`Composer(style, seed, 50, genres.get(genre).chord)`, and plans bars 0–123.
The cases cover every genre in minor, all six modes in lo-fi, and seeds 7 and 42.

For each plan, `dataclasses.asdict` is restricted to `section`, `section_bar`,
`energy`, `chord`, `passing`, `key_offset`, and `bass`. The checksum is
`sha256(json.dumps(plans, sort_keys=True).encode()).hexdigest()`.

This reference verifies that new melodic answers do not change the existing
harmonic or bass decisions. It intentionally excludes melody, counter-melody,
layer masks, audio and subjective quality. Regenerate from the recorded
upstream source only when deliberately changing that compatibility contract.
