#!/usr/bin/env  python

import os
import django
import pydoc

# Prepare Django before executing pydoc command
os.environ['DJANGO_SETTINGS_MODULE'] = 'djp1.settings'
django.setup()

# Now executing pydoc
pydoc.cli()
