alias pr="cd $HOME/repositories/personal"
alias ur="cd $HOME/repositories/itu"
alias cpc="cd $HOME/cloud/ITU/'Code Files'"

alias python3='python3.9'
alias pip3='pip3.9'
alias ituvpn='sudo openfortivpn sslvpn.itu.dk:443 --trusted-cert dd28d02edb94131bd84151c6aeee8ab5a88969a65d99ed9efa46b4507d75fcef --username=timp --realm=ITU'
alias op='nautilus . & &>/dev/null'

function dataUpload() {
    pp=$(realpath $1)
    python3 $HOME/repositories/personal/setupNdots/scripts/dataUpload.py $1 $pp
}

function kattis() {
    echo $personal_repos
    make -f $HOME/repositories/personal/setupNdots/scripts/kattis.mk $@
}

