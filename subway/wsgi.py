#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
import os

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=os.environ.get('DEBUG', False))
