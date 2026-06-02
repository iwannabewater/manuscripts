# Home | mise-en-place

> Source: https://mise.jdx.dev/

Skip to content

mise-en-place

SearchK

Appearance

mise · pronounced "meez"

Your dev env,
already prepped.

One tool to manage languages, env vars, and tasks per project, reproducibly.

Getting StartedDemo

mise-en-place

Dev tools, env vars, and tasks in one CLI

~/projects/orders · zsh

$ cd ~/projects/orders

# mise picks up mise.toml and updates the shell

✓ node@24 active

✓ python@3.13 active

✓ terraform@1 active

✓ DATABASE_URL loaded from .env.local

$ mise run deploy

→ running task "deploy" (4 steps)

build · test · migrate · ship ...

✓ done in 42.1s

curl https://mise.run | shcopyMore install methods

The Idea

Everything in its place, before you code.

In a professional kitchen, mise en place is the ritual of prep: knives sharpened, onions diced, stock warm, station clean. The work before the work.

mise does the same for your dev env. It installs and activates the right tools, loads the right env vars, and wires up the right tasks for the commands you run.

mise en place /meez ahn plahs/

1. the gathering and arrangement of ingredients and tools before cooking.

2. a polyglot tool that keeps your project tools, env, and tasks in one place.

The Menu

One CLI for the whole project setup.
All docs

— 01🔪
Dev Tools

Install project tools, pin versions, and switch automatically as you move between directories.
read more →— 02🫕
Environments

Load project-specific environment variables from mise.toml, .env files, shell commands, and more.
read more →— 03🍳
Tasks

Define build, test, lint, and deploy commands next to the tools and env vars they need.
read more →

— pantry · 900+ tools, 1 toml file —

nodepythonrubygorustjavadenobunterraformkubectlzigswiftphpelixirnodepythonrubygorustjavadenobunterraformkubectlzigswiftphpelixir

Chef's Special

Meet aube, a fast Node.js package manager.

New from en.dev by @jdx. aube uses your existing lockfile and is ready to try in beta.

$ aube

The Recipe

Four steps to a prepped station.

01 Install mise02 Add and install tools03 Load env vars04 Define tasks

$ curl https://mise.run | sh
✓ mise installed

$ mise doctor
✓ mise is ready

$ mise use node@26 python@3.14 terraform@1
✓ wrote mise.toml

$ mise install
✓ installed 3 tools

$ cat .env.local
DATABASE_URL=postgres://localhost/orders

$ mise env -s bash
export DATABASE_URL=postgres://localhost/orders

$ mise run test
→ lint · typecheck · unit · e2e
✓ 4 tasks complete

$ mise run deploy
✓ shipped

Ready When You Are

Allez, prep your station.

curl https://mise.run | sh

Getting startedRun the demo
