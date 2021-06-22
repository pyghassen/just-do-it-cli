# Just Do It CLI

![Created by](https://img.shields.io/badge/Created%20by-Ghassen%20Telmoudi%20%C2%A9-blue)
![GitHub](https://img.shields.io/github/license/pyghassen/just-do-it-cli)

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/pyghassen/just-do-it-cli/Just%20Do%20it%20CLI?logo=github)
[![codecov](https://codecov.io/gh/pyghassen/just-do-it-cli/branch/master/graph/badge.svg?token=8JI1NOE6PO)](https://codecov.io/gh/pyghassen/just-do-it-cli)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8f988bfd9a184950bc3f681f6130c0e5)](https://www.codacy.com/gh/pyghassen/just-do-it-cli/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pyghassen/just-do-it-cli&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/aa5d2559a2ff5009093d/maintainability)](https://codeclimate.com/github/pyghassen/just-do-it-cli/maintainability)
![Code Climate issues](https://img.shields.io/codeclimate/issues/pyghassen/just-do-it-cli?logo=codeclimate)
![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/pyghassen/just-do-it-cli?logo=codeclimate)
![Lines of code](https://img.shields.io/tokei/lines/github/pyghassen/just-do-it-cli)

![GitHub issues](https://img.shields.io/github/issues-raw/pyghassen/just-do-it-cli?logo=github)
![GitHub pull requests](https://img.shields.io/github/issues-pr/pyghassen/just-do-it-cli?logo=github)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/pyghassen/just-do-it-cli?logo=github)
![GitHub last commit](https://img.shields.io/github/last-commit/pyghassen/just-do-it-cli?logo=github)
![GitHub Repo stars](https://img.shields.io/github/stars/pyghassen/just-do-it-cli?style=social)

Just do it was created to solve some of the most common issues that us developers have to deal with.

You guessed it right, this tool gonna change the fact that you have to deal with "zoom meetings", "google meet" or whatever meetings on daily basis.

Sounds intriguing?

I think a lot of people have solved that in more creative way, just check tiktok or maybe youtube if you are an old fart.

However Just Do It CLI will help you deal with some of the annoying things like switching focus and organizing your daily tasks without the mental torture of using a corporate tool like Jira.

How you gonna achieve that, that's a fair question, here's how it works.
After finishing installing this tool, just create some boards to organize your daily tasks without the need leaving your terminal.

By the way, if you are a terminal hater, maybe you won't stomach it.

## Installation

Clone the repository

    git clone git@github.com:pyghassen/just-do-it-cli.git

Go inside the cloned repository directory

    cd just-do-it-cli

Run the installation command

    make install

## Usage

First you need to create a board and then create some tasks inside that board, you can get more help when you type the following command to get you started:

    justdoit --help

    Usage: justdoit [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      begin         Delete task.
      check         Mark task as done.
      create-board  Create Board.
      create-task   Create Task.
      delete-board  Delete board.
      delete-task   Delete Task.
      edit-board    Edit board.
      edit-task     Edit task.
      list          List all boards and tasks.
      priority      Set task priority from 1 to 5.
