# Shared Font Cache

This directory is a local build cache for publication fonts. The font binaries
are intentionally ignored by Git.

Run:

```bash
make fonts
```

The script downloads or copies the Winston publication fonts into this single
shared directory so work folders do not need their own `fonts/` subdirectories.
