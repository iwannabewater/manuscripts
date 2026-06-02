# Backends | mise-en-place

> Source: https://mise.jdx.dev/dev-tools/backends/

Skip to content

mise-en-place

SearchK

Appearance

Menu
Return to top

Backends ​

Backends are package managers or ecosystems that mise uses to install tools and plugins. Each backend can install and manage multiple tools from its ecosystem. For example, the npm backend can install many different tools like npm:prettier, or the pipx backend can install tools like pipx:black. This allows mise to support a wide variety of tools and languages by leveraging different package managers and their ecosystems.

When you run the mise use command, mise will determine the appropriate backend to use based on the tool you are trying to manage. The backend will then handle the installation, configuration, and any other necessary steps to ensure the tool is ready to use.

For more details on how backends fit into mise's overall design, see the backend architecture documentation.

Below is a list of the available backends in mise:

asdf (provide tools through plugins)

aqua

cargo

conda

dotnet experimental

forgejo

gem

github

gitlab

go

http

npm

pipx

s3 experimental

spm experimental

ubi

vfox (provide tools through plugins)

custom backends (build your own backend with a plugin which itself provides many tools)
