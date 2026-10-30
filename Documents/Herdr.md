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

## Howto reload the Herdr config

After editing `config.toml`, apply the changes without restarting herdr or its panes:

- Inside herdr: press `F5` (bound by `reload_config = "f5"` under `[keys]`)
- From a shell:

```bash
# Optional: check the config for errors first
herdr config check

# Reload the config
herdr server reload-config
```

## Useful commands

```bash

# Update herdr to the latest version
herdr update

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
surface0 = "#313244"
surface1 = "#45475a"
surface_dim = "#1e1e2e"
overlay0 = "#6c7086"
overlay1 = "#7f849c"
text = "#fff"
subtext0 = "#bac2de"
red = "#f38ba8"
green = "#a6e3a1"
yellow = "#FFFF00"
blue = "#89b4fa"
mauve = "#cba6f7"
teal = "#94e2d5"
peach = "#fab387"
accent = "#a6e3a1"

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
close_tab = "alt+w"
rename_tab = "f2"
move_tab_previous = "alt+shift+left"
move_tab_next = "alt+shift+right"

# F5: reload this config without restarting herdr
reload_config = "f5"

# Spaces (workspaces): alt+up/down
previous_workspace = "alt+up"
next_workspace = "alt+down"
close_workspace = "alt+shift+w"

# F1: jump to the target of the latest notification (e.g. an agent that finished)
open_notification_target = "f1"



```

## Plugin: herdr-file-viewer

[herdr-file-viewer](https://github.com/smarzban/herdr-file-viewer) is a plugin that opens a file viewer in a split or a tab inside herdr (Windows details: [windows.md](https://github.com/smarzban/herdr-file-viewer/blob/main/docs/windows.md)).

Install (on Windows herdr must be on its pre-release update channel; requires Windows PowerShell 5.1):

```bash
herdr plugin install smarzban/herdr-file-viewer
```

Add the shortcuts to `config.toml` (Windows uses the `-windows` action IDs; on Linux/macOS drop the `-windows` suffix), then reload with `F5`:

```toml
[[keys.command]]
key = "prefix+f"
type = "plugin_action"
command = "herdr-file-viewer.open-file-viewer-windows"
description = "open file viewer in split"

[[keys.command]]
key = "prefix+shift+f"
type = "plugin_action"
command = "herdr-file-viewer.open-file-viewer-tab-windows"
description = "open file viewer in tab"
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
