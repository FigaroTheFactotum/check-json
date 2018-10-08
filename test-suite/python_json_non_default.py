#!/usr/bin/python3
import json
import sys
from decimal import Decimal

class Encoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Decimal):
            return o.to_eng_string()

        return json.JSONEncoder.default(self, o)


try:
    obj = json.load(sys.stdin, parse_float=Decimal)
    text = json.dumps(obj, allow_nan=False, cls=Encoder)

except Exception as ex:
    sys.stderr.write(f"error: {ex}")

    sys.exit(1)

else:
    sys.stdout.write(text)

    sys.exit(0)
