# Herdr

[Herdr](https://github.com/ogulcancelik/herdr) is an open-source terminal multiplexer (like tmux) for running several AI coding agents (Claude Code, Codex, Copilot CLI, ...) side by side. A sidebar shows the state of every agent: blocked, working, done or idle.

Docs: <https://herdr.dev/docs/>

## Howto start, detach and reattach a session

```bash
# Start herdr in the directory where your work lives (also reattaches to a running session)
herdr

# Detach: sessions (and agents) keep running in the background
# Press ctrl+b, release, then press q
```

## Useful commands

```bash
# Show the resolved config path
herdr --help

# Print the full default config (a good starting point)
herdr --default-config

# Apply config changes without restarting panes
herdr server reload-config

# Check the config for errors
herdr config check
```

Set the `HERDR_CONFIG_PATH` environment variable to use a different config file.

Main sections: `[keys]`, `[theme]`, `[ui]`, `[terminal]`, `[worktrees]`, `[remote]`, `[server]`, `[session]`.

## My keybindings

Herdr works with a config file. The file lives at:

- Linux / macOS: `~/.config/herdr/config.toml`
- Windows: `%APPDATA%\herdr\config.toml`

```bash
# C:\Users\<YOUR_USERNAME>\AppData\Roaming\herdr\config.toml

onboarding = false

[ui.sound]
enabled = false

[theme]
name = "catppuccin"
auto_switch = false

[theme.custom]
panel_bg = "none"
surface0 = "#e2e2e2"
surface1 = "#d7d7d7"
surface_dim = "#e8e8e8"
overlay0 = "#6b6b6b"
overlay1 = "#565656"
text = "#fff"
subtext0 = "#474747"
red = "#a8334c"
green = "#4f6c31"
yellow = "#FFFF00"
blue = "#286486"
mauve = "#88507d"
teal = "#3b8992"
peach = "#944927"
accent = "#4f6c31"

[ui]
status_indicators = "symbols"
prompt_new_tab_name = false

# Sidebar: which columns each row shows for agents and for spaces.
[ui.sidebar.agents]
row_gap = 0
rows = [
  ["state_icon", {token = "terminal_title_stripped", dim = false, fg = "#a0a0a0"}],
  [{token = "workspace", dim = true, bold = false, fg ="#FFFF00" }],
]

[ui.sidebar.spaces]
row_gap = 0
rows = [
  ["state_icon", {token = "workspace", dim = true, bold = false, fg ="#FFFF00" }],
  ["branch", "git_status"],
]

[ui.toast]
delivery = "herdr"

[keys]
# Tabs: alt+left/right, alt+1..9 for direct jump
previous_tab = "alt+left"
next_tab = "alt+right"
switch_tab = "alt+1..9"
new_tab = "alt+t"
close_tab = "alt+shift+t"
rename_tab = "f2"
move_tab_previous = "alt+shift+left"
move_tab_next = "alt+shift+right"

# F5: reload this config without restarting herdr
reload_config = "f5"

# Spaces (workspaces): alt+up/down
previous_workspace = "alt+up"
next_workspace = "alt+down"

# F1: jump to the target of the latest notification (e.g. an agent that finished)
open_notification_target = "f1"

```

## Open/edit config.toml file in Herdr in nano (or your preferred editor)

```bash
# Open the config file in nano (or your preferred editor)
        

```powershell
## add the herdr-config function to your PowerShell profile (if not already present)
if (!(Test-Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force | Out-Null }

Add-Content $PROFILE @'

function herdr-config {
    $nano = if (Get-Command nano -ErrorAction SilentlyContinue) { 'nano' } else { 'C:\Program Files\Git\usr\bin\nano.exe' }
    & $nano "$env:APPDATA\herdr\config.toml"
    herdr config check
    herdr server reload-config
}
'@

. $PROFILE

## when added, you can run the following command to open the config file in Herdr:
herdr-config

```
