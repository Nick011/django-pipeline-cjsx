from __future__ import print_function

from pipeline.compilers import SubProcessCompiler
from os.path import dirname
from django.conf import settings


class CJSXCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('cjsx')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        command = "%s %s %s %s > %s" % (
            getattr(settings, 'PIPELINE_BROWSERIFY_VARS', ''),
            getattr(settings, 'PIPELINE_BROWSERIFY_BINARY', '/usr/bin/env browserify'),
            getattr(settings, 'PIPELINE_BROWSERIFY_ARGUMENTS', '-t coffee-reactify --extension=".cjsx" --extension=".coffee"'),
            infile,
            outfile
        )

        return self.execute_command(command, cwd=dirname(infile))

