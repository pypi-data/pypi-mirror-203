"""
Start-up program for emily version 0.9
This program is required to ensure emily.py is started as "emily0_9.emily" rather than "__main__", and therefore that relative module addressing works.
"""
# author R.N.Bosworth

# version 17 Mar 23  10:40
"""
Copyright (C) 2023  R.N.Bosworth

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License (gpl.txt) for more details.
"""

import sys
from emily0_9 import emily

emily.start(sys.argv)
