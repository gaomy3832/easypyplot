# /bin/bash

# Install dependencies in the given order with `pip`.

# Get {opts} wrapped between "--optsbeg" and "--optsend".
if [ "$1" == "--optsbeg" ]; then
    shift 1
    while [ "$#" -gt 0 ]; do
        arg=$1
        shift 1
        if [ "${arg}" == "--optsend" ]; then
            break
        else
            opts+=(${arg})
        fi
    done
fi

# Get the number of ordered deps.
if [ "$#" -ge 1 ]; then
    num=$1
    shift 1
    if [ "${num}" -gt "$#" ]; then
        num=""
    fi
fi

# Check arguments.
if [ -z "${num}" ]; then
    echo "Usage: $0 --optsbeg <opts> --optsend <N> <dep 1> ... <dep N> <packages>"
    exit 1
fi

# Ordered deps.
for ((i=1; i<=${num}; i++)); do
    pip install ${opts[@]} $1
    shift 1
done

# Other deps.
[ "$#" -gt 0 ] && pip install ${opts[@]} $@

