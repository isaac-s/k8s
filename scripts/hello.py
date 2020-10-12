#!/usr/bin/env python

from cloudify import ctx

ctx.logger.info("Hello world")
ctx.instance.runtime_properties['host'] = "https://cloudify.co"
ctx.instance.runtime_properties['port'] = 8080
