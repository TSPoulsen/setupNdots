:set tabstop=4
:set shiftwidth=4
:set expandtab
:set autoindent

filetype on
filetype plugin on
filetype indent on " file type based indentation

" Makes makefiles use tabs instead of 4 spaces when pressing tab
autocmd FileType make,mk set noexpandtab shiftwidth=8 softtabstop=0


" Comments in Vimscript start with a `"`.

" If you open this file in Vim, it'll be syntax highlighted for you.
set nocompatible

" Disable the default Vim startup message.
set shortmess+=I

" Show line numbers.
set number

" Always show the status line at the bottom, even if you only have one window open.
set laststatus=2

" The backspace key has slightly unintuitive behavior by default. For example,
" by default, you can't backspace before the insertion point set with 'i'.
" This configuration makes backspace behave more reasonably, in that you can
" backspace over anything.
set backspace=indent,eol,start

set hidden

" This setting makes search case-insensitive when all characters in the string
" being searched are lowercase. However, the search becomes case-sensitive if
" it contains any capital letters. This makes searching more convenient.
set ignorecase
set smartcase

" Enable searching as you type, rather than waiting till you press enter.
set incsearch

" Unbind some useless/annoying default key bindings.
nmap Q <Nop> " 'Q' in normal mode enters Ex mode. You almost never want this.

" Disable audible bell because it's annoying.
set noerrorbells visualbell t_vb=

" Enable mouse support. You should avoid relying on this too much, but it can
" sometimes be convenient.
set mouse+=a

" Makes ctrl+backspace delete previous word in insert mode
noremap! <C-h> <C-w> 

" Try to prevent bad habits like using the arrow keys for movement. This is
" not the only possible bad habit. For example, holding down the h/j/k/l keys
" for movement, rather than using more efficient movement commands, is also a
" bad habit. The former is enforceable through a .vimrc, while we don't know
" how to prevent the latter.
" Do this in normal mode...
nnoremap <Left>  :echoe "Use h"<CR>
nnoremap <Right> :echoe "Use l"<CR>
nnoremap <Up>    :echoe "Use k"<CR>
nnoremap <Down>  :echoe "Use j"<CR>
" ...and in insert mode
inoremap <Left>  <ESC>:echoe "Use h"<CR>
inoremap <Right> <ESC>:echoe "Use l"<CR>
inoremap <Up>    <ESC>:echoe "Use k"<CR>
inoremap <Down>  <ESC>:echoe "Use j"<CR>

" Plugins using the vim-plug plugin plugin manager
" Automatically installs vim-plug if it isn't already
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif
call plug#begin()
Plug 'preservim/NERDTree'   " file overview/manager on the left side use command NERDTree to view file
Plug 'morhetz/gruvbox'      " Colorscheme plugin which includes langauge specific colouring
Plug 'dense-analysis/ale'   " linting for most filetypes
call plug#end()

let g:ale_sign_column_always = 1 " make so that sign column when editing is always show and doesn't pop in and out of existing shifting the whole screen
autocmd vimenter * ++nested colorscheme gruvbox " Not sure, but says to include this in the installation of gruvbox
" Sets transparent background
autocmd vimenter * hi Normal guibg=NONE ctermbg=NONE
set background=dark    " Setting dark mode
let NERDTreeShowHidden=1 " Makes so that NERDTree shows hidden files aswell by default
