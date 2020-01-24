#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/"
cd $DIR

update() {
    # get all textes in python files
    find . -iname "*.py" | xargs xgettext -d base -p languages

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

generate() {
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

case "$1" in
	update)
		update
	;;
	generate)
		generate
	;;
	*)
		echo "Usage: $0 {update|generate}" >&2
		exit 1
	;;
esac