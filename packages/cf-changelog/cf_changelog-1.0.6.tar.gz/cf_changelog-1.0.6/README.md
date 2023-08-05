# cf_changelog - Conflict-Free Changelog manager

Simple tool to support changelog modifications on different git branches without conflicts on merging.
Written in python, installable with pip.

## Usage
1. Install it from pip:
```bash
pip install cf_changelog
```
2. Create some changelog on different branches entries using:
```bash
cf_changelog add
```
It is required to run this from root of your repository.
This will invoke standard text editor (or notepad/vim if standard editor is not configured), where you can fill a template with new features, bug fixes etc. 

Windows example:

![Windows_example of editor with changelog entry](img/windows_template_screenshot.png)

This is simple yaml format. You can use as many types of entries as you wish (New, Bugfix, Changed, Fixed, etc.). Each type should contain a flat list.
The most important thing is that you don't have to remember anything specific related to this tool, just fill in a template.

3. Commit newly created files.
4. Repeat 2 and 3 on different branches as many times as you need.
5. Merge all branches.
6. On merged branch run:

```bash
cf_changelog release X.Y.Z
```
where X.Y.Z is description of version you want to see in final changelog.

7. Commit registered changes in git repository (by default: Changelog.md and changelog directory).
8. Enjoy your updated changelog.

## How it works
  - `add` command creates files with unique names by default in changelog/sources. Since file names are unique there will be no conflict on merge.
  - `release` command parses those "source" files and adds them on the begining of Changelog.md. Then copies "source" files to "archive" just to keep them in history.
Those commands calls `git add` on created and modified files to remind you that you have to commit them.

## Project status
  - Manual tests on Windows passed
  - Manual tests on Ubuntu passed

