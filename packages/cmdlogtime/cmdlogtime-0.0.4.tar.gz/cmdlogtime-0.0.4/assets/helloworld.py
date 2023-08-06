#!/usr/bin/env python
#  need to import cmdlogtime
import cmdlogtime
from pathlib import Path
import sys

# need to specify a command line definition file.  See example command line definition file in this directory.
COMMAND_LINE_DEF_FILE = "helloworld_commandline.txt"


def main(out_dir, name, logfile=None):
    with open(Path(out_dir) / "hello.txt", "w") as f:
        f.write("Hello, " + name + "!")

    # if you want to add stuff to the logfile:
    if logfile:
        logfile.write("Hello'd complete.")


if __name__ == "__main__":
    # Call cmdlogtime.begin() at the beginning of main block
    (start_time_secs, pretty_start_time, my_args, logfile) = cmdlogtime.begin(
        COMMAND_LINE_DEF_FILE, sys.argv[0]
    )

    # the command line arguments will be in the my_args dictionary returned, so you can access them like this:

    main(my_args["out_dir"], my_args["name"], logfile)

    # Call cmdlogtime.end() at the end of main()
    cmdlogtime.end(logfile, start_time_secs)
    main()
