<div align="center">
  <h1>Vim Session Manager</h1>
  <p>A manager for the under-utilized `mksession` command in vim</p>
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/mattcoding4days/vsm?color=red&logo=github&style=for-the-badge">
  <img alt="GitHub" src="https://img.shields.io/github/license/mattcoding4days/vsm?color=green&logo=github&style=for-the-badge">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mattcoding4days/vsm?color=blue&logo=github&style=for-the-badge">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/mattcoding4days/vsm?logo=github&style=for-the-badge">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/mattcoding4days/vsm?color=orange&logo=github&style=for-the-badge">
  <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/mattcoding4days/vsm?label=Source%20Lines%20of%20code&logo=github&style=for-the-badge">
</div>

## :information_source: Reasoning

> If you use vim or neovim on a daily basis and work in large codebases, it is probably not uncommon for you
> to have 10+ tabs open at a time, with various splits. Once you close this vim session the layout is lost to the ethers.
> the `mksession` command in vim(neovim) can save you, thus saving the session to a directory, promising to return you to your
> work exactly how you left it. However, the problem is most of us accrue many of these session files scattered about, personally
> I have 28 vim session files, easily loading them, rememembering the context of each one, and removing stale sessions becomes a hassle.
> enter `vsm` (Vim Session Manager), it is a script I wrote years ago that has been kicking about my dotfiles, and now is being revamped
> and written as an easily installable python package as some of my compatriots have expressed interest in using it.

## :superhero_man: Features

#### Current planned features

  * [x] Open session by name (regex filtered)
  * [x] Remove session by name (regex filtered)
  * [x] List all sessions
  * [ ] Show programmer statistics for each session

## :construction_worker: Development (for the contribution driven opensourcer)

> The project is managed by [Python Poetry](https://python-poetry.org/) and uses python >= 3.10.1.
> Note: mypy static analyzing currently will not work as it does not yet support the match statement

### :keyboard: Commands to help you out

#### Install the package
`poetry install`

#### Run the tests to verify everything worked
`poetry run tests`

#### Run the executable
`poetry run drive`

#### You can pass command line arguments to executable through poetry

1. `poetry run drive --help`

2. `poetry run drive --open-session <session>`

3. `poetry run drive --remove-session <session>`

4. `poetry run drive --the-current-state-of-things`

## :package: 3rd party libraries

> Vim Session Manager uses the following Python libraries

1. [result for Rust like elegance](https://github.com/rustedpy/result)

2. [halo fancy spinner library](https://github.com/manrajgrover/halo)

3. [rich, make terminal programs great again](https://github.com/Textualize/rich)

## :scroll: Documentation

> To be completed


## :mage: Contributing

> To be completed
