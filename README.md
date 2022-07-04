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
> enter `vsm` (Vim Session Manager), it allows you to list, open, and remove sessions files, either interactively or by name.

## :superhero_man: Features

#### Current planned features

  * [x] Open session by name (regex filtered)
  * [x] Remove session by name (regex filtered)
  * [x] List all sessions
  * [x] Open and remove sessions from an interactive prompt
  * [x] Manages different vim variations (vim, nvim, gvim, macvim etc..)
  * [ ] Show programmer statistics for each session when listed

#### Current planned packaging 

  * [x] Build and install manually with poetry
  * [ ] Pip install from pypi
  * [ ] Install from AUR or clone and build with makepkg (Arch Users)

## Installing

> NOTE that the environment variable `VIM_SESSIONS` is expected on the system,
> if it is not defined `vsm` will default to `~/.config/vim_sessions` when it looks
> for your session files.

* bash/zsh `export VIM_SESSIONS="path/to/where/you/want/to/store/your/sessions"`

* fish `set -Ux VIM_SESSIONS "path/to/where/you/want/to/store/your/sessions"`


1. Clone the repo and build the package manually 

```bash
# This is the fast way
pip install git+https://github.com/mattcoding4days/vsm.git#egg=vim_session_manager --user

# you should now be able to use the program
vsm --help
```

2. Pip install from Pypi (Not available)

`pip install vim_session_manager`

3. Install from Arch User Repository (Not available)

`paru -S vim_session_manager`

4. Clone and makepkg (Not available)

```bash
# clone
git@github.com:mattcoding4days/vsm.git

# navigate into the directory
cd vsm/

# make the package
makepkg -cf

# you should now be able to use the program
vsm --help
```

## Usage



## :construction_worker: Development (for the contribution driven opensourcerer)

> The project is managed by [Python Poetry](https://python-poetry.org/) and uses python >= 3.10.1.
> Note: mypy static analyzing currently will not work as it does not yet support the match statement

### :keyboard: Commands to help you out

> NOTE: if you are installing poetry, DO NOT install it with pip
> `curl -sSL https://install.python-poetry.org | python3 -`

#### Install the package
`poetry install`

#### Run the tests to verify everything worked
`pytest`

#### Run the executable
`poetry run vsm`

#### You can pass command line arguments to executable through poetry

`poetry run vsm --help`

## :package: 3rd party libraries

> Vim Session Manager uses the following Python libraries

1. [result for Rust like elegance](https://github.com/rustedpy/result)

2. [inquirer for fancy prompt driven selection](https://pypi.org/project/inquirer/)

3. [rich, make terminal programs great again](https://github.com/Textualize/rich)

## :scroll: Documentation

> To be completed

## :mage: Contributing

> To be completed
