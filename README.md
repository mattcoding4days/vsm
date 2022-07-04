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
  * [x] Open sessions from an interactive prompt
  * [x] Batch session file removal from an interactive prompt
  * [x] Manages different vim variations (vim, nvim, gvim, macvim etc..)
  * [ ] Show programmer statistics for each session when listed

#### Current planned packaging 

  * [x] Pip install from this repo
  * [x] Build and install manually with poetry
  * [x] Pip install from pypi

## Installing

1. Install from pypi

> [Check it out on Pypi](https://pypi.org/project/vim-session-manager/#description)
`pip install vim-session-manager`

2. Pip Installing from the git repo

```bash
# Copy and run this command
pip install git+https://github.com/mattcoding4days/vsm.git#egg=vim_session_manager --user

# you should now be able to use the program
vsm --help
```

`pip install vim_session_manager`

## :mage: Usage

### Set up

> NOTE that an environement variable `VIM_SESSIONS` is expected on the system,
> if it is not defined `vsm` will default to `~/.config/vim_sessions` when it looks
> for your session files.

* bash/zsh `export VIM_SESSIONS="path/to/where/you/want/to/store/your/sessions"`

* fish `set -Ux VIM_SESSIONS "path/to/where/you/want/to/store/your/sessions"`

### Create session files easier

> Add the below snippet to your `.vimrc` or `init.vim` to make creating
> new session files much easier.

```vim
if isdirectory(expand($VIM_SESSIONS))
  nnoremap mk :mksession $VIM_SESSIONS/
  nnoremap mo :mksession! $VIM_SESSIONS/
else
  nnoremap mk :echo "VIM_SESSIONS directory does not exist, get vim session manager at https://github.com/mattcoding4days/vsm"<CR>
  nnoremap mo :echo "VIM_SESSIONS directory does not exist, get vim session manager at https://github.com/mattcoding4days/vsm"<CR>
endif
```

<div align="center">
  <h3>Exploring the help menu for subcommands</h3>
  <img width="800" height="300" src="assets/vsm_help.gif">
  <br>
</div>

<div align="center">
  <h3>Managing many variations of vim installed on the system</h3>
  <img width="800" height="300" src="assets/vsm_vim_variant.gif">
  <br>
</div>

<div align="center">
  <h3>Open a session file interactively</h3>
  <img width="800" height="300" src="assets/vsm_open_interactive.gif">
  <br>
</div>

<div align="center">
  <h3>Open session file by name</h3>
  <img width="800" height="300" src="assets/vsm_open_name.gif">
  <br>
</div>

<div align="center">
  <h3>Remove session file(s) interactively (one or many)</h3>
  <p>Note that only the arrow keys are supported for movement, and the space bar is used to select/unselect</p>
  <img width="800" height="300" src="assets/vsm_remove_interactive.gif">
  <br>
</div>

<div align="center">
  <h3>Remove a single session file by name (with regex matching)</h3>
  <img width="800" height="300" src="assets/vsm_remove_name.gif">
  <br>
</div>

## :construction_worker: Development

> The project is managed by [Python Poetry](https://python-poetry.org/) and uses python >= 3.10.1.
> Note: mypy static analyzing currently will not work as it does not yet support the match statement

### :keyboard: Commands to help you out

> NOTE: if you are installing poetry, DO NOT install it with pip
> `curl -sSL https://install.python-poetry.org | python3 -`

#### Install the package
`poetry install`

#### Run the tests to verify everything worked
`pytest`

#### Start a poetry shell and run the executable
`poetry shell`
`vsm --help`


## :package: 3rd party libraries

> Vim Session Manager uses the following Python libraries

1. [result for Rust like elegance](https://github.com/rustedpy/result)

2. [inquirer for fancy prompt driven selection](https://pypi.org/project/inquirer/)

3. [rich, make terminal programs great again](https://github.com/Textualize/rich)

## :scroll: Documentation

> To be completed
