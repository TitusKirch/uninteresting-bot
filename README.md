# UninterestingBot
<p align="center">
    <a href="https://github.com/TitusKirch/uninteresting-bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/TitusKirch/uninteresting-bot?label=License&labelColor=30363D&color=2FBF50" alt="License"></a>
    <a href="https://github.com/TitusKirch/uninteresting-bot/releases"><img src="https://img.shields.io/github/downloads/TitusKirch/uninteresting-bot/total?label=Downloads&labelColor=30363D&color=2FBF50" alt="Downloads"></a>
    <a href="https://github.com/TitusKirch/uninteresting-bot/graphs/contributors"><img src="https://img.shields.io/github/contributors/TitusKirch/uninteresting-bot?label=Contributors&labelColor=30363D&color=2FBF50" alt="Contributors"></a>
    <a href="https://discord.tkirch.dev"><img src="https://img.shields.io/discord/576562577769889805?label=Discord (TKirch.dev)&labelColor=30363D&color=2FBF50&logoColor=959DA5&logo=Discord" alt="Discord (TKirch.dev)"></a>
</p>

## Table of Contents
* [About the project](#about-the-project)
* [Getting Started](#getting-started)
    * [Requirements](#requirements)
    * [Installing](#installing)
    * [Run bot](#run-bot)
    * [Commands](#commands)
* [Contributing](#contributing)
* [Versioning](#versioning)
* [Built With](#built-with)
* [Authors](#authors)
* [License](#license)

## About the project
A self hosting Discord bot, written in Python.

## Getting Started
In order for the software to be used properly, all [requirements](#requirements) must be met.

### Requirements
* Python 3.5.3 or higher
* PIP
* tmux
* git

### Installing
*At the end of this section you will find all commands in one block*

Clone the repository, go to the cloned folder and set permissions
```bash
git clone https://github.com/TitusKirch/uninteresting-bot.git
cd uninteresting-bot
chmod +x bot.sh
```

Copy the default configuration file
```bash
cp config_default.ini config.ini 
```

Edit the configuration file (it is important that you add your bot token)
```bash
nano config.ini 
```

Install all requirements
```bash
./bot.sh install
```

(Optional) Update the bot
```bash
./bot.sh update
```

Here are all commands also in one block
```bash
git clone https://github.com/TitusKirch/uninteresting-bot.git
cd uninteresting-bot
chmod +x bot.sh
cp config_default.ini config.ini 
nano config.ini 
./bot.sh install
```

### Run the bot
You can start the bot with the following command
```bash
./bot.sh start
```

### Commands
You can start the bot with the following command

| Command | Action |
| --- | --- |
| `./bot.sh start` | Start the bot |
| `./bot.sh stop` | Stop the bot |
| `./bot.sh restart` | Restart the bot |
| `./bot.sh install` | Install all requirements |
| `./bot.sh update` | Update the bot from this repository |

## Contributing
There are many ways to help this open source project. Write tutorials, improve documentation, share bugs with others, make feature requests, or just write code. We look forward to every contribution.

For more information and our guidelines, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Versioning
We use [SemVer](http://semver.org/) for versioning. For available versions, see the [tags on this repository](https://github.com/TitusKirch/uninteresting-bot/tags). 

## Built With
* [discord.py](https://github.com/Rapptz/discord.py) - An API wrapper for Discord written in Python.

## Authors
* **Titus Kirch** - *Main development* - [TitusKirch](https://github.com/TitusKirch)

See also the list of [contributors](https://github.com/TitusKirch/uninteresting-bot/graphs/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.