
alias pr='cd ~/repositories/personal'
alias ur='cd ~/repositories/itu'
alias cpc="cd ~/dropbox/ITU/'code files'"

alias python3='python3.9'
alias pip3='pip3.9'
alias ituvpn='sudo openfortivpn sslvpn.itu.dk:443 --trusted-cert dd28d02edb94131bd84151c6aeee8ab5a88969a65d99ed9efa46b4507d75fcef --username=timp --realm=ITU'
alias op='nautilus . &'
# Monitor to camera - streams screen to camera output
alias mon2cam="deno run --unstable -A -r -q https://raw.githubusercontent.com/ShayBox/Mon2Cam/master/src/mod.ts"

function upload() {
    pp=$(realpath $1)
    python3 "$HOME/setupNdots/scripts/dataUpload.py" $1 $pp
}