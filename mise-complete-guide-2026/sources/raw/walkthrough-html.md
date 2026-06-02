# Walkthrough | mise-en-place

> Source: https://mise.jdx.dev/walkthrough.html

Skip to content

mise-en-place

SearchK

Appearance

Menu
Return to top

Walkthrough ​

Once you've completed the Getting Started guide, you're ready to start using mise. This document offers a quick overview on some initial things you may want to try out.

Installing Dev Tools ​

The main command for working with tools in mise is mise u|use. This does 2 main things:

Installs tools (if not already installed)

Adds the tool to the mise.toml configuration file—in mise I say the tool is "active" if it's in mise.toml

WARNING

Both of these are required to use a tool. If you simply install a tool via mise install, it won't be available in your shell. It must also be added to mise.toml—which is why I promote using mise use since it does both.

You use it like so (note that mise must be activated for this example to work):

bashmkdir example-project && cd example-project
mise use node@26
node -v
# v26.x.x

And you'll also note that you now have a mise.toml file with the following content:

mise.toml

mise-toml[tools]
node = "26"

If this file is in the root of a project, node will be installed whenever someone runs mise install|i.

This is the command you want to run when you first clone a project or when you want to update installed tools.

mise.toml Configuration ​

You can create a mise.toml file manually or with the CLI.

TIP

Use mise edit to open an interactive editor for your configuration. It provides a TUI where you can navigate sections, add tools from the registry with fuzzy search, and configure settings with schema-aware autocompletion.

Use mise.toml to share your tool configurations with others. This file should be committed to version control and contains the common toolset needed for your project.

For tools or settings you want to keep private, use mise.local.toml. This file should be added to .gitignore and is perfect for personal preferences or configurations.

mise supports nested configuration files that cascade from broad to specific settings:

~/.config/mise/config.toml - Global settings for all projects

~/work/mise.toml - Work-specific settings

~/work/project/mise.toml - Project-specific settings

~/work/project/mise.local.toml - Project-specific settings that should not be shared

mise will use all the parent directories together to determine the set of tools—overriding configuration as it goes lower in the hierarchy.

TIP

Use mise config ls to see the configuration files currently used by mise.

In general, it's preferred to use loose versions like node@26 in mise so that other people working on a project don't have to worry about the exact version of a tool you're using. If you'd like to pin the version to enforce a specific version, use mise use --pin or the lockfile setting.

If you leave out the version, then mise will default to node@latest.

Dev Tool Backends ​

Tools are installed with a variety of backends like aqua, github, or gitlab. See registry for the full list of shorthands like node you can use.

You can also use other backends like npm or cargo which can install any package from their respective registries:

bashmise use npm:@antfu/ni
mise use cargo:starship

Upgrading Dev Tools ​

Upgrading tool versions can be done with mise up|upgrade. By default, it will respect the version prefix in mise.toml. If a lockfile exists, mise will update mise.lock to the latest version of the tool with the prefix from mise.toml.

So if you have node = "26" in mise.toml, then mise upgrade node will upgrade to the latest version of node 26.

If you'd like to update the version in mise.toml to something newer, you can use mise upgrade --bump node. It will set the version at the same specificity as the current version, so if you have node = "24", but use mise upgrade --bump node to update to node@26, then it will set node = "26" in mise.toml.

See Dev Tools for more information on working with tools.

Setting Environment Variables ​

mise can also be used to set environment variables for your project. You can set environment variables with the CLI:

bashmise set MY_VAR=123
echo $MY_VAR
# 123

Or by directly modifying mise.toml:

toml[env]
MY_VAR = "123"

Some examples on where this can be used:

Setting NODE_ENV for a Node.js project

Setting DATABASE_URL for a database connection

Setting RUST_TEST_THREADS=1 to run cargo tests in series

Do not set secrets in a project's mise.toml, as the file is intended to be added to version control. Use mise.local.toml instead for secrets.

You can also modify PATH with mise.toml. This example makes CLIs installed with npm available:

toml[env]
_.path = "./node_modules/.bin"

This will add ./node_modules/.bin to the PATH for the project — with "." here referring to the directory the mise.toml file is in so if you enter a subdirectory, it will still work.

See Environments for more information on working with environment variables.

Tasks ​

Tasks are defined in a project to execute commands.

You can define tasks in a mise.toml:

mise.toml

mise-toml[tasks]
build = "npm run build"
test = "npm test"

Or in a mise-tasks directory as a standalone file, such as mise-tasks/build:

mise-tasks/build

bash#!/bin/bash
npm run build

Tasks are executed with mise r|run:

bashmise run build
mise run test

TIP

mise run sets up the "mise environment" before running the task (tools and environment variables). So if you'd rather not activate mise in your shell, you can use mise run to run tasks, and it will have the tools in PATH and the environment variables from mise.toml set.

mise is paired with usage which provides lots of features for documenting and running tasks.

Here is an example of a task with usage spec:

mise-tasks/greet

bash#!/usr/bin/env bash
set -e

#MISE description="Greet a user with a message"
#USAGE flag "-g --greeting <greeting>" help="The greeting word to use" {
#USAGE   choices "hi" "hello" "hey"
#USAGE }
#USAGE flag "-u --user <user>" help="The user to greet"
#USAGE flag "--dir <dir>" help="The directory to greet from" default="."
#USAGE complete "dir" run="find . -maxdepth 1 -type d"
#USAGE arg "<message>" help="Greeting message"

echo "all available options are in the env with the prefix 'usage_'"
env | grep usage_

echo "${usage_greeting?}, ${usage_user?}! Your message is: ${usage_message?}"

This task can be run like so:

shellmise run greet --user jdx -g "hey" "How are you?"

The options will all be passed as environment variables prefixed with usage_ like usage_user.

Help is available with mise run greet --help and will show the options defined in the task.

Completions are available like you'd expect, so typing mise run greet --greeting <tag> will show hi, hello, and hey as options.

Custom completion can be provided by a CLI. mise run greet --dir <tab> will execute find . -maxdepth 1 -type d to provide completions.

To get the autocompletion working, set up mise autocompletions.

See Tasks for more information on working with tasks.

Common Commands ​

Since there are a lot of commands available in mise, here are what I consider the most important:

mise completion – Set up completions for your shell.

mise cfg|config – A bunch of commands for working with mise.toml files via the CLI.

mise x|exec – Execute a command in the mise environment without activating mise.

mise g|generate – Generates things like git hooks, task documentation, GitHub actions, and more for your project.

mise i|install – Install tools.

mise link – Symlink a tool installed by some other means into the mise.

mise ls-remote – List all available versions of a tool.

mise ls – Lists information about installed/active tools.

mise outdated – Informs you of any tools with newer versions available.

mise plugin – Plugins can extend mise with new functionality like extra tools or environment variable management. Commonly, these are simply asdf plugins or modern plugins.

mise r|run – Run a task defined in mise.toml or mise-tasks.

mise self-update – Update mise to the latest version. Don't use this if you installed mise via a package manager.

mise settings – CLI access to get/set configuration settings.

mise rm|uninstall – Uninstall a tool.

mise up|upgrade – Upgrade tool versions.

mise u|use – Install and activate tools.

mise w|watch – Watch for changes in a project and run tasks when they occur.

Final Thoughts ​

Dev tools, env vars, and tasks work together to make managing your development environment easier—especially when working with others. The goal is to have a consistent UX to interface with projects regardless of the programming languages or tools used on it.

For further reading:

Dev Tools – A deeper overview of working with dev tools

Environments – A deeper overview of working with environment variables

Tasks – A deeper overview of working with tasks

Configuration – More information on mise.toml files

Settings – All the configuration settings available in mise

Backends – An index of all the backends available in mise

Registry – Every "shorthand" available for tools in mise like node, terraform, or watchexec which point to core:node, asdf:asdf-community/asdf-hashicorp, and aqua:watchexec/watchexec respectively

CLI – The full list of commands available in mise
