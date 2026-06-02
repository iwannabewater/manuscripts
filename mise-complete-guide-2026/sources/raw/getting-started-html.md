# Getting Started | mise-en-place

> Source: https://mise.jdx.dev/getting-started.html

Skip to content

mise-en-place

SearchK

Appearance

Menu
Return to top

Getting Started ​

Get up and running with mise in minutes.

1. Install mise CLI ​

See installing mise for other ways to install mise (macport, apt, yum, nix, etc.).

Linux/macOSBrewWindowsDebian/Ubuntu (apt)Fedora 41+, RHEL/CentOS Stream 9+ (dnf)Snap (beta)

shellcurl https://mise.run | sh

By default, mise installs to ~/.local/bin, but it can go anywhere.

Verify the installation:

shell~/.local/bin/mise --version
# mise 2024.x.x

~/.local/bin does not need to be in PATH. mise will automatically add its own directory to PATH when activated.

mise respects MISE_DATA_DIR and XDG_DATA_HOME if you'd like to change these locations.

2. mise exec and run ​

Once installed, you can start using mise right away to install and run tools, launch tasks, and manage environment variables.

The quickest way to run a tool at a specific version is mise x|exec. For example, to launch a Python 3 REPL:

TIP

If mise isn't on PATH yet, use ~/.local/bin/mise instead.

shmise exec python@3 -- python
# this will download and install Python if it is not already installed
# Python 3.15.0
# >>> ...

or run node 26:

shmise exec node@26 -- node -v
# v26.x.x

To install a tool permanently, use mise u|use:

shellmise use --global node@26 # install node 26 and set it as the global default
mise exec -- node my-script.js
# run my-script.js with node 26...

mise r|run lets you run tasks or scripts with the full mise context (tools + env vars) loaded.

TIP

You can set a shell alias in your shell's rc file like alias x="mise x --" to save some keystrokes.

3. Activate mise optional ​

mise exec works great for one-off commands, but for interactive shells you'll probably want to activate mise so tools and environment variables are loaded automatically.

There are two approaches:

mise activate — updates your PATH and environment every time your prompt runs. Recommended for interactive shells.

Shims — symlinks that intercept commands and load the right environment. Better for CI/CD, IDEs, and scripts. Note that shims don't support all features of mise activate.

You can also skip both and call mise exec or mise run directly. See this guide for more information.

Here is how to activate mise for your shell:

https://mise.runBrewWindowsOther package managers

bashzshfish

shecho 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc

shecho 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc

shecho '~/.local/bin/mise activate fish | source' >> ~/.config/fish/config.fish

Restart your shell session after modifying your rc file. Run mise dr|doctor to verify everything is set up correctly.

With mise activated, tools are available directly on PATH:

shmise use --global node@26
node -v
# v26.x.x

When you ran mise use --global node@26, mise updated your global config:

~/.config/mise/config.toml

toml[tools]
node = "26"

Shell Feature Compatibility ​

Not all shells support every mise feature:

FeatureBashZshFishNushellElvishXonshPowerShell

mise activateYesYesYesYesYesYesYes

mise shellYesYesYesYesYesYesYes

Shell aliases ([shell_alias])YesYesYesNoNoYesNo

chpwd hookYesYesYesYesYesYesYes

4. Use tools from backends (npm, pipx, core, aqua, github) ​

Backends are the package ecosystems that mise pulls tools from. With mise use, you can install from any of them.

Install claude-code from npm:

sh# one-off
mise exec npm:@anthropic-ai/claude-code -- claude --version

# or install globally
mise use --global npm:@anthropic-ai/claude-code
claude --version

Install black from PyPI via pipx:

sh# one-off
mise exec pipx:black -- black --version

# or install globally
mise use --global pipx:black
black --version

Install ripgrep directly from GitHub releases:

sh# one-off
mise exec github:BurntSushi/ripgrep -- rg --version

# or install globally
mise use --global github:BurntSushi/ripgrep
rg --version

Each mise use command above updates your config file. For example, after running all three globally, your ~/.config/mise/config.toml would contain:

~/.config/mise/config.toml

toml[tools]
"npm:@anthropic-ai/claude-code" = "latest"
"pipx:black" = "latest"
"github:BurntSushi/ripgrep" = "latest"

You can also edit mise.toml directly instead of using mise use — the effect is the same. Run mise install after editing to install the tools.

See Backends for more ecosystems and details.

Trusting config files ​

When you or a teammate adds a mise.toml to a project, mise will prompt you to trust it before it runs any env directives or hooks:

mise ~/my-project/mise.toml is not trusted. Trust it? [y/n]

This is a security measure — config files can execute arbitrary code via [env] directives, hooks, and tasks. To trust a file, run:

shmise trust

This only needs to be done once per file. See mise trust for more details.

To disable trust prompts entirely, trust the root path:

shmise settings trusted_config_paths=["/"]

Or set the environment variable MISE_TRUSTED_CONFIG_PATHS=/.

TIP

mise use automatically trusts the file it creates, so you'll only see this prompt when pulling a config someone else wrote or when editing mise.toml by hand.

5. Setting environment variables ​

Define environment variables in mise.toml — they'll be loaded whenever mise is activated or when using mise exec:

mise.toml

toml[env]
NODE_ENV = "production"

shmise exec -- node --eval 'console.log(process.env.NODE_ENV)'

# or if mise is activated in your shell
echo "node env: $NODE_ENV"
# node env: production

6. Run a task ​

Define tasks in mise.toml and run them with mise run:

mise.toml

toml[tasks]
hello = "echo hello from mise"

shmise run hello
# hello from mise

TIP

mise automatically installs all tools from mise.toml before running a task.

See tasks for more on defining and running tasks.

7. Next steps ​

Follow the walkthrough for more examples on how to use mise.

Set up autocompletion ​

See autocompletion to learn how to set up autocompletion for your shell.

GitHub API rate limiting ​

WARNING

Many tools in mise require the GitHub API. Unauthenticated requests are often rate limited — if you see 4xx errors, see GitHub Tokens for how to configure authentication.
