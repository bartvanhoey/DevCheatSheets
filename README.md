# DevCheatSheets

[![pages-build-deployment](https://github.com/bartvanhoey/DevCheatSheets/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/bartvanhoey/DevCheatSheets/actions/workflows/pages/pages-build-deployment) [![Validate](https://github.com/bartvanhoey/DevCheatSheets/actions/workflows/validate.yml/badge.svg)](https://github.com/bartvanhoey/DevCheatSheets/actions/workflows/validate.yml)

Personal cheat-sheet collection for developer tools, commands, and tips —
primarily aimed at **.NET developers** working on **Windows** with **VS Code** or **Rider**.
Topics include Git, Docker, Kubernetes, .NET, Blazor, VS Code, Rider, and more.

## IDE & Editors

| Topic | Description |
|-------|-------------|
| [VS Code](Documents/VsCode.md) | Favorite shortcuts, extensions and settings tweaks |
| [Rider Keyboard Shortcuts](Documents/Rider.md) | Favorite shortcuts (Visual Studio keymap) and tips |
| [Vim Editor](Documents/VimEditor.md) | Essential commands to edit, save and quit |
| [Notepad++](Documents/NotepadPlusPlus.md) | Notepad++ tips and tricks |

## DevOps & Cloud

| Topic | Description |
|-------|-------------|
| [Docker](Documents/Docker.md) | Commands for images, containers, Compose, volumes and Docker Hub |
| [Kubernetes](Documents/Kubernetes.md) | K8S dashboard setup, RBAC fix and kubectl commands |
| [Azure Kubernetes Service](Documents/AKS.md) | Connect kubectl to an AKS cluster, DNS zones and cluster deletion |
| [Azurite](Documents/Azurite.md) | Install and run the local Azure Storage emulator |
| [Ngrok](Documents/Ngrok.md) | Expose localhost through tunnels, incl. multiple ports and scripts |
| [Insomnia](Documents/Insomnia.md) | Chain API requests with environment variables |

## .NET & C#

| Topic | Description |
|-------|-------------|
| [.NET](Documents/DotNet.md) | dotnet CLI commands for solutions, projects and SDK versions |
| [EF Core](Documents/EntityFrameworkCore.md) | EF Core tools and migration commands |
| [ABP CLI](Documents/ABPcli.md) | Install, upgrade and use the ABP Framework CLI |
| [Advanced C#](Documents/AdvancedCSharp.md) | Advanced C# concepts a senior developer uses daily |
| [Blazor](Documents/Blazor.md) | Blazor tips: file nesting, debug assets and HTTPS dev certificate |

## Frontend & CSS

| Topic | Description |
|-------|-------------|
| [Tailwind CSS](Documents/TailwindCss.md) | Tailwind CLI setup and utility classes |
| [CSS](Documents/Css.md) | CSS notes, incl. cascade layers |
| [Next.js](Documents/NextJs.md) | Next.js setup, fixes and useful npm packages |

## Productivity & Learning

| Topic | Description |
|-------|-------------|
| [Boost your Productivity](Documents/BoostProductivity.md) | Ways to enhance developer productivity |
| [Refactoring Techniques](Documents/RefactoringTechniques.md) | What makes code hard to work with and how to clean it up |
| [10 Options for Maintainable .NET Apps](Documents/ScottSauber10OptionsToCreateMoreMaintainableDotNetApps.md) | Scott Sauber's 10 options for more maintainable .NET apps |
| [Useful Claude Code Skills](Documents/UsefulClaudeCodeSkills.md) | Claude Code skills and commands worth using |

## Tools & General

| Topic | Description |
|-------|-------------|
| [All about Git](Documents/Git.md) | Git and GitHub CLI tips, authentication and common fixes |
| [Command Line Commands](Documents/TopTenCommandLineCommands.md) | Handy command line commands, e.g. find the process on a port |
| [PowerShell](Documents/PowerShell.md) | PowerShell one-liners for CSV, JSON and code statistics |
| [Chrome](Documents/Chrome.md) | Chrome keyboard shortcuts and extensions |
| [Herdr](Documents/Herdr.md) | Herdr terminal multiplexer for AI agents: keys, config and plugins |

## Setup

After cloning, activate the pre-push validation hook:

```bash
git config core.hooksPath .githooks
```
