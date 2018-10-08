#!/usr/bin/python3
import json
import sys


try:
    obj = json.load(sys.stdin)
    text = json.dumps(obj)

except Exception as ex:
    sys.stderr.write(f"error: {ex}")

    sys.exit(1)

else:
    sys.stdout.write(text)

    sys.exit(0)
