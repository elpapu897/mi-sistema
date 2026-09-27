export PATH="/home/matiigonzz/.nvm/versions/node/v24.18.1/bin:$PATH"
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
    for rc in ~/.bashrc.d/*; do
        if [ -f "$rc" ]; then
            . "$rc"
        fi
    done
fi
unset rc

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# kimi-code
export PATH="/home/matiigonzz/.kimi-code/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# ============ PLUGINS CONFIGURATION ============
# Nano Banana (Image Generation)
export NANO_BANANA_PATH="$HOME/.config/Claude/local-agent-mode-sessions"

# Gemini CLI Configuration
export GEMINI_API_KEY="AQ.Ab8RN6L7F0onTJfOvPPf9pPqXqvz3HpW5Cd1RLm1PzptoMC6qw"
export GEMINI_CLI_TRUST_WORKSPACE=true

# Antigravity CLI
export PATH="$HOME/.local/bin:$PATH"

# Quick aliases
alias nanobana='python "$CLAUDE_PLUGIN_ROOT/scripts/genimage.py"'
alias gemini-check='command -v gemini && echo "✅ Gemini CLI available" || echo "❌ Gemini CLI not found"'
alias agy-check='command -v agy && agy --version || echo "❌ Antigravity CLI not found"'

[ -f ~/.replicate-env ] && source ~/.replicate-env

alias img='python ~/Claude/scripts/genimage-replicate.py'

# rice-claude
export PATH="$HOME/.local/bin:$PATH"
alias vim='nvim'
alias vi='nvim'
alias ff='fastfetch'
# saludo al abrir terminal interactiva
if [[ $- == *i* ]] && command -v fastfetch >/dev/null; then
  fastfetch
fi

# opencode
export PATH=/home/matiigonzz/.opencode/bin:$PATH

# pinguclean (limpieza del sistema)
pingu() {
    sudo /usr/local/sbin/pinguclean.sh "$@"
}
. "$HOME/.cargo/env"

. "/home/matiigonzz/.deno/env"
