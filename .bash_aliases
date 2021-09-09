

personal_repos=

alias pr="cd $HOME/repositories/personal"
alias ur='cd ~/repositories/itu'
alias cpc="cd $HOME/cloud/ITU/'Code Files'"

alias python3='python3.9'
alias pip3='pip3.9'
alias ituvpn='sudo openfortivpn sslvpn.itu.dk:443 --trusted-cert dd28d02edb94131bd84151c6aeee8ab5a88969a65d99ed9efa46b4507d75fcef --username=timp --realm=ITU'
alias op='nautilus . & &>/dev/null'
# Monitor to camera - streams screen to camera output
alias mon2cam="deno run --unstable -A -r -q https://raw.githubusercontent.com/ShayBox/Mon2Cam/master/src/mod.ts"

function dataUpload() {
    pp=$(realpath $1)
    python3 $HOME/repositories/personal/setupNdots/scripts/dataUpload.py $1 $pp
}

function kattis() {
    echo $personal_repos
    make -f $HOME/repositories/personal/setupNdots/scripts/kattis.mk $@
}

unset personal_repos
