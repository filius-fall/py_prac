import os
import sys
import logging



with open("shell_output.txt","a") as sys.stdout:

    h = os.system("sudo du -h /home | sort -rh")

    print(h)


# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# ch = logging.StreamHandler()
# ch.setLevel(logging.info)

# logger.addHandler(ch)

