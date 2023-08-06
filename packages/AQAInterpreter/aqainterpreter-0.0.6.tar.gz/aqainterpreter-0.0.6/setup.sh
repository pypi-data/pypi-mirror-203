#!/bin/bash

# # ubuntu
# sudo apt update && sudo apt upgrade -y
# sudo apt install hatch pandoc texlive-xetex fonts-firacode yarnpkg fossil -y 

# # fedora
# sudo dnf install 'dnf-command(copr)'
# sudo dnf copr enable adrienverge/some-nice-fonts -y
# sudo dnf install hatch pandoc texlive-xetex fira-code-fonts some-nice-fonts yarnpkg librsvg2-tools texlive-scheme-medium fossil -y


# cd report
# mkdir mermaid
# cd mermaid
# cd report
# mkdir mermaid
# cd mermaid

# https://github.com/mermaid-js/mermaid-cli#install-locally
# sudo yarn global add -g @mermaid-js/mermaid-cli

# then manually change `==` to `<=` for syntax_tree.svg with inspect element
# becuase otherwise renders as `&lt;`

# # auto generate packages.mmd and classes.md
# pyreverse ./AQAInterpreter/ -o mmd

# # setup project
# hatch shell

# # publish to pypi
# hatch build
# hatch publish
#   # go on https://pypi.org
#   # get a token https://pypi.org/help/#apitoke
#   # copy paste the username and token in this command

