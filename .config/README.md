# How to setup configs correctly

## Directory and file placement:

**Directories/Folders to be placed in ~/.config**

**Files like .p10k.zsh and .zshrc to be placed in your home directory**

## Dependencies
Hyprland with [Cealestia shell](https://github.com/caelestia-dots/shell) - WM/Wayland

Kitty - Terminal

Zsh - Shell

## Installation

Before Installing backup your current .config

> Back up your existing configs first: `cp -r ~/.config ~/.config.bak`

```
git clone https://github.com/Ivory-sudo/Linux-rice-v1.git
cd Linux-rice-v1
cp -r .config/* ~/.config/
cp .zshrc .p10k.zsh ~/
```

## Zsh Setup
- [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh): zsh framework
- [Powerlevel10k](https://github.com/romkatv/powerlevel10k): prompt theme

### Plugins
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions): suggests commands as you type, based on history
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting): colors commands as you type
- [zsh-history-substring-search](https://github.com/zsh-users/zsh-history-substring-search): search history with the up/down arrows
- [zsh-completions](https://github.com/zsh-users/zsh-completions): extra tab completions

## CLI Tools
- [fzf](https://github.com/junegunn/fzf): fuzzy finder for files, history, and anything piped into it
- [zoxide](https://github.com/ajeetdsouza/zoxide): smarter `cd` that learns your most-used directories
