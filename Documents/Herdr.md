# Herdr

[Herdr](https://github.com/ogulcancelik/herdr) is an open-source terminal multiplexer (like tmux) for running several AI coding agents (Claude Code, Codex, Copilot CLI, ...) side by side. A sidebar shows the state of every agent: blocked, working, done or idle.

Docs: <https://herdr.dev/docs/>

## Howto install Herdr

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

```bash
# Linux / macOS
curl -fsSL https://herdr.dev/install.sh | sh

# macOS (Homebrew)
brew install herdr

# Cross-platform (mise)
mise use -g herdr
```

## Howto start, detach and reattach a session

```bash
# Start herdr in the directory where your work lives (also reattaches to a running session)
herdr

# Detach: sessions (and agents) keep running in the background
# Press ctrl+b, release, then press q
```

## Default keybindings

The default prefix is `ctrl+b`. Press it, release, then press the next key.

| Action | Key |
|--------|-----|
| Show all active bindings | `prefix` `?` |
| New tab | `prefix` `c` |
| Split right | `prefix` `v` |
| Split down | `prefix` `-` |
| Move focus between panes | `prefix` `h` `j` `k` `l` |
| Zoom focused pane | `prefix` `z` |
| Close pane | `prefix` `x` |
| Swap panes | `prefix` `shift+h/j/k/l` |
| Resize mode | `prefix` `r` |
| Copy mode | `prefix` `[` |
| Next / previous tab | `prefix` `n` / `prefix` `p` |
| Jump to tab 1-9 | `prefix` `1`..`9` |
| Rename tab | `prefix` `shift+t` |
| Close tab | `prefix` `shift+x` |
| New workspace | `prefix` `shift+n` |
| Rename workspace | `prefix` `shift+w` |
| Close workspace | `prefix` `shift+d` |
| Workspace navigation | `prefix` `w` |
| Goto picker | `prefix` `g` |
| Toggle sidebar | `prefix` `b` |
| Detach | `prefix` `q` |

## Howto configure Herdr

Herdr works without a config file. The file lives at:

- Linux / macOS: `~/.config/herdr/config.toml`
- Windows: `%APPDATA%\herdr\config.toml`

```bash
# Show the resolved config path
herdr --help

# Print the full default config (a good starting point)
herdr --default-config

# Apply config changes without restarting panes
herdr server reload-config
```

Set the `HERDR_CONFIG_PATH` environment variable to use a different config file.

Main sections: `[keys]`, `[theme]`, `[ui]`, `[terminal]`, `[worktrees]`, `[remote]`, `[server]`, `[session]`.

## Howto connect to a remote machine

```bash
herdr --remote
```

SSH keepalive and connection reuse are set in the `[remote]` section of the config.
