# Log Agent

- A prototype for a remote "Who" command.

- Finds "successfully authorized" players at an interval.

## Table of Contents

- [Requirements](#Requirements)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [Usage](#Usage)
- [Contribution](#Contribution)
- [Support](#Support)

## Requirements

- Python 3

- A Xania environment with logs!

```bash
xania/make install && make dirs
```

## Installation

```bash
git clone https://github.com/abraidotti/xania-utils
cd xania-utils/log-agent
```

## Configuration

None needed.

## Usage

Use the path flag to point to log files:

```bash
python log-agent.py -p "../../xania/log"
```

Leave the agent running, and it will print out successfully authorized players at an interval.

## Contribution

Find Tajil in the game or file an issue.

## Support

Find Tajil in the game or file an issue.
