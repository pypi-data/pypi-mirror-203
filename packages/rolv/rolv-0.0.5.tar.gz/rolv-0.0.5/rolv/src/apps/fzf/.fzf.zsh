# Setup fzf
# ---------
if [[ ! "$PATH" == *$HOME/.rolv/fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}$HOME/.rolv/fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "$HOME/.rolv/fzf/shell/completion.zsh" 2> /dev/null

# Key bindings
# ------------
source "$HOME/.rolv/fzf/shell/key-bindings.zsh"
