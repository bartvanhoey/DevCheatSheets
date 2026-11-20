## Vim

### Start the interactive Vim tutorial (run in a shell, not inside Vim)

```bash
vimtutor
```

### Essential commands

| Command | Action |
|---------|--------|
| `i` | Enter insert mode to start typing text |
| `<ESC>` | Leave insert mode (back to normal mode) |
| `:w` | Save (write) the file |
| `:wq` | Save and quit |
| `:q!` | Quit without saving |
| `x` | Delete the character under the cursor |
| `dd` | Delete (cut) the current line |
| `yy` | Copy (yank) the current line |
| `p` | Paste after the cursor |
| `u` | Undo |
| `Ctrl+r` | Redo |
| `/text` | Search forward for `text` (`n` = next match, `N` = previous) |
| `gg` / `G` | Go to the first / last line |

All `:` commands are typed in normal mode — press `<ESC>` first if you are in insert mode.
