# Installing Mise | mise-en-place

> Source: https://mise.jdx.dev/installing-mise.html

Skip to content

mise-en-place

SearchK

Appearance

Menu
Return to top

Installing Mise ​

If you are new to mise, follow the Getting Started guide first.

Installation Methods ​

This page lists various ways to install mise on your system.

PlatformRecommendedAlternative

macOSHomebrewmise.run

Linux (Debian/Ubuntu)aptmise.run

Linux (Fedora/RHEL)dnfmise.run

Linux (Arch)pacmanmise.run

Linux (Alpine)apkmise.run

WindowsScoopwinget

Any (Rust users)cargo binstallcargo install

CI/Dockermise.runGitHub Releases

Which methods auto-update?

Package managers (apt, dnf, brew, pacman, etc.) update mise when you update system packages. Other methods can be updated with mise self-update.

https://mise.run ​

Note that it isn't necessary for mise to be on PATH. If you run the activate script in your shell's rc file, mise will automatically add itself to PATH.

shcurl https://mise.run | sh

or with options

shcurl https://mise.run | MISE_INSTALL_PATH=/usr/local/bin/mise sh

Shell-specific installation + activation ​

For a more streamlined setup, you can use shell-specific endpoints that will install mise and automatically configure activation in your shell's configuration file:

zshbashfish

shcurl https://mise.run/zsh | sh
# Installs mise and adds activation to ~/.zshrc

shcurl https://mise.run/bash | sh
# Installs mise and adds activation to ~/.bashrc

shcurl https://mise.run/fish | sh
# Installs mise and adds activation to ~/.config/fish/config.fish

These shell-specific installers will:

Install mise using the same logic as the main installer

Automatically detect your shell's configuration file

Add the activation line if it's not already present

Skip adding activation if it's already configured (safe to run multiple times)

Options:

MISE_DEBUG=1 – enable debug logging

MISE_QUIET=1 – disable non-error output

MISE_INSTALL_PATH=/some/path – change the binary path (default: ~/.local/bin/mise)

MISE_VERSION=v2025.12.0 – install a specific version

If you want to verify the install script hasn't been tampered with:

shgpg --keyserver hkps://keys.openpgp.org --recv-keys 24853EC9F655CE80B48E6C3A8B81C9D17413A06D
curl https://mise.en.dev/install.sh.sig | gpg --decrypt > install.sh
# ensure the above is signed with the mise release key
sh ./install.sh

TIP

As long as you don't change the version with MISE_VERSION, the install script will be pinned to whatever the latest version was when it was downloaded with checksums inside the file. This makes downloading the file and putting it into a project a great way to ensure that anyone installing with that script fetches the exact same mise bin.

Supported os/arch:

macos-x64

macos-arm64

linux-x64

linux-x64-musl

linux-arm64

linux-arm64-musl

linux-armv6

linux-armv6-musl

linux-armv7

linux-armv7-musl

If you need something else, compile it with cargo install mise (see below).

apk ​

For Alpine Linux:

shapk add mise

mise lives in the community repository.

apt ​

On Ubuntu 26.04+, mise is available via a PPA:

shsudo add-apt-repository -y ppa:jdxcode/mise
sudo apt update -y
sudo apt install -y mise

For older Ubuntu/Debian versions:

shsudo apt update -y && sudo apt install -y curl
sudo install -dm 755 /etc/apt/keyrings
curl -fSs https://mise.en.dev/gpg-key.pub | sudo tee /etc/apt/keyrings/mise-archive-keyring.asc 1> /dev/null
echo "deb [signed-by=/etc/apt/keyrings/mise-archive-keyring.asc] https://mise.en.dev/deb stable main" | sudo tee /etc/apt/sources.list.d/mise.list
sudo apt update -y
sudo apt install -y mise

pacman ​

For Arch Linux:

shsudo pacman -S mise

Arch package

Cargo ​

Build from source with Cargo:

shcargo install --locked mise

Do it faster with cargo-binstall:

shcargo install cargo-binstall
cargo binstall mise

Build from the latest commit in main:

shcargo install mise --git https://github.com/jdx/mise --branch main

dnf ​

Fedora 41+, CentOS Stream 9+, RHEL 10+ ​

shdnf copr enable jdxcode/mise
dnf install mise

RHEL 9 / AlmaLinux 9 / Rocky 9 ​

RHEL 9 AppStream is currently frozen at Rust 1.88, which is older than mise's minimum supported Rust version. Use the CentOS Stream 9 build instead — the resulting binary works on RHEL 9 derivatives:

shdnf copr enable jdxcode/mise centos-stream+epel-next-9
dnf install mise

COPR package page

Snap (Linux, currently in beta) ​

shsudo snap install mise --classic --beta

snapcraft.io page

Docker ​

See the Docker cookbook for tips on using mise with Docker.
Example Dockerfile
dockerfileFROM debian:13-slim

RUN apt-get update \
&& apt-get -y --no-install-recommends install sudo curl git ca-certificates build-essential \
&& rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV MISE_DATA_DIR="/mise"
ENV MISE_CONFIG_DIR="/mise"
ENV MISE_CACHE_DIR="/mise/cache"
ENV MISE_INSTALL_PATH="/usr/local/bin/mise"
ENV PATH="/mise/shims:$PATH"
RUN curl https://mise.run | sh
RUN mise trust -a && mise install

Homebrew ​

shbrew install mise

Homebrew formula

npm ​

mise is available on npm as a precompiled binary. This isn't a Node.js package—just distributed via npm. This is useful for JS projects that want to setup mise via package.json or npx.

shnpm install -g mise

Use npx if you just want to test it out for a single command without fully installing:

shnpx mise exec python@3.11 -- python some_script.py

npm package

The legacy @jdxcode/mise package is still published.

GitHub Releases ​

Download the latest release from GitHub.

shcurl -L https://github.com/jdx/mise/releases/download/v2025.12.0/mise-v2025.12.0-linux-x64 > /usr/local/bin/mise
chmod +x /usr/local/bin/mise

MacPorts ​

shsudo port install mise

MacPorts port

nix ​

For the Nix package manager, at release 24.05 or later:

shnix-env -iA mise

You can also import the package directly using mise-flake.packages.${system}.mise. It supports all default Nix systems.

NixOS compiles from source by default

For precompiled binaries, enable nix-ld and disable all_compile.

yum (RHEL 8, CentOS Stream 8, Amazon Linux 2) ​

shyum install -y yum-utils
yum-config-manager --add-repo https://mise.en.dev/rpm/mise.repo
yum install -y mise

zypper ​

shsudo wget https://mise.en.dev/rpm/mise.repo -O /etc/zypp/repos.d/mise.repo
sudo zypper refresh
sudo zypper install mise

Windows - Scoop ​

This is the recommended way to install mise on Windows. It will automatically add your shims to PATH.

shscoop install mise

Scoop manifest

Windows - winget ​

shwinget install jdx.mise

winget manifest

Windows - Chocolatey ​

INFO

chocolatey version is currently outdated.

shchoco install mise

Windows - manual ​

Download the latest release from GitHub and add the binary to your PATH.

If your shell does not support mise activate, you would want to edit PATH to include the shims directory (by default: %LOCALAPPDATA%\mise\shims).

Shells ​

Bash ​

shecho 'eval "$(mise activate bash)"' >> ~/.bashrc

Zsh ​

shecho 'eval "$(mise activate zsh)"' >> "${ZDOTDIR-$HOME}/.zshrc"

Fish ​

shecho 'mise activate fish | source' >> ~/.config/fish/config.fish

TIP

For homebrew and possibly other installs mise is automatically activated so this is not necessary.

See MISE_FISH_AUTO_ACTIVATE=1 for more information.

PowerShell ​

WARNING

See about_Profiles docs to find your actual profile location. You will need to first create the parent directory if it does not exist.

powershellecho '(&mise activate pwsh) | Out-String | Invoke-Expression' >> $HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1

Nushell ​

Nu does not support eval Install Mise by appending env.nu and config.nu:

nushell'
let mise_path = $nu.default-config-dir | path join mise.nu
^mise activate nu | save $mise_path --force
' | save $nu.env-path --append
"\nuse ($nu.default-config-dir | path join mise.nu)" | save $nu.config-path --append

If you prefer to keep your dotfiles clean you can save it to a different directory then update $env.NU_LIB_DIRS:

nushell"\n$env.NU_LIB_DIRS ++= ($mise_path | path dirname | to nuon)" | save $nu.env-path --append

Xonsh ​

Since .xsh files are not compiled you may shave a bit off startup time by using a pure Python import: add the code below to, for example, ~/.config/xonsh/mise.py config file and import mise it in ~/.config/xonsh/rc.xsh:

pythonfrom pathlib import Path
from xonsh.built_ins import XSH

ctx = XSH.ctx
mise_init = subprocess.run([Path('~/bin/mise').expanduser(),'activate','xonsh'],capture_output=True,encoding="UTF-8").stdout
XSH.builtins.execx(mise_init,'exec',ctx,filename='mise')

Or continue to use rc.xsh/.xonshrc:

shecho 'execx($(~/bin/mise activate xonsh))' >> ~/.config/xonsh/rc.xsh # or ~/.xonshrc

Given that mise replaces both shell env $PATH and OS environ PATH, watch out that your configs don't have these two set differently (might throw os.environ['PATH'] = xonsh.built_ins.XSH.env.get_detyped('PATH') at the end of a config to make sure they match)

Elvish ​

Add following to your rc.elv:

shellvar mise: = (ns [&])
eval (mise activate elvish | slurp) &ns=$mise: &on-end={|ns| set mise: = $ns }
mise:activate

Optionally alias mise to mise:mise for seamless integration of mise {activate,deactivate,shell}:

shelledit:add-var mise~ {|@args| mise:mise $@args }

Something else? ​

Adding a new shell is not hard at all since very little shell code is in this project. See here for how the others are implemented. If your shell isn't currently supported I'd be happy to help you get yours integrated.

Autocompletion ​

TIP

Some installation methods automatically install autocompletion scripts.

The mise completion command can generate autocompletion scripts for your shell. This requires usage to be installed. If you don't have it, install it with:

shellmise use -g usage

Then, run the following commands to install the completion script for your shell:

bashzshfish

sh# This requires bash-completion to be installed
mkdir -p ~/.local/share/bash-completion/completions/
mise completion bash --include-bash-completion-lib > ~/.local/share/bash-completion/completions/mise

sh# If you use oh-my-zsh, there is a `mise` plugin. Update your .zshrc file with:
# plugins=(... mise)

# Otherwise, look where zsh search for completions with
echo $fpath | tr ' ' '\n'

# if you installed zsh with `apt-get` for example, this will work:
mkdir -p /usr/local/share/zsh/site-functions
mise completion zsh  > /usr/local/share/zsh/site-functions/_mise

shmise completion fish > ~/.config/fish/completions/mise.fish

Then source your shell's rc file or restart your shell.

Troubleshooting ​

If you encounter issues after installation, run:

shmise doctor

This will diagnose common problems with your mise setup. See mise doctor for more information.

Uninstalling ​

Use mise implode to uninstall mise. This will remove the mise binary and all of its data. Use mise implode --help for more information.

Alternatively, manually remove the following directories to fully clean up:

~/.local/share/mise (can also be MISE_DATA_DIR or XDG_DATA_HOME/mise)

~/.local/state/mise (can also be MISE_STATE_DIR or XDG_STATE_HOME/mise)

~/.config/mise (can also be MISE_CONFIG_DIR or XDG_CONFIG_HOME/mise)

on Linux: ~/.cache/mise (can also be MISE_CACHE_DIR or XDG_CACHE_HOME/mise)

on macOS: ~/Library/Caches/mise (can also be MISE_CACHE_DIR)
