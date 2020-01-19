#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

start() {
    echo "Start bot..."
	tmux new-session -d -s uninterestingBot \; send-keys /"cd $DIR ;python3 $DIR/run.py" Enter
}

stop() {
    echo "Stop bot..."
	tmux kill-session -t uninterestingBot
}

install() {
    echo "Install requirements..."
	pip3 install -r requirements.txt
}

update() {
    echo "Update..."
	cd $DIR 
    git clone https://github.com/TitusKirch/uninteresting-bot.git --branch feat/first_release tmp
    cp -a tmp/* $DIR
	chmod +x bot.sh
    rm -rf tmp
}

declare -a PackageArray=("python3" "python3-pip" "python3-setuptools" "tmux" "git")
missing_package=false

for pkg in "${PackageArray[@]}"; do
	if [ $(dpkg-query -W -f='${Status}' $pkg 2>/dev/null | grep -c "ok installed") -eq 1 ]; then
		:
	else
		read -p "$pkg is not installed. Do you want to install it? (y/n)" request
		if  [ $request == "y" ];then
			apt-get install $pkg
		else
			missing_package=true
		fi
	fi
done

if [ "$missing_package" = false ] ; then
    echo "All required packages were found."
	case "$1" in
		start)
			start
			;;
		stop)
			stop
			;;
		restart)
			stop
			start
			;;
		install)
			stop
			install
			;;
		update)
			stop
			update
			;;
		*)
			echo "Usage: $0 {start|stop|restart|install|update}" >&2
			exit 1
			;;
	esac
else
	echo "Unfortunately missing packets to start the bot."
fi
