# Zig's fork objectives

The first objective of this fork was to get SpinTool to work on a standard Linux installation in 2024, 3 years after the last commit, and fix any bug I encounter while using it.
Secondary objectives include tweaks or new features to match my own workflow, which may get merged upstream eventually.

Ideas:
- command-line options to load MIDI mapping, scenes, mute groups
- command-line options to load a song
- visual feedback showing how long is left before a clip starts
- display the content of the clip and a progression bar on top of it (like seq24/seq66/seq192), see e.g. [this gist](https://gist.github.com/SpotlightKid/33ed933944beed851697039142613d98) 
- let clips start at the next bar, even if it is not a multiple of its duration? i.e. never wait more than 1 bar before a clip starts
- OSC interface similar to seq192's
- end recording when I press a button, with MIDI mapping
- logging with levels
- vumeters on the clips?
- LED blink in sync with tempo
- progression bars update every beat, with constant interpolation
- progression bars on the clip when not playing, in a different color, like seq24/se166/seq128
- Jack transport: remove the ticks number, remove the bars number, remove the rewind button, ensure that the beat number is in sync

Done:
- Fixed bugs with Qt widgets' `setvalue()` requiring integers, see [81ce4f6c](/../../commit/81ce4f6cbfd365d9e91a8673ffc7f3f2792efcd1)
- Fixed a bug when triggering an empty clip via midi, see [5c2380ad](/../../commit/5c2380ad3e79427a83d8f439af3dc7d76e82cd2b)