# Setup | direnv

> Source: https://direnv.net/docs/hook.html

direnv

Setup

For direnv to work properly it needs to be hooked into the shell. Each shell
has its own extension mechanism.

Once the hook is configured, restart your shell for direnv to be activated.

BASH

Add the following line at the end of the ~/.bashrc file:

eval "$(direnv hook bash)"

Make sure it appears even after rvm, git-prompt and other shell extensions
that manipulate the prompt.

ZSH

Add the following line at the end of the ~/.zshrc file:

eval "$(direnv hook zsh)"

Oh my zsh

Oh my zsh has a core plugin with direnv support.

Add direnv to the plugins array in your zshrc file:

plugins=(... direnv)

FISH

Add the following line at the end of the ~/.config/fish/config.fish file:

direnv hook fish | source

Fish supports 3 modes you can set with the global environment variable direnv_fish_mode:

set -g direnv_fish_mode eval_on_arrow    # trigger direnv at prompt, and on every arrow-based directory change (default)
set -g direnv_fish_mode eval_after_arrow # trigger direnv at prompt, and only after arrow-based directory changes before executing command
set -g direnv_fish_mode disable_arrow    # trigger direnv at prompt only, this is similar functionality to the original behavior

TCSH

Add the following line at the end of the ~/.cshrc file:

eval `direnv hook tcsh`

Elvish (0.12+)

Run:

~> mkdir -p ~/.config/elvish/lib
~> direnv hook elvish > ~/.config/elvish/lib/direnv.elv

and add the following line to your ~/.config/elvish/rc.elv file:

use direnv

Nushell

Add the following hook to your $env.config.hooks.env_change.PWD list in config.nu:

{ ||
if (which direnv | is-empty) {
return
}

direnv export json | from json | default {} | load-env
}

Note
you can follow the nu_scripts of Nushell
for the always up-to-date version of the hook above

PowerShell

Add the following line to your $PROFILE:

Invoke-Expression "$(direnv hook pwsh)"

Murex

Add the following line to your ~/.murex_profile file:

direnv hook murex -> source

This site is open source. Improve this page.
