> cat .vimrc
set nocompatible
"behave mswin
syntax on
set hls
set nu
set fileencoding=utf-8
set encoding=utf-8
set nocompatible
set backspace=indent,eol,start
color desert
set showcmd
set go-=T
set paste
set nowrap
"set autoindent
"set mouse=v
set backspace=2
set tabstop=4
set smartindent
set softtabstop=4
set ai!
set ruler
"set cursorline
set shortmess=atI
set novisualbell
set list
"set listchars=tab:>.,trail:.
set listchars=tab:>.
set laststatus=2
"set fdm=marker
"set foldlevel=1
set clipboard=unnamed
set shiftwidth=4
set textwidth=79
set expandtab
"set autoindent
set fileformat=unix


filetype off
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'kien/ctrlp.vim'
Plugin 'tpope/vim-fugitive'
"Plugin 'Lokaltog/powerline',{'rtp': 'powerline/bindings/vim/'}

"Plugin 'Valloric/YouCompleteMe'
Bundle 'Valloric/YouCompleteMe'


" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required


let python_highlight_all=1

let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

"call togglebg#map("<F5>")



"filetype plugin on
"let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict'
"let g:pydiction_menu_height = 3
