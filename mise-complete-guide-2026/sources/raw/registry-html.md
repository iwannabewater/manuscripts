# Registry | mise-en-place

> Source: https://mise.jdx.dev/registry.html

Skip to content

mise-en-place

SearchK

Appearance

Menu
Return to top

Registry ​

List of all tools aliased by default in mise.

You can use these shorthands with mise use. This allows you to use a tool without needing to know the full name. For example, to use the aws-cli tool, you can do the following:

shellmise use aws-cli

instead of

shellmise use aqua:aws/aws-cli

If a tool is not available in the registry, you can install it by its full name. github and aqua give you for example access to almost all programs available on GitHub.

Backends ​

In addition to built-in core tools, mise supports a variety of backends to install tools.

Backends fall into the following acceptance tiers for new registry entries:

Tier 1 — preferred, routinely accepted:

aqua - offers the most features and security while not requiring plugins

github - for tools that are not available in the aqua registry, but are available on GitHub

gitlab - for tools that are not available in the aqua registry, but are available on GitLab

Tier 2 — high bar, but lower than tier 3:

conda - potentially accepted for tools that can't reasonably be supported via aqua/github. The bar is lower than tier 3 because mise's conda backend does not require a separately-installed package manager — packages are fetched and extracted directly from anaconda.org with no conda/mamba/micromamba needed on PATH.

Tier 3 — very high bar, rarely accepted:

pipx - only for python tools, requires python on PATH

npm - only for node tools, requires node on PATH

gem - only for ruby tools, requires ruby on PATH

go - only for go tools, requires go to be installed to compile. Because go tools can be distributed as a single binary, aqua/github are definitely preferred.

cargo - only for rust tools, requires cargo to be installed to compile. Because rust tools can be distributed as a single binary, aqua/github are definitely preferred.

dotnet - only for dotnet tools, requires dotnet to be installed to compile. Because dotnet tools can be distributed as a single binary, aqua/github are definitely preferred.

These all depend on a separately-installed runtime/toolchain on PATH, which is fragile — npm/pipx/gem in particular silently bind tools to whichever node/python/ruby happened to be on PATH at install time.

Not accepted:

New vfox and asdf tools are not accepted for supply-chain security reasons — use aqua (preferred) or github instead.

The ubi backend is deprecated and is not accepted for new registry entries.

Users can still install via any backend themselves with explicit syntax (mise use vfox:owner/repo, mise use cargo:name, etc.) — they just don't get a registry shorthand for it.

Backends Priority ​

Each tool can define its own priority if it has more than one backend it supports. If you would like to disable a backend, you can do so with the following command:

shellmise settings disable_backends=asdf

This will disable the asdf backend. See Aliases for a way to set a default backend for a tool. Note that the asdf backend is disabled by default on Windows.

You can also specify the full name for a tool using mise use aqua:1password/cli if you want to use a specific backend.

Environment Variable Overrides ​

You can override the backend for any tool using environment variables with the pattern MISE_BACKENDS_<TOOL>. This takes the highest priority and overrides any registry or alias configuration:

shell# Use vfox backend for php
export MISE_BACKENDS_PHP='vfox:mise-plugins/vfox-php'
mise install php@latest

The tool name in the environment variable should be in SHOUTY_SNAKE_CASE (uppercase with underscores). For example, my-tool becomes MISE_BACKENDS_MY_TOOL.

Source: https://github.com/jdx/mise/blob/main/registry/

Tools ​

Note that mise registry can be used to list all tools in the registry. mise use without any arguments will show a tui to select a tool to install.

ShortFullOS

1passwordvfox:mise-plugins/vfox-1password
aqua:1password/cli

aapt2vfox:mise-plugins/vfox-aapt2

acliaqua:atlassian.com/aclilinux, macos

actaqua:nektos/act
asdf:gr1m0h/asdf-act

action-validatoraqua:mpalmer/action-validator
asdf:mpalmer/action-validator
cargo:action-validatorlinux, macos

actionlintaqua:rhysd/actionlint
asdf:crazy-matt/asdf-actionlint
go:github.com/rhysd/actionlint/cmd/actionlint

adr-toolsaqua:npryce/adr-tools
asdf:https://gitlab.com/td7x/asdf/adr-tools

agvfox:mise-plugins/vfox-ag
asdf:mise-plugins/mise-ag

ageaqua:FiloSottile/age
asdf:threkk/asdf-age

age-plugin-yubikeygithub:str4d/age-plugin-yubikey
asdf:joke/asdf-age-plugin-yubikey
cargo:age-plugin-yubikey

ageboxaqua:slok/agebox
asdf:slok/asdf-agebox

aichataqua:sigoden/aichat

airaqua:air-verse/air
asdf:pdemagny/asdf-air

aks-engineaqua:Azure/aks-engine
asdf:robsonpeixoto/asdf-aks-engine

alluregithub:allure-framework/allure2
asdf:mise-plugins/mise-allure

allurectlgithub:allure-framework/allurectl

alpaqua:tkuchiki/alp
asdf:asdf-community/asdf-alp

amassgithub:owasp-amass/amass
asdf:dhoeric/asdf-amass

amazon-ecr-credential-helperaqua:awslabs/amazon-ecr-credential-helper
asdf:dex4er/asdf-amazon-ecr-credential-helper

amazon-ecs-cliaqua:aws/amazon-ecs-cli

ampnpm:@ampcode/cli

android-sdkvfox:mise-plugins/vfox-android-sdk

ansiblepipx:ansible

ansible-corepipx:ansible-core

antvfox:mise-plugins/vfox-ant

apkoaqua:chainguard-dev/apko
asdf:omissis/asdf-apko

apollo-iosgithub:apollographql/apollo-iosmacos

apollo-routergithub:apollographql/router
asdf:safx/asdf-apollo-router

apollo-rovergithub:apollographql/rover

aquagithub:aquaproj/aqua

arduinoaqua:arduino/arduino-cli
asdf:egnor/asdf-arduino-cli

argcgithub:sigoden/argc

argoaqua:argoproj/argo-workflows
asdf:sudermanjr/asdf-argo

argo-rolloutsaqua:argoproj/argo-rollouts
asdf:abatilo/asdf-argo-rollouts

argocdaqua:argoproj/argo-cd
asdf:beardix/asdf-argocd

asciidoctorjvfox:mise-plugins/vfox-asciidoctorj
asdf:mise-plugins/mise-asciidoctorj

asshgithub:moul/assh
asdf:mise-plugins/mise-assh

ast-grepaqua:ast-grep/ast-grep
cargo:ast-grep
pipx:ast-grep-cli

astrogithub:astronomer/astro-cli

atlasaqua:ariga/atlas
asdf:komi1230/asdf-atlas

atlas-communityaqua:ariga/atlas/community

atmosaqua:cloudposse/atmos
asdf:cloudposse/asdf-atmos

atuinaqua:atuinsh/atuin
cargo:atuin

aubegithub:endevco/aube
cargo:aube

auto-docgithub:tj-actions/auto-doc
asdf:mise-plugins/mise-auto-doc

aws-amplifygithub:aws-amplify/amplify-cli
asdf:LozanoMatheus/asdf-aws-amplify-cli

aws-cliaqua:aws/aws-cli
asdf:MetricMike/asdf-awsclilinux, macos

aws-copilotaqua:aws/copilot-cli
asdf:NeoHsu/asdf-copilot

aws-iam-authenticatoraqua:kubernetes-sigs/aws-iam-authenticator
asdf:zekker6/asdf-aws-iam-authenticator

aws-nukeaqua:ekristen/aws-nuke
asdf:bersalazar/asdf-aws-nuke

aws-samaqua:aws/aws-sam-cli
pipx:aws-sam-cli
asdf:mise-plugins/mise-pyapp

aws-ssoaqua:synfinatic/aws-sso-cli
asdf:adamcrews/asdf-aws-sso-cli

aws-vaultaqua:ByteNess/aws-vault

awscli-localpipx:awscli-local

awsebclipipx:awsebcli
asdf:mise-plugins/mise-pyapp

awslsgithub:jckuester/awsls
asdf:chessmango/asdf-awsls

awsrmgithub:jckuester/awsrm
asdf:chessmango/asdf-awsrm

awsweepergithub:jckuester/awsweeper
asdf:chessmango/asdf-awsweeper

azdaqua:Azure/azure-dev

azurepipx:azure-cli

azure-functions-core-toolsvfox:mise-plugins/vfox-azure-functions-core-tools
asdf:mise-plugins/mise-azure-functions-core-tools

azure-kubeloginaqua:Azure/kubelogin
asdf:sechmann/asdf-kubelogin

babashkagithub:babashka/babashka
asdf:pitch-io/asdf-babashka

balenagithub:balena-io/balena-cli
asdf:jaredallard/asdf-balena-cli

bashbotaqua:mathew-fleisch/bashbot
asdf:mathew-fleisch/asdf-bashbot

bashlygem:bashly

bataqua:sharkdp/bat
cargo:bat
asdf:https://gitlab.com/wt0f/asdf-bat

bat-extrasaqua:eth-p/bat-extras
asdf:mise-plugins/mise-bat-extras

batsaqua:bats-core/bats-core
asdf:timgluz/asdf-batslinux, macos

bazelaqua:bazelbuild/bazel
asdf:rajatvig/asdf-bazel

bazel-watcheraqua:bazelbuild/bazel-watcher

bazeliskaqua:bazelbuild/bazelisk
npm:@bazel/bazelisk
asdf:josephtate/asdf-bazelisk

betterleaksaqua:betterleaks/betterleaks
github:betterleaks/betterleaks

bfsvfox:mise-plugins/vfox-bfs
asdf:mise-plugins/mise-bfs

bibtex-tidynpm:bibtex-tidy

binnacleaqua:Traackr/binnacle
asdf:Traackr/asdf-binnacle

biomeaqua:biomejs/biome
npm:@biomejs/biome

bitwardenaqua:bitwarden/clients
asdf:vixus0/asdf-bitwarden

bitwarden-secrets-manageraqua:bitwarden/sdk-sm
github:bitwarden/sdk
asdf:asdf-community/asdf-bitwarden-secrets-manager

blackaqua:psf/black

blenderaqua:blender/blender

bobaqua:MordechaiHadad/bob
cargo:bob-nvim

boilerplateaqua:gruntwork-io/boilerplate

bombardieraqua:codesenberg/bombardier
asdf:NeoHsu/asdf-bombardier

borgaqua:borgbackup/borg
asdf:lwiechec/asdf-borg

boshaqua:cloudfoundry/bosh-cli
asdf:mise-plugins/tanzu-plug-in-for-asdf

bottomaqua:ClementTsang/bottom
asdf:carbonteq/asdf-btm
cargo:bottom

boundaryaqua:hashicorp/boundary
asdf:mise-plugins/mise-hashicorp

bpkgvfox:mise-plugins/vfox-bpkg
asdf:mise-plugins/mise-bpkg

btopaqua:aristocratos/btop

buck2aqua:facebook/buck2
github:facebook/buck2

bufaqua:bufbuild/buf
asdf:truepay/asdf-buf

buildifieraqua:bazelbuild/buildtools/buildifier

buildpackaqua:buildpacks/pack
asdf:johnlayton/asdf-buildpack

buncore:bun

cabalaqua:haskell/cabal/cabal-install

caddyaqua:caddyserver/caddy
asdf:salasrod/asdf-caddy

calendarsyncaqua:inovex/CalendarSync
asdf:FeryET/asdf-calendarsync

calicoctlaqua:projectcalico/calico/calicoctl
asdf:TheCubicleJockey/asdf-calicoctl

carapaceaqua:carapace-sh/carapace-bin

cargo-binstallaqua:cargo-bins/cargo-binstall
cargo:cargo-binstall

cargo-distaqua:axodotdev/cargo-dist
github:axodotdev/cargo-dist
cargo:cargo-dist

cargo-instaaqua:mitsuhiko/insta
cargo:insta

cargo-makeaqua:sagiegurari/cargo-make
asdf:mise-plugins/asdf-cargo-make
cargo:cargo-make

carthagevfox:mise-plugins/vfox-carthage
asdf:mise-plugins/mise-carthagemacos

ccachegithub:ccache/ccache
asdf:asdf-community/asdf-ccache

certstrapgithub:square/certstrap
asdf:carnei-ro/asdf-certstrap

cfgithub:cloudfoundry/cli
asdf:mise-plugins/mise-cf

cfn-lintpipx:cfn-lint

cfsslaqua:cloudflare/cfssl/cfssl
asdf:mathew-fleisch/asdf-cfssl

cfssljsonaqua:cloudflare/cfssl/cfssljson

chamberaqua:segmentio/chamber
asdf:mintel/asdf-chamber

changieaqua:miniscruff/changie
asdf:pdemagny/asdf-changie

cheataqua:cheat/cheat
asdf:jmoratilla/asdf-cheat-plugin

checkmakeaqua:checkmake/checkmake

checkovaqua:bridgecrewio/checkov
asdf:bosmak/asdf-checkov

chezmoiaqua:twpayne/chezmoi
asdf:joke/asdf-chezmoi

chezschemevfox:mise-plugins/vfox-chezscheme
asdf:mise-plugins/mise-chezscheme

chickenvfox:mise-plugins/vfox-chickenlinux, macos, freebsd, openbsd

chiselaqua:jpillora/chisel
go:github.com/jpillora/chisel
asdf:lwiechec/asdf-chisel

chooseaqua:theryangeary/choose
cargo:choose
asdf:carbonteq/asdf-choose

chromedrivervfox:mise-plugins/vfox-chromedriver
asdf:mise-plugins/mise-chromedriver

cidr-mergergithub:zhanhb/cidr-merger
asdf:ORCID/asdf-cidr-merger

cidrchkgithub:mhausenblas/cidrchk
asdf:ORCID/asdf-cidrchk

cilium-cliaqua:cilium/cilium-cli
asdf:carnei-ro/asdf-cilium-cli

cilium-hubbleaqua:cilium/hubble
github:cilium/hubble
asdf:NitriKx/asdf-cilium-hubble

circleciaqua:CircleCI-Public/circleci-cli
asdf:ucpr/asdf-circleci-cli

clangconda:clang
asdf:mise-plugins/mise-llvm
vfox:mise-plugins/vfox-clang

clang-formatconda:clang-format
asdf:mise-plugins/mise-llvm

claudeaqua:anthropics/claude-code
http:claudelinux, macos, windows

claude-powerlinenpm:@owloops/claude-powerline

claude-squadaqua:smtg-ai/claude-squad

clickhousevfox:mise-plugins/vfox-clickhouse
asdf:mise-plugins/mise-clickhouse

clj-kondogithub:clj-kondo/clj-kondo
asdf:rynkowsg/asdf-clj-kondo

cljstylegithub:greglook/cljstyle
asdf:abogoyavlensky/asdf-cljstylelinux, macos

clojureasdf:mise-plugins/mise-clojure

cloud-sql-proxyaqua:GoogleCloudPlatform/cloud-sql-proxy
asdf:pbr0ck3r/asdf-cloud-sql-proxy

cloudflaredaqua:cloudflare/cloudflared
asdf:threkk/asdf-cloudflared

clusterawsadmgithub:kubernetes-sigs/cluster-api-provider-aws
asdf:kahun/asdf-clusterawsadm

clusterctlaqua:kubernetes-sigs/cluster-api
asdf:pfnet-research/asdf-clusterctl

cmakeaqua:Kitware/CMake
asdf:mise-plugins/mise-cmake
vfox:mise-plugins/vfox-cmake

cmctlaqua:cert-manager/cmctl
asdf:asdf-community/asdf-cmctl

cmdxaqua:suzuki-shunsuke/cmdx

cockroachaqua:cockroachdb/cockroach
asdf:salasrod/asdf-cockroach

cocoapodsgem:cocoapodsmacos

cocogittoaqua:cocogitto/cocogitto

codeaqua:just-every/code

code-review-graphpipx:code-review-graph

codebuffnpm:codebuff

codefreshgithub:codefresh-io/cli
asdf:gurukulkarni/asdf-codefresh

codeqlgithub:github/codeql-cli-binaries
asdf:mise-plugins/mise-codeql

coderaqua:coder/coder
asdf:mise-plugins/asdf-coder

codexaqua:openai/codex
npm:@openai/codex

codongithub:exaloop/codonlinux, macos

colimaaqua:abiosoft/colima
asdf:CrouchingMuppet/asdf-colima

committedaqua:crate-ci/committed

communiquegithub:jdx/communique

conanpipx:conan
asdf:mise-plugins/mise-pyapp

conformaqua:siderolabs/conform
asdf:skyzyx/asdf-conformlinux, macos

conftestaqua:open-policy-agent/conftest
asdf:looztra/asdf-conftest

consulaqua:hashicorp/consul
asdf:mise-plugins/mise-hashicorp

containeraqua:apple/containermacos

container-structure-testaqua:GoogleContainerTools/container-structure-test
asdf:FeryET/asdf-container-structure-test

container-useaqua:dagger/container-use

cookiecutterpipx:cookiecutter
asdf:shawon-crosen/asdf-cookiecutter

copierpipx:copier
asdf:looztra/asdf-copier

copilotaqua:github/copilot-cli
github:github/copilot-cli
npm:@github/copilot

corednsgithub:coredns/coredns
asdf:s3than/asdf-coredns

coreutilsaqua:uutils/coreutils

cosignaqua:sigstore/cosign
asdf:https://gitlab.com/wt0f/asdf-cosign

coursiergithub:coursier/coursier
asdf:jiahuili430/asdf-coursier

cowsaynpm:cowsay

cpzaqua:SUPERCILEX/fuc/cpz

craneaqua:google/go-containerregistry
asdf:dmpe/asdf-crane

crictlaqua:kubernetes-sigs/cri-tools/crictl
asdf:FairwindsOps/asdf-crictl

crocaqua:schollz/croc

crossplaneaqua:crossplane/crossplane
asdf:joke/asdf-crossplane-cli

crushaqua:charmbracelet/crush

crystalgithub:crystal-lang/crystal
asdf:mise-plugins/mise-crystal
vfox:mise-plugins/vfox-crystal

cspellnpm:cspell

ctlptlaqua:tilt-dev/ctlptl
asdf:ezcater/asdf-ctlptl

ctopaqua:bcicen/ctop
asdf:NeoHsu/asdf-ctop

cueaqua:cue-lang/cue
asdf:asdf-community/asdf-cue

curlieaqua:rs/curlie

cyclonedxaqua:CycloneDX/cyclonedx-cli
asdf:xeedio/asdf-cyclonedx

d2aqua:terrastruct/d2
github:terrastruct/d2

daggeraqua:dagger/dagger
asdf:virtualstaticvoid/asdf-dagger

daguaqua:dagu-org/dagu

danger-jsnpm:danger

danger-swiftspm:danger/swift

dapraqua:dapr/cli
asdf:asdf-community/asdf-dapr-cli

darthttp:dart
asdf:mise-plugins/mise-dart
vfox:mise-plugins/vfox-dart

daselaqua:TomWright/dasel
asdf:asdf-community/asdf-dasel

databricks-cliaqua:databricks/cli
github:databricks/cli

daytonagithub:daytonaio/daytona
asdf:mise-plugins/mise-daytona

dbmateaqua:amacneil/dbmate
asdf:juusujanar/asdf-dbmate

dbt-fusionaqua:getdbt.com/dbt-fusion

deckaqua:Kong/deck
asdf:nutellinoit/asdf-deck

deltaaqua:dandavison/delta
asdf:andweeb/asdf-delta
cargo:git-delta

denocore:deno

dependency-checkaqua:dependency-check/DependencyCheck

depotgithub:depot/cli
asdf:depot/asdf-depot

deskaqua:jamesob/desk
asdf:endorama/asdf-desklinux, macos

devcontainer-clinpm:@devcontainers/cli

devspaceaqua:devspace-sh/devspace
asdf:NeoHsu/asdf-devspace

dhallaqua:dhall-lang/dhall-haskell
asdf:mise-plugins/mise-dhall

diffociaqua:reproducible-containers/diffoci

difftasticaqua:Wilfred/difftastic
asdf:volf52/asdf-difftastic
cargo:difftastic

direnvaqua:direnv/direnv
asdf:asdf-community/asdf-direnv

diveaqua:wagoodman/dive
asdf:looztra/asdf-dive

docker-cliaqua:docker/cli

docker-composeaqua:docker/compose

docker-slimaqua:mintoolkit/mint
asdf:xataz/asdf-docker-slimlinux, macos

dockleaqua:goodwithtech/dockle
asdf:mathew-fleisch/asdf-dockle

doctlaqua:digitalocean/doctl
asdf:maristgeek/asdf-doctl

docuumaqua:stepchowfun/docuum
cargo:docuum
asdf:bradym/asdf-docuum

doggoaqua:mr-karan/doggo

dopplergithub:DopplerHQ/cli
asdf:takutakahashi/asdf-doppler

dotenv-linteraqua:dotenv-linter/dotenv-linter
asdf:wesleimp/asdf-dotenv-linter
cargo:dotenv-linter

dotenvxaqua:dotenvx/dotenvx

dotnetcore:dotnet
vfox:mise-plugins/vfox-dotnet
asdf:mise-plugins/mise-dotnet

dotslashgithub:facebook/dotslash

dprintaqua:dprint/dprint
asdf:asdf-community/asdf-dprint

driftctlaqua:snyk/driftctl
asdf:nlamirault/asdf-driftctl

droneaqua:harness/drone-cli
asdf:virtualstaticvoid/asdf-drone

dtaqua:so-dang-cool/dt
asdf:so-dang-cool/asdf-dt

duaaqua:Byron/dua-cli
cargo:dua-cli

duckdbaqua:duckdb/duckdb

dufaqua:muesli/duf
asdf:NeoHsu/asdf-duf

dustaqua:bootandy/dust
asdf:looztra/asdf-dust
cargo:du-dust

dvcpipx:dvc

dyffaqua:homeport/dyff
asdf:https://gitlab.com/wt0f/asdf-dyff

dynatrace-monacogithub:Dynatrace/dynatrace-configuration-as-code
asdf:nsaputro/asdf-monaco

e1saqua:keidarcy/e1s
asdf:tbobm/asdf-e1s

earthlyaqua:earthly/earthly
asdf:YR-ZR0/asdf-earthly

ecspressoaqua:kayac/ecspresso
asdf:kayac/asdf-ecspresso

editaqua:microsoft/edit

editorconfig-checkeraqua:editorconfig-checker/editorconfig-checker
asdf:gabitchov/asdf-editorconfig-checker

ejsonaqua:Shopify/ejson
asdf:cipherstash/asdf-ejson

eksctlaqua:eksctl-io/eksctl
asdf:elementalvoid/asdf-eksctl

elasticsearchasdf:mise-plugins/mise-elasticsearch

elixircore:elixir

elixir-lsaqua:elixir-lsp/elixir-ls
asdf:mise-plugins/mise-elixir-ls

elmgithub:elm/compiler
asdf:asdf-community/asdf-elm

emsdkasdf:mise-plugins/mise-emsdk

entireio-cliaqua:entireio/cli
github:entireio/cli
go:github.com/entireio/cli/cmd/entirelinux, macos

envsubstaqua:a8m/envsubst
asdf:dex4er/asdf-envsubst

erlangcore:erlang

escaqua:pulumi/esc
asdf:fxsalazar/asdf-esc

etcdaqua:etcd-io/etcd
asdf:particledecay/asdf-etcd
vfox:mise-plugins/vfox-etcd

evansaqua:ktr0731/evans
asdf:goki90210/asdf-evans

expertaqua:expert-lsp/expert
github:expert-lsp/expert

ezaaqua:eza-community/eza
asdf:mise-plugins/mise-eza
cargo:eza

fastfetchaqua:fastfetch-cli/fastfetch

fdaqua:sharkdp/fd
asdf:https://gitlab.com/wt0f/asdf-fd
cargo:fd-find

ffmpegconda:ffmpeg
asdf:mise-plugins/mise-ffmpeg

figma-exportgithub:RedMadRobot/figma-export
asdf:younke/asdf-figma-exportmacos

fillinaqua:itchyny/fillin
asdf:ouest/asdf-fillin

firebaseaqua:firebase/firebase-tools
npm:firebase-tools
asdf:jthegedus/asdf-firebase

fissionaqua:fission/fission
asdf:virtualstaticvoid/asdf-fission

flamingogithub:flux-subsystem-argo/flamingo
asdf:log2/asdf-flamingo

flatcgithub:google/flatbuffers
asdf:TheOpenDictionary/asdf-flatc

flutterhttp:flutter
asdf:mise-plugins/mise-flutter
vfox:mise-plugins/vfox-flutter

fluttergengithub:FlutterGen/flutter_gen
asdf:FlutterGen/asdf-fluttergenlinux, macos

flux-operatoraqua:controlplaneio-fluxcd/flux-operator

flux-operator-mcpaqua:controlplaneio-fluxcd/flux-operator/flux-operator-mcp

flux2aqua:fluxcd/flux2
asdf:tablexi/asdf-flux2

flyaqua:concourse/concourse/fly
asdf:mise-plugins/tanzu-plug-in-for-asdf

flyctlaqua:superfly/flyctl
asdf:chessmango/asdf-flyctl

flywaygithub:flyway/flyway
asdf:mise-plugins/mise-flyway

fnoxgithub:jdx/fnox

foundryaqua:foundry-rs/foundry

func-egithub:tetratelabs/func-e
asdf:mise-plugins/mise-func-e

furyctlgithub:sighupio/furyctl
asdf:sighupio/asdf-furyctllinux, macos

fxaqua:antonmedv/fx
asdf:https://gitlab.com/wt0f/asdf-fx

fzfaqua:junegunn/fzf
asdf:kompiro/asdf-fzf

gallery-dlpipx:gallery-dl

gamgithub:GAM-team/GAM
asdf:offbyone/asdf-gam

gatoraqua:open-policy-agent/gatekeeper
asdf:MxNxPx/asdf-gator

gcc-arm-none-eabiasdf:mise-plugins/mise-gcc-arm-none-eabi

gcloudvfox:mise-plugins/vfox-gcloud
asdf:mise-plugins/mise-gcloud

gduaqua:dundee/gdu

gemini-clinpm:@google/gemini-cli

getenvoygithub:tetratelabs-attic/getenvoy
asdf:mise-plugins/mise-getenvoy

ggshieldaqua:GitGuardian/ggshield
pipx:ggshield

ghalintaqua:suzuki-shunsuke/ghalint

ghcconda:ghc
asdf:mise-plugins/mise-ghcup

ghcupaqua:haskell/ghcup-hs
asdf:mise-plugins/mise-ghcuplinux, macos

ghorgaqua:gabrie30/ghorg
asdf:gbloquel/asdf-ghorg

ghqaqua:x-motemen/ghq
asdf:kajisha/asdf-ghq

ginkgogo:github.com/onsi/ginkgo/v2/ginkgo
asdf:mise-plugins/mise-ginkgo

git-chglogaqua:git-chglog/git-chglog
asdf:GoodwayGroup/asdf-git-chglog

git-cliffaqua:orhun/git-cliff
asdf:jylenhof/asdf-git-cliff

git-filter-repopipx:git-filter-repo

git-lfsaqua:git-lfs/git-lfs

gitconfiggithub:0ghny/gitconfig
asdf:0ghny/asdf-gitconfig

github-cliaqua:cli/cli
asdf:bartlomiejdanek/asdf-github-cli

github-markdown-tocaqua:ekalinin/github-markdown-toc
asdf:skyzyx/asdf-github-markdown-toc

gitleaksaqua:gitleaks/gitleaks
asdf:jmcvetta/asdf-gitleaks

gitsignaqua:sigstore/gitsign
asdf:spencergilbert/asdf-gitsignlinux, macos

gituaqua:altsem/gitu
cargo:gitu

gituiaqua:extrawurst/gitui
asdf:looztra/asdf-gitui
cargo:gitui

gitversionaqua:gittools/gitversion

glabgitlab:gitlab-org/cli
gitlab:gitlab-org/cli
asdf:mise-plugins/mise-glab

gleamaqua:gleam-lang/gleam
asdf:asdf-community/asdf-gleam

glooctlgithub:solo-io/gloo
asdf:halilkaya/asdf-glooctl

glowaqua:charmbracelet/glow
asdf:mise-plugins/asdf-glow

gocore:go

go-containerregistryaqua:google/go-containerregistry
asdf:dex4er/asdf-go-containerregistry

go-getteraqua:hashicorp/go-getter
asdf:mise-plugins/mise-go-getter

go-jiraaqua:go-jira/jira
asdf:dguihal/asdf-go-jira

go-jsonnetaqua:google/go-jsonnet
asdf:https://gitlab.com/craigfurman/asdf-go-jsonnet

go-junit-reportaqua:jstemmer/go-junit-report
asdf:jwillker/asdf-go-junit-report

go-swaggeraqua:go-swagger/go-swagger
asdf:jfreeland/asdf-go-swaggerlinux, macos

goconveygo:github.com/smartystreets/goconvey
asdf:mise-plugins/mise-goconvey

gocryptfsaqua:rfjakob/gocryptfs

godotaqua:godotengine/godot

gofumptaqua:mvdan/gofumpt
asdf:looztra/asdf-gofumpt

gojqaqua:itchyny/gojq
asdf:jimmidyson/asdf-gojq
go:github.com/itchyny/gojq/cmd/gojq

gokeyaqua:cloudflare/gokey

golangci-lintaqua:golangci/golangci-lint
asdf:hypnoglow/asdf-golangci-lint

golangci-lint-langserveraqua:nametake/golangci-lint-langserver
go:github.com/nametake/golangci-lint-langserver

golinesaqua:segmentio/golines
go:github.com/segmentio/golines

gomigrateaqua:golang-migrate/migrate
asdf:joschi/asdf-gomigrate

gomplateaqua:hairyhenderson/gomplate
asdf:sneakybeaky/asdf-gomplate

google-java-formataqua:google/google-java-format

gopassaqua:gopasspw/gopass
asdf:trallnag/asdf-gopass

goreleaseraqua:goreleaser/goreleaser
asdf:kforsthoevel/asdf-goreleaser

gossaqua:goss-org/goss
asdf:raimon49/asdf-goss

gotestsumaqua:gotestyourself/gotestsum
asdf:pmalek/mise-gotestsum

gpingaqua:orf/gping
github:orf/gping
cargo:gping

graalvmasdf:mise-plugins/mise-graalvm

gradleaqua:gradle/gradle
vfox:mise-plugins/vfox-gradle

grafana-kubernetes-pluginaqua:ricoberger/grafana-kubernetes-plugin

grantedaqua:fwdcloudsec/granted
asdf:dex4er/asdf-granted

graphitegithub:withgraphite/homebrew-tap
npm:@withgraphite/graphite-cli

grexaqua:pemistahl/grex
asdf:ouest/asdf-grex
cargo:grex

gronaqua:tomnomnom/gron

groovyasdf:mise-plugins/mise-groovy
vfox:mise-plugins/vfox-groovy

grpc-health-probeaqua:grpc-ecosystem/grpc-health-probe
asdf:zufardhiyaulhaq/asdf-grpc-health-probelinux, macos

grpcurlaqua:fullstorydev/grpcurl
asdf:asdf-community/asdf-grpcurl

grypeaqua:anchore/grype
asdf:poikilotherm/asdf-grype

gsudogithub:gerardog/gsudowindows

gumaqua:charmbracelet/gum
asdf:lwiechec/asdf-gum

gupaqua:nao1215/gup

gwvaultaqua:GoodwayGroup/gwvault
asdf:GoodwayGroup/asdf-gwvault

hadolintaqua:hadolint/hadolint
asdf:devlincashman/asdf-hadolint

harper-cliaqua:Automattic/harper/harper-cli

harper-lsaqua:Automattic/harper/harper-ls

hasaqua:kdabir/has
asdf:sylvainmetayer/asdf-haslinux, macos

hasura-cliaqua:hasura/graphql-engine
asdf:gurukulkarni/asdf-hasura

hatchpipx:hatch

haxegithub:HaxeFoundation/haxe
asdf:mise-plugins/mise-haxe

hcl2jsonaqua:tmccombs/hcl2json
asdf:dex4er/asdf-hcl2json

hcloudaqua:hetznercloud/cli
asdf:chessmango/asdf-hcloud

helixaqua:helix-editor/helix

helmaqua:helm/helm
asdf:Antiarchitect/asdf-helm

helm-craqua:helm/chart-releaser
asdf:Antiarchitect/asdf-helm-cr

helm-ctaqua:helm/chart-testing
asdf:tablexi/asdf-helm-ct

helm-diffgithub:databus23/helm-diff
asdf:mise-plugins/mise-helm-diff

helm-docsaqua:norwoodj/helm-docs
asdf:sudermanjr/asdf-helm-docs

helm-lsaqua:mrjosh/helm-ls

helmfileaqua:helmfile/helmfile
asdf:feniix/asdf-helmfile

helmsmangithub:Praqma/helmsman
asdf:luisdavim/asdf-helmsman

helmwaveaqua:helmwave/helmwave

herdrgithub:ogulcancelik/herdr

herokunpm:heroku

hexylaqua:sharkdp/hexyl
cargo:hexyl

hishtorygithub:ddworken/hishtory
asdf:asdf-community/asdf-hishtory

hivemindgithub:DarthSim/hivemind
go:github.com/DarthSim/hivemind

hkaqua:jdx/hk

hledgergithub:simonmichael/hledger
asdf:airtonix/asdf-hledger

hledger-flowgithub:apauley/hledger-flow
asdf:airtonix/asdf-hledger-flow

hlintgithub:ndmitchell/hlint

hostctlaqua:guumaster/hostctl
asdf:svenluijten/asdf-hostctl

htmlqaqua:mgdm/htmlq
cargo:htmlq

httpie-goaqua:nojima/httpie-go
asdf:abatilo/asdf-httpie-golinux, macos

hubaqua:mislav/hub
asdf:mise-plugins/asdf-hub

hugoaqua:gohugoio/hugo
asdf:NeoHsu/asdf-hugo
asdf:nklmilojevic/asdf-hugo

hugo-extendedaqua:gohugoio/hugo/hugo-extended

hunkaqua:modem-dev/hunk
github:modem-dev/hunk

hurlaqua:Orange-OpenSource/hurl
asdf:raimon49/asdf-hurl
cargo:hurl

hwatchaqua:blacknon/hwatch
asdf:chessmango/asdf-hwatch

hygengithub:jondot/hygen
asdf:brentjanderson/asdf-hygen

hyperfineaqua:sharkdp/hyperfine
asdf:volf52/asdf-hyperfine
cargo:hyperfine

iam-policy-json-to-terraformaqua:flosell/iam-policy-json-to-terraform
asdf:carlduevel/asdf-iam-policy-json-to-terraform

iamliveaqua:iann0036/iamlive
asdf:chessmango/asdf-iamlive

ibmcloudaqua:IBM-Cloud/ibm-cloud-cli-release

imagemagickconda:imagemagick
asdf:mise-plugins/mise-imagemagick

imgpkgaqua:carvel-dev/imgpkg
asdf:vmware-tanzu/asdf-carvel

infisicalgithub:Infisical/cli

infracostaqua:infracost/infracost
asdf:dex4er/asdf-infracost

istioctlaqua:istio/istio/istioctl
asdf:virtualstaticvoid/asdf-istioctl

janetgithub:janet-lang/janet

jaqaqua:01mf02/jaq
cargo:jaq

javacore:java

jbangaqua:jbangdev/jbang
asdf:mise-plugins/jbang-asdf

jcaqua:kellyjonbrazil/jc
pipx:jc

jdaqua:josephburnett/jd
go:github.com/josephburnett/jd

jfrog-cliconda:jfrog-cli
asdf:mise-plugins/mise-jfrog-cli

jibasdf:mise-plugins/mise-jib

jiqaqua:fiatjaf/jiq
asdf:chessmango/asdf-jiq

jjaqua:jj-vcs/jj
cargo:jj-cli

jjuiaqua:idursun/jjui

jlessaqua:PaulJuliusMartinez/jless
asdf:jc00ke/asdf-jless
cargo:jless

jmespathaqua:jmespath/jp
asdf:skyzyx/asdf-jmespath

jnvaqua:ynqa/jnv
asdf:raimon49/asdf-jnv

jqaqua:jqlang/jq
asdf:mise-plugins/asdf-jq

jqpaqua:noahgorstein/jqp
asdf:https://gitlab.com/wt0f/asdf-jqp

jreleaseraqua:jreleaser/jreleaser
asdf:joschi/asdf-jreleaser

json5npm:json5

jsonnet-bundleraqua:jsonnet-bundler/jsonnet-bundler
asdf:beardix/asdf-jb

jsonschemaaqua:sourcemeta/jsonschema

julesnpm:@google/jules

juliahttp:julia
asdf:mise-plugins/mise-julia

justaqua:casey/just
asdf:olofvndrhr/asdf-just
cargo:just

jwtaqua:mike-engel/jwt-cli
cargo:jwt-cli

jwtuigithub:jwt-rs/jwt-ui
cargo:jwt-ui

jxaqua:jenkins-x/jx
asdf:vbehar/asdf-jx

k0sctlaqua:k0sproject/k0sctl
asdf:Its-Alex/asdf-plugin-k0sctl

k2tfaqua:sl1pm4t/k2tf
asdf:carlduevel/asdf-k2tf

k3daqua:k3d-io/k3d
asdf:spencergilbert/asdf-k3d

k3kcligithub:rancher/k3k
asdf:xanmanning/asdf-k3kcli

k3saqua:k3s-io/k3s
asdf:mise-plugins/mise-k3s

k3supaqua:alexellis/k3sup
asdf:cgroschupp/asdf-k3sup

k6aqua:grafana/k6
asdf:gr1m0h/asdf-k6

k9saqua:derailed/k9s
asdf:looztra/asdf-k9s

kafkactlaqua:deviceinsight/kafkactl
asdf:anweber/asdf-kafkactl

kappaqua:carvel-dev/kapp
asdf:vmware-tanzu/asdf-carvel

kbldaqua:carvel-dev/kbld
asdf:vmware-tanzu/asdf-carvel

kclaqua:kcl-lang/cli
asdf:mise-plugins/mise-kcl

kconfaqua:particledecay/kconf
asdf:particledecay/asdf-kconf

killportaqua:jkfran/killport
cargo:killport

kindaqua:kubernetes-sigs/kind
asdf:johnlayton/asdf-kind

kiotaaqua:microsoft/kiota
asdf:asdf-community/asdf-kiota

kiro-cliaqua:kiro.dev/kiro-clilinux, macos

knaqua:knative/client
asdf:joke/asdf-kn

koaqua:ko-build/ko
asdf:zasdaym/asdf-ko

kokagithub:koka-lang/koka
asdf:susurri/asdf-koka

komposeaqua:kubernetes/kompose
asdf:technikhil314/asdf-kompose

kopiaaqua:kopia/kopia
github:kopia/kopia

kopsaqua:kubernetes/kops
asdf:Antiarchitect/asdf-kops

kotlingithub:JetBrains/kotlin
asdf:mise-plugins/mise-kotlin
vfox:mise-plugins/vfox-kotlin

kptaqua:kptdev/kpt
asdf:nlamirault/asdf-kptlinux, macos

krewaqua:kubernetes-sigs/krew
asdf:bjw-s/asdf-krew

kscriptgithub:kscripting/kscript
asdf:edgelevel/asdf-kscript

ksopsaqua:viaduct-ai/kustomize-sops
asdf:janpieper/asdf-ksops

ktlintaqua:pinterest/ktlint
asdf:mise-plugins/mise-ktlint

kube-capacityaqua:robscott/kube-capacity
asdf:looztra/asdf-kube-capacity

kube-controller-toolsgithub:kubernetes-sigs/controller-tools
asdf:jimmidyson/asdf-kube-controller-tools

kube-linteraqua:stackrox/kube-linter
asdf:devlincashman/asdf-kube-linter

kube-scoreaqua:zegl/kube-score
asdf:bageljp/asdf-kube-score

kubebuilderaqua:kubernetes-sigs/kubebuilder
asdf:virtualstaticvoid/asdf-kubebuilder

kubecmaqua:sunny0826/kubecm
asdf:samhvw8/asdf-kubecm

kubecoloraqua:kubecolor/kubecolor
asdf:dex4er/asdf-kubecolor

kubeconformaqua:yannh/kubeconform
asdf:lirlia/asdf-kubeconform

kubectlaqua:kubernetes/kubernetes/kubectl
asdf:asdf-community/asdf-kubectl

kubectl-convertaqua:kubernetes/kubernetes/kubectl-convert
asdf:iul1an/asdf-kubectl-convert

kubectl-kotsaqua:replicatedhq/kots
asdf:ganta/asdf-kubectl-kots

kubectl-kuttlaqua:kudobuilder/kuttl
asdf:jimmidyson/asdf-kuttllinux, macos

kubectl-rolesumaqua:Ladicle/kubectl-rolesum
asdf:looztra/asdf-kubectl-bindrole

kubectxaqua:ahmetb/kubectx
asdf:https://gitlab.com/wt0f/asdf-kubectx

kubeloginaqua:int128/kubelogin

kubensaqua:ahmetb/kubectx/kubens

kubentaqua:doitintl/kube-no-trouble
asdf:virtualstaticvoid/asdf-kubent

kubeoneaqua:kubermatic/kubeone
aqua:kubermatic/kubeone

kubergruntaqua:gruntwork-io/kubergrunt
asdf:NeoHsu/asdf-kubergrunt

kubesealaqua:bitnami-labs/sealed-secrets
asdf:stefansedich/asdf-kubeseal

kubesecaqua:controlplaneio/kubesec
asdf:vitalis/asdf-kubesec

kubesharkaqua:kubeshark/kubeshark
asdf:carnei-ro/asdf-kubeshark

kubespyaqua:pulumi/kubespy
asdf:jfreeland/asdf-kubespy

kubeswitchaqua:danielfoehrKn/kubeswitch
github:danielfoehrKn/kubeswitch

kubevalaqua:instrumenta/kubeval
asdf:stefansedich/asdf-kubeval

kubevelaaqua:kubevela/kubevela
asdf:gustavclausen/asdf-kubevela

kubieaqua:sbstp/kubie
asdf:johnhamelink/asdf-kubie

kustomizeaqua:kubernetes-sigs/kustomize
asdf:Banno/asdf-kustomize

kwokctlaqua:kubernetes-sigs/kwok/kwokctl

kyvernoaqua:kyverno/kyverno
asdf:https://github.com/hobaen/asdf-kyverno-cli.git

lazydockeraqua:jesseduffield/lazydocker

lazygitaqua:jesseduffield/lazygit
asdf:nklmilojevic/asdf-lazygit

lazyjournalaqua:Lifailon/lazyjournal

lazysshaqua:Adembc/lazyssh

lefthookaqua:evilmartians/lefthook
asdf:jtzero/asdf-lefthook
go:github.com/evilmartians/lefthook

leiningenvfox:mise-plugins/vfox-leiningen
asdf:mise-plugins/mise-lein

libsql-servergithub:tursodatabase/libsql
asdf:jonasb/asdf-libsql-serverlinux, macos

license-plistaqua:mono0926/LicensePlist
asdf:MacPaw/asdf-license-plistmacos

limaaqua:lima-vm/lima
asdf:CrouchingMuppet/asdf-lima

linkerdaqua:linkerd/linkerd2
asdf:kforsthoevel/asdf-linkerd

liquibasegithub:liquibase/liquibase
asdf:mise-plugins/mise-liquibase

lisettegithub:ivov/lisette
cargo:lisette

litestreamaqua:benbjohnson/litestream
asdf:threkk/asdf-litestream

llama.cppgithub:ggml-org/llama.cpp

llmfitgithub:AlexsJones/llmfit

lnavaqua:tstack/lnav

localstackaqua:localstack/localstack-cli
github:localstack/localstack-cli

loki-logcliaqua:grafana/loki/logcli
asdf:comdotlinux/asdf-loki-logcli

longbridge-terminalgithub:longbridge/longbridge-terminal
cargo:longbridge-terminal

ls-lintaqua:loeffel-io/ls-lint
npm:@ls-lint/ls-lint
asdf:Ameausoone/asdf-ls-lint

lsdaqua:lsd-rs/lsd
asdf:mise-plugins/asdf-lsd
cargo:lsd

luavfox:mise-plugins/vfox-lua
asdf:mise-plugins/mise-lua

lua-language-serveraqua:LuaLS/lua-language-server
asdf:bellini666/asdf-lua-language-server

luajitconda:luajit
asdf:mise-plugins/mise-luaJIT

luauaqua:luau-lang/luau

lycheeaqua:lycheeverse/lychee
cargo:lychee

maestrogithub:mobile-dev-inc/maestro
asdf:dotanuki-labs/asdf-maestro

mageaqua:magefile/mage
asdf:mathew-fleisch/asdf-mage

magikacargo:magika-cli

magoaqua:carthage-software/mago

makeconda:make
asdf:mise-plugins/mise-make

maniaqua:alajmo/mani
asdf:anweber/asdf-mani

markaqua:kovetskiy/mark
github:kovetskiy/mark
asdf:jfreeland/asdf-mark

markdownlint-cli2npm:markdownlint-cli2
asdf:paulo-ferraz-oliveira/asdf-markdownlint-cli2

marksmanaqua:artempyanykh/marksman

marp-cliaqua:marp-team/marp-cli
asdf:xataz/asdf-marp-cli

masaqua:mas-cli/masmacos

maskaqua:jacobdeichert/mask
asdf:aaaaninja/asdf-mask

maturingithub:PyO3/maturin

mavenaqua:apache/maven
asdf:mise-plugins/mise-maven
vfox:mise-plugins/vfox-maven

mcaqua:minio/mc
asdf:mise-plugins/mise-mc

mdbookaqua:rust-lang/mdBook
asdf:cipherstash/asdf-mdbook
cargo:mdbook

mdbook-linkcheckgithub:Michael-F-Bryan/mdbook-linkcheck
cargo:mdbook-linkcheck
asdf:mise-plugins/mise-mdbook-linkcheck

melangeaqua:chainguard-dev/melange
asdf:omissis/asdf-melangelinux, macos

mermaid-asciiaqua:AlexanderGrooff/mermaid-ascii
github:AlexanderGrooff/mermaid-ascii

mesonpipx:meson
asdf:mise-plugins/mise-meson

micromambagithub:mamba-org/micromamba-releases

micronautgithub:micronaut-projects/micronaut-starter
asdf:mise-plugins/mise-micronaut

milleraqua:johnkerl/miller

mimirtoolaqua:grafana/mimir/mimirtool
asdf:asdf-community/asdf-mimirtoollinux, macos

minifyaqua:tdewolff/minify
asdf:axilleas/asdf-minify

minikubeaqua:kubernetes/minikube
asdf:alvarobp/asdf-minikube

minioconda:minio-server
asdf:mise-plugins/mise-minio

minishiftaqua:minishift/minishift
asdf:sqtran/asdf-minishift

minisignaqua:jedisct1/minisign

mintgithub:mint-lang/mint
asdf:mint-lang/asdf-mint

mirrordaqua:metalbear-co/mirrord
asdf:metalbear-co/asdf-mirrord

mitmproxypipx:mitmproxy
asdf:mise-plugins/mise-mitmproxy

mkcertaqua:FiloSottile/mkcert
asdf:salasrod/asdf-mkcert

mockeryaqua:vektra/mockery
asdf:cabify/asdf-mockery

mockologithub:uber/mockolo
asdf:mise-plugins/mise-mockolo

moldaqua:rui314/mold

mongodbasdf:mise-plugins/mise-mongodb
vfox:echocat/vfox-mongod

mongoshgithub:mongodb-js/mongosh
asdf:itspngu/asdf-mongosh

mprocsaqua:pvolok/mprocs

mssqldefaqua:sqldef/sqldef/mssqldef

mutagenaqua:mutagen-io/mutagen
github:mutagen-io/mutagen

mvndaqua:apache/maven-mvnd
asdf:joschi/asdf-mvnd

mysqlasdf:mise-plugins/mise-mysql

mysql-clientconda:mysql-client

mysqldefaqua:sqldef/sqldef/mysqldef

nancyaqua:sonatype-nexus-community/nancy
asdf:iilyak/asdf-nancy

naviaqua:denisidoro/navi
cargo:navi

nekogithub:HaxeFoundation/neko
asdf:asdf-community/asdf-neko

nelmaqua:werf/nelm

neo4jhttp:neo4j

neonctlaqua:neondatabase/neonctl

neovimvfox:mise-plugins/vfox-neovim
aqua:neovim/neovim

nerdctlaqua:containerd/nerdctl
asdf:dmpe/asdf-nerdctl

newrelicaqua:newrelic/newrelic-cli
asdf:NeoHsu/asdf-newrelic-cli

nfpmaqua:goreleaser/nfpm
asdf:ORCID/asdf-nfpm

ninpm:@antfu/ni

ninjaaqua:ninja-build/ninja
asdf:asdf-community/asdf-ninja

nodecore:node

nomadaqua:hashicorp/nomad
asdf:mise-plugins/mise-hashicorp

nomad-packhttp:nomad-pack
asdf:mise-plugins/mise-hashicorp

notationaqua:notaryproject/notation
asdf:bodgit/asdf-notation

novaaqua:FairwindsOps/nova
asdf:elementalvoid/asdf-nova

npmaqua:npm/cli
npm:npm

nscgithub:nats-io/nsc
asdf:dex4er/asdf-nsc

numbataqua:sharkdp/numbat
cargo:numbat-cli

oapi-codegengo:github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen
asdf:dylanrayboss/asdf-oapi-codegen

oauth2caqua:cloudentity/oauth2c

ochttp:oc
conda:openshift-cli
asdf:mise-plugins/mise-oclinux, macos, windows

ociasdf:mise-plugins/mise-oci

octosqlgithub:cube2222/octosql

odingithub:odin-lang/Odin
asdf:jtakakura/asdf-odin

odoaqua:redhat-developer/odo
asdf:rm3l/asdf-odo

oh-my-poshaqua:JanDeDobbeleer/oh-my-posh

ohaaqua:hatoo/oha
github:hatoo/oha

okta-awsaqua:okta/okta-aws-cli
asdf:bennythejudge/asdf-plugin-okta-aws-cli

oktetoaqua:okteto/okteto
asdf:BradenM/asdf-okteto

ollamaaqua:ollama/ollama
asdf:virtualstaticvoid/asdf-ollama

omaqua:pivotal-cf/om
asdf:mise-plugins/tanzu-plug-in-for-asdf

omnictlaqua:siderolabs/omni/omnictl

onyxgithub:onyx-lang/onyx
asdf:jtakakura/asdf-onyx

opaaqua:open-policy-agent/opa
asdf:tochukwuvictor/asdf-opa

opamgithub:ocaml/opam
asdf:asdf-community/asdf-opam

openbaoaqua:openbao/openbao/bao
github:openbao/openbao

opencodeaqua:anomalyco/opencode

openfaas-cliaqua:openfaas/faas-cli
asdf:zekker6/asdf-faas-cli

openfgagithub:openfga/openfga

opengrepaqua:opengrep/opengrep

opensearch-cligithub:opensearch-project/opensearch-cli
asdf:mise-plugins/mise-opensearch-cli

openshift-installhttp:openshift-installlinux, macos

opentofuaqua:opentofu/opentofu
asdf:virtualroot/asdf-opentofu

operator-sdkaqua:operator-framework/operator-sdk
asdf:Medium/asdf-operator-sdk

orasaqua:oras-project/oras
asdf:bodgit/asdf-oras

ormolugithub:tweag/ormolu

orvalnpm:orval

osv-scanneraqua:google/osv-scanner

overmindgithub:DarthSim/overmind
go:github.com/DarthSim/overmind/v2

oxfmtnpm:oxfmt

oxipngaqua:oxipng/oxipng
cargo:oxipng

oxkeraqua:mrjackwills/oxker
cargo:oxker

oxlintnpm:oxlint
aqua:oxc-project/oxc/oxlint

packeraqua:hashicorp/packer
asdf:mise-plugins/mise-hashicorp

pandocgithub:jgm/pandoc
asdf:Fbrisset/asdf-pandoc

patatgithub:jaspervdj/patat
asdf:airtonix/asdf-patat

pdmpipx:pdm
asdf:1oglop1/asdf-pdm

pecoaqua:peco/peco
asdf:asdf-community/asdf-peco

peripheryaqua:peripheryapp/periphery
asdf:mise-plugins/mise-periphery

perlaqua:skaji/relocatable-perl
asdf:ouest/asdf-perl

phpasdf:mise-plugins/asdf-php
vfox:mise-plugins/vfox-php

pigithub:earendil-works/pi
aqua:earendil-works/pi
npm:@earendil-works/pi-coding-agent

pinactaqua:suzuki-shunsuke/pinact

pintaqua:cloudflare/pint
asdf:sam-burrell/asdf-pint

pipectlaqua:pipe-cd/pipecd/pipectl
asdf:pipe-cd/asdf-pipectllinux, macos

pipenvvfox:mise-plugins/vfox-pipenv
pipx:pipenv

pipxaqua:pypa/pipx
asdf:mise-plugins/mise-pipx

pitchforkaqua:jdx/pitchfork

pivnetaqua:pivotal-cf/pivnet-cli
asdf:mise-plugins/tanzu-plug-in-for-asdf

pixigithub:prefix-dev/pixi

pklaqua:apple/pkl
asdf:mise-plugins/asdf-pkl

pleaseaqua:thought-machine/please
asdf:asdf-community/asdf-please

plutoaqua:FairwindsOps/pluto
asdf:FairwindsOps/asdf-pluto

pnpmaqua:pnpm/pnpm
npm:pnpm

pocketbasegithub:pocketbase/pocketbase

podletaqua:containers/podlet
github:containers/podlet
cargo:podlet

podmangithub:containers/podman
asdf:tvon/asdf-podman

podman-tuigithub:containers/podman-tui

poetryvfox:mise-plugins/vfox-poetry
pipx:poetry

polarisaqua:FairwindsOps/polaris
asdf:particledecay/asdf-polaris

popeyeaqua:derailed/popeye
asdf:nlamirault/asdf-popeye

porteraqua:getporter/porter/porter
github:getporter/porter

portlessnpm:portless

postgresvfox:mise-plugins/vfox-postgres
asdf:mise-plugins/mise-postgres

powerline-goaqua:justjanne/powerline-go
asdf:dex4er/asdf-powerline-go

powerpipeaqua:turbot/powerpipe
asdf:jc00ke/asdf-powerpipe

powershell-coreaqua:PowerShell/PowerShell
asdf:daveneeley/asdf-powershell-core

pre-commitaqua:pre-commit/pre-commit
asdf:jonathanmorley/asdf-pre-commit
pipx:pre-commit

prekaqua:j178/prek

prettiernpm:prettier

process-composeaqua:F1bonacc1/process-compose
github:F1bonacc1/process-compose

promtoolaqua:prometheus/prometheus
asdf:asdf-community/asdf-promtool

protocaqua:protocolbuffers/protobuf/protoc
asdf:paxosglobal/asdf-protoc

protoc-gen-connect-gogo:connectrpc.com/connect/cmd/protoc-gen-connect-go
asdf:dylanrayboss/asdf-protoc-gen-connect-go

protoc-gen-goaqua:protocolbuffers/protobuf-go/protoc-gen-go
asdf:pbr0ck3r/asdf-protoc-gen-go

protoc-gen-go-grpcaqua:grpc/grpc-go/protoc-gen-go-grpc
asdf:pbr0ck3r/asdf-protoc-gen-go-grpc

protoc-gen-jsgithub:protocolbuffers/protobuf-javascript
asdf:pbr0ck3r/asdf-protoc-gen-js

protoc-gen-validateaqua:bufbuild/protoc-gen-validate
go:github.com/envoyproxy/protoc-gen-validate

protolintaqua:yoheimuta/protolint
asdf:spencergilbert/asdf-protolint

psqldefaqua:sqldef/sqldef/psqldef

pulumiaqua:pulumi/pulumi
asdf:canha/asdf-pulumi

purescriptgithub:purescript/purescript
asdf:jrrom/asdf-purescript

purtynpm:purty

pythoncore:python

qdnsgithub:natesales/q
asdf:moritz-makandra/asdf-plugin-qdns

qsvaqua:dathere/qsv
github:dathere/qsv
asdf:vjda/asdf-qsv

quarkusgithub:quarkusio/quarkus
asdf:mise-plugins/mise-quarkus

quicktypenpm:quicktype

qwennpm:@qwen-code/qwen-code

racketaqua:racket/racket/minimal

railwaygithub:railwayapp/cli
cargo:railwayapp

rancheraqua:rancher/cli
asdf:abinet/asdf-rancher

rbac-lookupaqua:FairwindsOps/rbac-lookup
asdf:looztra/asdf-rbac-lookup

rcloneaqua:rclone/rclone
asdf:johnlayton/asdf-rclone

rebargithub:erlang/rebar3

reckonergithub:FairwindsOps/reckoner
asdf:FairwindsOps/asdf-reckoner

redisvfox:mise-plugins/vfox-redis
asdf:mise-plugins/mise-redis

redpanda-connectaqua:redpanda-data/connect
asdf:benthosdev/benthos-asdf

regaqua:genuinetools/reg
asdf:looztra/asdf-reg

regalaqua:open-policy-agent/regal
asdf:mise-plugins/mise-regal

regctlaqua:regclient/regclient/regctl
asdf:ORCID/asdf-regctl

regsyncaqua:regclient/regclient/regsync
asdf:rsrchboy/asdf-regsync

release-plzaqua:release-plz/release-plz
github:release-plz/release-plz
cargo:release-plz

resticaqua:restic/restic
asdf:xataz/asdf-restic

restishaqua:rest-sh/restish
go:github.com/danielgtaylor/restish

resvgaqua:linebender/resvg
cargo:resvg

reviveaqua:mgechev/revive
asdf:bjw-s/asdf-revive

richgoaqua:kyoh86/richgo
asdf:paxosglobal/asdf-richgo

ripgrepaqua:BurntSushi/ripgrep
asdf:https://gitlab.com/wt0f/asdf-ripgrep
cargo:ripgrep

ripgrep-allaqua:phiresky/ripgrep-all
cargo:ripgrep_all

ripsecretsaqua:sirwart/ripsecrets
asdf:https://github.com/boris-smidt-klarrio/asdf-ripsecrets

rmzaqua:SUPERCILEX/fuc/rmz

rpkaqua:redpanda-data/redpanda

rtkaqua:rtk-ai/rtk
github:rtk-ai/rtk

rubycore:ruby

ruffaqua:astral-sh/ruff
asdf:simhem/asdf-ruff

rumdlaqua:rvben/rumdl
github:rvben/rumdl

rushaqua:shenwei356/rush

rustcore:rust
asdf:code-lever/asdf-rust

rust-analyzeraqua:rust-lang/rust-analyzer
asdf:Xyven1/asdf-rust-analyzer

rustfsgithub:rustfs/rustfs

rusticaqua:rustic-rs/rustic
cargo:rustic-rs

ryeaqua:astral-sh/rye
asdf:Azuki-bar/asdf-rye
cargo:rye

s5cmdaqua:peak/s5cmd

saml2awsaqua:Versent/saml2aws
asdf:elementalvoid/asdf-saml2aws

sampleraqua:sqshq/sampler

sbtconda:sbt
asdf:mise-plugins/mise-sbt

scalaasdf:mise-plugins/mise-scala
vfox:mise-plugins/vfox-scala

scala-cligithub:VirtusLab/scala-cli
asdf:mise-plugins/mise-scala-cli

scalafmtgithub:scalameta/scalafmt

scalewayaqua:scaleway/scaleway-cli
asdf:albarralnunez/asdf-plugin-scaleway-cli

scalingo-cliaqua:Scalingo/cli
asdf:brandon-welsch/asdf-scalingo-cli

scarbgithub:software-mansion/scarb
asdf:software-mansion/asdf-scarb

sccacheaqua:mozilla/sccache
asdf:emersonmx/asdf-sccache
cargo:sccache

schemacrawlergithub:schemacrawler/SchemaCrawler

scie-pantsgithub:pantsbuild/scie-pants
asdf:robzr/asdf-scie-pants

scooteraqua:thomasschafer/scooter
cargo:scooter

scorecardaqua:ossf/scorecard

sdaqua:chmln/sd
cargo:sd

semgreppipx:semgrep
asdf:mise-plugins/mise-semgrep

semveraqua:fsaintjacques/semver-tool
vfox:mise-plugins/vfox-semver
asdf:mathew-fleisch/asdf-semver

sentinelhttp:sentinel
asdf:mise-plugins/mise-hashicorp

sentryaqua:getsentry/sentry-cli

serverlessnpm:serverless
asdf:mise-plugins/mise-serverless

setup-envtestaqua:kubernetes-sigs/controller-runtime/setup-envtest
asdf:mise-plugins/mise-setup-envtest

sheldonaqua:rossmacarthur/sheldon
github:rossmacarthur/sheldon
cargo:sheldonlinux, macos

shell2httpaqua:msoap/shell2http
asdf:ORCID/asdf-shell2http

shellcheckaqua:koalaman/shellcheck
asdf:luizm/asdf-shellcheck

shellspecaqua:shellspec/shellspec
asdf:poikilotherm/asdf-shellspec

shfmtaqua:mvdan/sh
asdf:luizm/asdf-shfmt
go:mvdan.cc/sh/v3/cmd/shfmt

signadotgithub:signadot/cli

sing-boxgithub:sagernet/sing-box

skaffoldaqua:GoogleContainerTools/skaffold
asdf:nklmilojevic/asdf-skaffold

skateaqua:charmbracelet/skate
asdf:chessmango/asdf-skate

skeemaaqua:skeema/skeema

slothaqua:slok/sloth
asdf:slok/asdf-sloth

slsa-verifieraqua:slsa-framework/slsa-verifier
github:slsa-framework/slsa-verifier
go:github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier

smithyaqua:smithy-lang/smithy
asdf:mise-plugins/mise-smithy

snykaqua:snyk/cli
github:snyk/cli
asdf:nirfuchs/asdf-snyk

soft-servegithub:charmbracelet/soft-serve
asdf:chessmango/asdf-soft-serve

soliditygithub:ethereum/solidity
asdf:diegodorado/asdf-solidity

sonar-scanner-cliaqua:SonarSource/sonar-scanner-cli
asdf:virtualstaticvoid/asdf-sonarscanner

sonarqube-cliaqua:SonarSource/sonarqube-cli

sonobuoygithub:vmware-tanzu/sonobuoy
asdf:Nick-Triller/asdf-sonobuoy

sopsaqua:getsops/sops
asdf:mise-plugins/mise-sops

sopstoolaqua:ibotta/sopstool
asdf:elementalvoid/asdf-sopstool

sourcerygithub:krzysztofzablocki/Sourcery
asdf:mise-plugins/mise-sourcerylinux, macos

spacectlaqua:spacelift-io/spacectl
asdf:bodgit/asdf-spacectl

spagogithub:purescript/spago
asdf:jrrom/asdf-spago

sparkaqua:apache/spark
asdf:mise-plugins/mise-spark

specstoryaqua:specstoryai/getspecstorylinux, macos

spectralaqua:stoplightio/spectral
asdf:vbyrd/asdf-spectral

spinaqua:spinnaker/spin
asdf:pavloos/asdf-spin

spring-bootasdf:mise-plugins/mise-spring-boot

spruceaqua:geofffranks/spruce
asdf:woneill/asdf-spruce

sqlcaqua:sqlc-dev/sqlc
github:sqlc-dev/sqlc

sqliteconda:sqlite
asdf:mise-plugins/mise-sqlite

sqlite3defaqua:sqldef/sqldef/sqlite3def

sshiaqua:aakso/ssh-inscribe/sshi

sshuttlepipx:sshuttle
asdf:mise-plugins/mise-sshuttle

sstgithub:sst/sst

stackaqua:commercialhaskell/stack
asdf:mise-plugins/mise-ghcup

starknet-foundrygithub:foundry-rs/starknet-foundry

starknet-foundry-sncastgithub:foundry-rs/starknet-foundry

starshipaqua:starship/starship
asdf:gr1m0h/asdf-starship
cargo:starship

staticcheckaqua:dominikh/go-tools/staticcheck
asdf:pbr0ck3r/asdf-staticcheck
go:honnef.co/go/tools/cmd/staticcheck

steampipeaqua:turbot/steampipe
asdf:carnei-ro/asdf-steampipe

stepaqua:smallstep/cli
asdf:log2/asdf-step

sternaqua:stern/stern
asdf:looztra/asdf-stern

stripeaqua:stripe/stripe-cli
asdf:offbyone/asdf-stripe

styluaaqua:JohnnyMorganz/StyLua
asdf:jc00ke/asdf-stylua
cargo:stylua

suigithub:MystenLabs/sui
asdf:placeholder-soft/asdf-sui

supabaseaqua:supabase/cli

superfileaqua:yorukot/superfile

superhtmlgithub:kristoff-it/superhtml

svgonpm:svgo

svuaqua:caarlos0/svu
asdf:asdf-community/asdf-svu

swagaqua:swaggo/swag
asdf:behoof4mind/asdf-swag

swiftcore:swiftlinux, macos

swift-package-listgithub:FelixHerrmann/swift-package-list
spm:FelixHerrmann/swift-package-list
asdf:mise-plugins/mise-swift-package-list

swiftformatgithub:nicklockwood/SwiftFormat
asdf:mise-plugins/mise-swiftformat

swiftgengithub:SwiftGen/SwiftGen
asdf:mise-plugins/mise-swiftgen

swiftlintaqua:realm/SwiftLint
asdf:mise-plugins/mise-swiftlint

syftaqua:anchore/syft
asdf:davidgp1701/asdf-syft

systemctl-tuiaqua:rgwood/systemctl-tuilinux

tailpipeaqua:turbot/tailpipe

talhelperaqua:budimanjojo/talhelper
asdf:bjw-s/asdf-talhelper

talosctlaqua:siderolabs/talos

tankaaqua:grafana/tanka
asdf:trotttrotttrott/asdf-tanka

tanzugithub:vmware-tanzu/tanzu-cli

taploaqua:tamasfe/taplo
cargo:taplo-cli

tartaqua:cirruslabs/tartmacos

taskaqua:go-task/task
asdf:particledecay/asdf-task

tblsaqua:k1LoW/tbls

tctlaqua:temporalio/tctl
asdf:eko/asdf-tctl

tektonaqua:tektoncd/cli
asdf:johnhamelink/asdf-tekton-cli

teleport-communityasdf:mise-plugins/mise-teleport-community

teleport-entasdf:mise-plugins/mise-teleport-ent

telepresenceaqua:telepresenceio/telepresence
asdf:pirackr/asdf-telepresence

televisionaqua:alexpasmantier/television

telleraqua:tellerops/teller
asdf:pdemagny/asdf-teller

temporalaqua:temporalio/temporal
asdf:asdf-community/asdf-temporal

terraformaqua:hashicorp/terraform
asdf:mise-plugins/mise-hashicorp
vfox:mise-plugins/vfox-terraform

terraform-docsaqua:terraform-docs/terraform-docs
asdf:looztra/asdf-terraform-docs

terraform-lsaqua:hashicorp/terraform-ls
asdf:mise-plugins/mise-hashicorp

terraform-lspaqua:juliosueiras/terraform-lsp
asdf:bartlomiejdanek/asdf-terraform-lsp

terraform-validatoraqua:thazelart/terraform-validator
asdf:looztra/asdf-terraform-validator

terraformeraqua:GoogleCloudPlatform/terraformer
asdf:gr1m0h/asdf-terraformer

terragruntaqua:gruntwork-io/terragrunt
asdf:gruntwork-io/asdf-terragrunt

terramateaqua:terramate-io/terramate
asdf:martinlindner/asdf-terramate

terrascanaqua:tenable/terrascan
asdf:hpdobrica/asdf-terrascan

tf-summarizeaqua:dineshba/tf-summarize
asdf:adamcrews/asdf-tf-summarize

tfc-agenthttp:tfc-agent
asdf:mise-plugins/mise-hashicorplinux

tfctlaqua:flux-iac/tofu-controller/tfctl
asdf:deas/asdf-tfctl

tfenvaqua:tfutils/tfenv
asdf:carlduevel/asdf-tfenv

tflintaqua:terraform-linters/tflint
asdf:skyzyx/asdf-tflint

tfmigrateaqua:minamijoyo/tfmigrate
asdf:dex4er/asdf-tfmigrate

tfnotifyaqua:mercari/tfnotify
asdf:jnavarrof/asdf-tfnotify

tfsecaqua:aquasecurity/tfsec
asdf:woneill/asdf-tfsec

tfstate-lookupaqua:fujiwara/tfstate-lookup
asdf:carnei-ro/asdf-tfstate-lookup

tfswitchgithub:warrensbox/terraform-switcher
asdf:iul1an/asdf-tfswitch

tfupdateaqua:minamijoyo/tfupdate
asdf:yuokada/asdf-tfupdate

tigerbeetlegithub:tigerbeetle/tigerbeetle

tiltaqua:tilt-dev/tilt
asdf:eaceaser/asdf-tilt

timoniaqua:stefanprodan/timoni
asdf:Smana/asdf-timoni

tinyasdf:mise-plugins/mise-tiny

tinygoaqua:tinygo-org/tinygo

tinymistaqua:Myriad-Dreamin/tinymist
cargo:tinymist

tinytexasdf:mise-plugins/mise-tinytex

tirithgithub:sheeki03/tirith
cargo:tirith

tlrcaqua:tldr-pages/tlrc
cargo:tlrc

tmuxaqua:tmux/tmux-builds
asdf:mise-plugins/mise-tmuxlinux, macos

tokeicargo:tokei
aqua:XAMPPRocky/tokei
asdf:gasuketsu/asdf-tokei

tombiaqua:tombi-toml/tombi

tomcataqua:apache/tomcat
asdf:mise-plugins/mise-tomcat

tonnagegithub:elementalvoid/tonnage
asdf:elementalvoid/asdf-tonnage

topgradeaqua:topgrade-rs/topgrade
github:topgrade-rs/topgrade
cargo:topgrade

traefikgithub:traefik/traefik
asdf:Dabolus/asdf-traefik

transifexgithub:transifex/cli
asdf:ORCID/asdf-transifex

trdsqlaqua:noborus/trdsql
asdf:johnlayton/asdf-trdsql

tree-sitteraqua:tree-sitter/tree-sitter
asdf:ivanvc/asdf-tree-sitter

tridentctlaqua:NetApp/trident/tridentctl
asdf:asdf-community/asdf-tridentctllinux, macos

trivyaqua:aquasecurity/trivy
asdf:zufardhiyaulhaq/asdf-trivy

trufflehogaqua:trufflesecurity/trufflehog
github:trufflesecurity/trufflehog

trunknpm:@trunkio/launcher

trzsz-goaqua:trzsz/trzsz-go
github:trzsz/trzsz-go

trzsz-sshaqua:trzsz/trzsz-ssh
go:github.com/trzsz/trzsz-ssh/cmd/tssh

tsurugithub:tsuru/tsuru-client
asdf:virtualstaticvoid/asdf-tsuru

ttydaqua:tsl0922/ttyd
asdf:ivanvc/asdf-ttyd

tuistaqua:tuist/tuist
asdf:mise-plugins/mise-tuistmacos, linux

turbonpm:turbo

tursoaqua:tursodatabase/turso-cli
github:tursodatabase/turso-cli

tusdgithub:tus/tusd

tyaqua:astral-sh/ty
github:astral-sh/ty

typosaqua:crate-ci/typos
asdf:aschiavon91/asdf-typos
cargo:typos-cli

typstaqua:typst/typst
github:typst/typst
asdf:stephane-klein/asdf-typst
cargo:typst-cli

typstyleaqua:Enter-tainer/typstyle
cargo:typstyle

ubiaqua:houseabsolute/ubi

umociaqua:opencontainers/umocilinux

unisongithub:unisonweb/unison
asdf:susurri/asdf-unison

upctlaqua:UpCloudLtd/upcloud-cli

updatecliaqua:updatecli/updatecli
asdf:updatecli/asdf-updatecli

uptgithub:sigoden/upt
asdf:ORCID/asdf-upt

upxaqua:upx/upx
asdf:jimmidyson/asdf-upx

usageaqua:jdx/usage
asdf:mise-plugins/mise-usage
cargo:usage-cli

usqlaqua:xo/usql
asdf:itspngu/asdf-usql

uvaqua:astral-sh/uv
asdf:asdf-community/asdf-uv
pipx:uv

vasdf:mise-plugins/mise-v

vacuumaqua:daveshanley/vacuum

valeaqua:vale-cli/vale
asdf:pdemagny/asdf-vale

valsaqua:helmfile/vals
asdf:dex4er/asdf-vals

vaultaqua:hashicorp/vault
asdf:mise-plugins/mise-hashicorp

vclusteraqua:loft-sh/vcluster
asdf:https://gitlab.com/wt0f/asdf-vcluster

vectoraqua:vectordotdev/vector

veladgithub:kubevela/velad
asdf:mise-plugins/mise-velad

veleroaqua:vmware-tanzu/velero
asdf:looztra/asdf-velero

vendiraqua:carvel-dev/vendir
asdf:vmware-tanzu/asdf-carvel

venomaqua:ovh/venom
asdf:aabouzaid/asdf-venom

vercelnpm:vercel

vespa-cligithub:vespa-engine/vespa

vfoxaqua:version-fox/vfox

vhsaqua:charmbracelet/vhs
asdf:chessmango/asdf-vhs

victoria-metricsaqua:VictoriaMetrics/VictoriaMetrics/victoria-metrics

viddyaqua:sachaos/viddy
asdf:ryodocx/asdf-viddy

vimconda:vim
asdf:mise-plugins/mise-vim

viteplusnpm:vite-plus

vividaqua:sharkdp/vivid
cargo:vivid

vlangvfox:mise-plugins/vfox-vlang

vultrgithub:vultr/vultr-cli
asdf:ikuradon/asdf-vultr-cli

wacliaqua:openclaw/wacli
github:openclaw/wacli

wait-for-gh-rate-limitgithub:jdx/wait-for-gh-rate-limit

washaqua:wasmCloud/wasmCloud/wash

wasm-toolsaqua:bytecodealliance/wasm-tools
cargo:wasm-tools

wasmeraqua:wasmerio/wasmer
asdf:tachyonicbytes/asdf-wasmer

wasmtimeaqua:bytecodealliance/wasmtime
asdf:tachyonicbytes/asdf-wasmtime

watchexecaqua:watchexec/watchexec
cargo:watchexec-cli

waypointaqua:hashicorp/waypoint
asdf:mise-plugins/mise-hashicorp

weave-gitopsgithub:weaveworks/weave-gitops
asdf:deas/asdf-weave-gitops

websocataqua:vi/websocat
asdf:bdellegrazie/asdf-websocat
cargo:websocat

werfaqua:werf/werf

workmuxgithub:raine/workmux
cargo:workmux

worktrunkaqua:max-sixty/worktrunk
cargo:worktrunk

wranglernpm:wrangler

wtfutilaqua:wtfutil/wtf
asdf:NeoHsu/asdf-wtfutil

xcaqua:joerdav/xc
asdf:airtonix/asdf-xc

xcbeautifyaqua:cpisciotta/xcbeautify
asdf:mise-plugins/asdf-xcbeautify

xchtmlreportgithub:XCTestHTMLReport/XCTestHTMLReportmacos

xcodegenaqua:yonaskolb/XcodeGen
github:yonaskolb/XcodeGenmacos

xcodesaqua:XcodesOrg/xcodesmacos

xcresultparsergithub:a7ex/xcresultparsermacos

xcsiftgithub:ldomaradzki/xcsiftmacos

xhaqua:ducaale/xh
asdf:NeoHsu/asdf-xh
cargo:xh

xxhpipx:xxh-xxh

yamlfmtaqua:google/yamlfmt
asdf:mise-plugins/asdf-yamlfmt
go:github.com/google/yamlfmt/cmd/yamlfmt

yamllintpipx:yamllint
asdf:ericcornelissen/asdf-yamllint

yamlscriptaqua:yaml/yamlscript
asdf:mise-plugins/mise-yamlscript

yara-xgithub:VirusTotal/yara-x

yarnvfox:mise-plugins/vfox-yarn
asdf:mise-plugins/mise-yarn
aqua:yarnpkg/berry
npm:@yarnpkg/cli-dist

yaziaqua:sxyazi/yazi
cargo:yazi-fm

yjaqua:sclevine/yj
asdf:ryodocx/asdf-yj

yoraqua:bridgecrewio/yor
asdf:ordinaryexperts/asdf-yor

youtube-dlaqua:ytdl-org/ytdl-nightly
asdf:mise-plugins/mise-youtube-dl

yqaqua:mikefarah/yq
asdf:sudermanjr/asdf-yq
go:github.com/mikefarah/yq/v4

yt-dlpgithub:yt-dlp/yt-dlp
asdf:duhow/asdf-yt-dlp

yttaqua:carvel-dev/ytt
asdf:vmware-tanzu/asdf-carvel

zarfaqua:zarf-dev/zarf

zellijaqua:zellij-org/zellij
asdf:chessmango/asdf-zellij
cargo:zellij

zephyraqua:MaybeJustJames/zephyr
asdf:nsaunders/asdf-zephyr

zigcore:zig

zigmodaqua:nektro/zigmod
github:nektro/zigmod
asdf:mise-plugins/asdf-zigmod

zizmoraqua:zizmorcore/zizmor
cargo:zizmor

zlsaqua:zigtools/zls

zolaaqua:getzola/zola
asdf:salasrod/asdf-zola

zoxideaqua:ajeetdsouza/zoxide
cargo:zoxide

zprintaqua:kkinnear/zprint
github:kkinnear/zprint
asdf:mise-plugins/mise-zprint
