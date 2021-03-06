#!/usr/bin/env python3
data = "\t  \nabc  def\t  \n"

# The strip method removes leading and trailing
# whitespace
result = data.strip()
print(len(data), ":", len(result))

# The rstrip method removes trailing whitespace
result = data.rstrip()
print(len(data), ":", len(result))

# The lstrip method removes leading whitespace
result = data.lstrip()
print(len(data), ":", len(result))
