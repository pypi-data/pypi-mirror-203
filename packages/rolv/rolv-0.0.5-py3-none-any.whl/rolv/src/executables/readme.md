- Files in this folder should be:
  - executable (if it is a script, add a shebang)
  - single-filed (one file = one program)
- Files in this folder will be placed in $HOME/.local/bin, where the file name will be prefixed with `__rolv_`
- Before that though, files under $HOME/.local/bin starting with `__rolv_` are deleted (ensuring outdated files are removed).
- An alias will be made for each file in this folder, such that `alias ${filename}="__rolv_${filename}"`

This system makes sure that we can bulk copy files from this folder over to `$HOME/.local/bin` and 
easily remove outdated files, without keeping track of state.


