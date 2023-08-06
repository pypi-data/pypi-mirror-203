# Setup fzf
# ---------
if [[ ! "$PATH" == *$HOME/.rolv/fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}$HOME/.rolv/fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "$HOME/.rolv/fzf/shell/completion.bash" 2> /dev/null

# Kubens bug
# ----------
export KUBECTX_IGNORE_FZF=1

# Key bindings
# ------------
source "$HOME/.rolv/fzf/shell/key-bindings.bash"
