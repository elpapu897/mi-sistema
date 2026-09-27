export PATH="/home/matiigonzz/.nvm/versions/node/v24.18.1/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# ============ PLUGINS CONFIGURATION ============
# Nano Banana (Image Generation)
export NANO_BANANA_PATH="$HOME/.config/Claude/local-agent-mode-sessions"

# Gemini CLI Configuration
export GEMINI_API_KEY="AQ.Ab8RN6L7F0onTJfOvPPf9pPqXqvz3HpW5Cd1RLm1PzptoMC6qw"
export GEMINI_CLI_TRUST_WORKSPACE=true

# Antigravity CLI
export PATH="$HOME/.local/bin:$PATH"

# pinguclean (limpieza del sistema)
pingu() {
    sudo /usr/local/sbin/pinguclean.sh "$@"
}
