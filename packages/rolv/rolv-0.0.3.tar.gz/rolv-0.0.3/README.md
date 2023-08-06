# Rolv
Personal package to quickly setup a shell to my liking, with functions, shell integrations, scripts, aliasses, etc.

Not intended to be used by others, though everyone is free to copy/reuse code that they find useful.

## Notices
- Will remove all files under `$HOME/.local/bin` that start with `__rolv_`!
- Will copy executables to `$HOME/.local/bin`! (all files written there are prefixed with `__rolv_`)
- Will add a block to any default rc file path, such as `$HOME/.bashrc`, unless `ROLV_RC_FILE_PATH` is present in env!
