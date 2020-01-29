#!/bin/bash

# config
tmux_session="uninterestingBot"

# setup system variables
app_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/"
declare -a required_packages=("python3" "python3-pip" "python3-setuptools" "tmux" "git")
missing_package=false

# go to application dir
cd $app_dir

# all functions
start() {
    echo "Start bot..."
	tmux new-session -d -s $tmux_session \; send-keys /"cd $app_dir ;python3 run.py" Enter
}
stop() {
    echo "Stop bot..."
	tmux kill-session -t $tmux_session
}
restart() {
    start
    stop
}
update_files() {
    # update by cloning from github
    echo "Update..."
	cd $app_dir 
    git clone https://github.com/TitusKirch/uninteresting-bot.git --branch feat/first_release tmp
    cp -a tmp/* $app_dir
	chmod +x bot.sh
    rm -rf tmp
}
update_requirements() {
    # install all requirements
    echo "Install requirements..."
	pip3 install -r requirements.txt
}
update_all() {
    update_clone
    update_requirements
}
language_update() {
    # get all textes in python files
    find . -iname "*.py" | xargs xgettext -d base -p languages -L Python

    # cd to languages folder 
    cd languages/

    # update all languages
    for d in */
    do
        # check if base.po exist and if not, create one
        if [ ! -f ${d%/}/LC_MESSAGES/base.po ]; then
            echo "\"languages/"${d%/}"/LC_MESSAGES/base.po\" not found!"
            touch ${d%/}/LC_MESSAGES/base.po
            echo "\"languages/"${d%/}"/LC_MESSAGES/base.po\" has now been created!"
        fi

        # merge langauge file
        msgmerge --update ${d%/}/LC_MESSAGES/base.po base.po
    done
}
language_generate() {
    # cd to languages folder 
    cd languages/

    # update all languages
    for d in */
    do
        # check if base.po exist and if not, create one
        if [ -f ${d%/}/LC_MESSAGES/base.po ]; then
            # generate .mo file
            echo ${d%/}/LC_MESSAGES/base.mo ${d%/}/LC_MESSAGES/base
            msgfmt -o ${d%/}/LC_MESSAGES/base.mo ${d%/}/LC_MESSAGES/base
            echo "\"languages/"${d%/}"/LC_MESSAGES/base.mo\" was generated!"
        fi
    done
}

# check all required packages
for pkg in "${required_packages[@]}"; do
    # check if pkg is installed
	if [ $(dpkg-query -W -f='${Status}' $pkg 2>/dev/null | grep -c "ok installed") -eq 1 ]; then
		:
	else
        # ask to install pkg
		read -p "$pkg is not installed. Do you want to install it? (y/n)" request
		if  [ $request == "y" ];then
			apt-get install $pkg
		else
			missing_package=true
		fi
	fi
done

# check for command
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
			restart
			;;
		update)
            case "$2" in
                all)
                    stop
                    update_all
                ;;
                files)
                    stop
                    update_files
                ;;
                requirements)
                    stop
                    update_requirements
                ;;
                *)
                    echo "Usage: $0 $1 {all|files|requirements}" >&2
                    exit 1
                    ;;
	        esac
            ;;
        language)
            case "$2" in
                update)
                    language_update
                ;;
                generate)
                    language_generate
                ;;
                *)
                    echo "Usage: $0 $1 {update|generate}" >&2
                    exit 1
                    ;;
	        esac
            ;;
		*)
			echo "Usage: $0 {start|stop|language}" >&2
			exit 1
			;;
	esac
else
	echo "Unfortunately not all required packages are installed."
fi
