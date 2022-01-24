<div align="center">
  <h1>Vim Session Manager</h1>
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/mattcoding4days/vsm?color=red&logo=github&style=for-the-badge">
</div>


> A manager for the under-utilized `:mksession` command in vim

## :information_source: Reasoning

> If you use vim or neovim on a daily basis and work in large codebases, it is probably not uncommon for you
> to have 10+ tabs open at a time, with various splits. Once you close this vim session the layout is lost to the ethers.
> the `mksession` command in vim(neovim) can save you, thus saving the session to a directory, promising to return you to your
> work exactly how you left it. However, the problem is most of us accrue many of these session files scattered about, personally
> I have 28 vim session files, easily loading them, rememembering the context of each one, and removing stale sessions becomes a hassle.
> enter `vsm` (Vim Session Manager), it is a script I wrote years ago that has been kicking about my dotfiles, and now is being revamped
> and written as an easily installable python package as some of my compatriots have expressed interest in using it.

## :construction_worker: Development (for the contribution driven opensourcer)

> The project is managed by [Python Poetry](https://python-poetry.org/),
> and uses python3 >= 3.10.1

### :keyboard: Commands to help you out

#### Install the package
`poetry install`

#### Run the tests to verify everything worked
`poetry run tests`

#### Run the executable
`poetry run drive`

#### You can pass commands to executable
`poetry run drive -r`

## :package: 3rd party libraries

> Vim Session Manager uses the following Python libraries

1. [result](https://github.com/rustedpy/result)

2. [halo](https://github.com/manrajgrover/halo)

3. [rich](https://github.com/Textualize/rich)
