function! Demo() abort
   exec "pyx" "import vim,os,sys"
   exec "pyx" "cwd = vim.eval('expand(\"<sfile>:p:h\")')"
   exec "pyx" "cwd = os.path.join(cwd,'autoload'); print(cwd)"
   exec "pyx" "sys.path.insert(0,cwd)"
   exec "pyx" "from generate_mkd_url import generate_mkd_url"
   exec "pyx" "path = 'autoload';suffix = 'vim';"
   exec "pyx" "ignore = '__init__.py'"
   exec "pyx" "print(generate_mkd_url(path,suffix,ignore))"
endfunction
call Demo()
