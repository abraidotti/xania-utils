# TMUX

This script will stand up and run a persistent local build of Xania in discrete TMUX windows.

## Table of Contents

- [Requirements](#Requirements)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [Usage](#Usage)
- [Contribution](#Contribution)
- [Support](#Support)

## Requirements

- A linux environment

- The [Xania](https://github.com/mattgodbolt/xania) repo.

- [TMUX](https://github.com/tmux/tmux/wiki)

## Installation

First build Xania's doorman and Xania binaries:

```bash
/xania/make install
```

To open tmux and execute those binaries, run:

```bash
/xania-utils/tmux-xania-local.sh
```

And if you want to edit files and recompile, quit the Xania binary and run:

```bash
cd /xania/cmake-build-debug && /xania/make all install
```

and restart:

```bash
/install/bin/xania
```

## Configuration

No configuration needed at the moment.

## Usage

### A few helpful tmux commands

`tmux a` will reconnect to an existing session

`tmux kill-session -t Xania` will kill this current tmux server and the Xania binaries

`tmux list-sessions` to see what's running

### Inside tmux

`ctrl+b n` to cycle through windows

`ctrl+b ;` to cycle through panes

`ctrl+b d` to exit tmux

## Contribution

WIP

## Support

Find Tajil in the game or file an issue.
