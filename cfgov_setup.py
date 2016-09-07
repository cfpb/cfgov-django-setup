import os

from distutils.command.build_ext import build_ext as _build_ext
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

from setuptools import Command

from subprocess import call


class FrontEndBuildFailure(Exception):
    pass


class build_frontend(Command):
    """ A command class to run `setup.sh` """
    description = 'build front-end JavaScript and CSS'
    user_options = []
    possible_scripts = ['frontendbuild.sh', 'setup.sh']
    available_scripts = [script for script in possible_scripts
                         if os.path.exists(script)]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        script = self.available_scripts[0]

        exit_code = call(['sh', script])
        if exit_code > 0:
            raise FrontEndBuildFailure


class build_ext(_build_ext):
    """ A build_ext subclass that adds build_frontend """
    def run(self):
        self.run_command('build_frontend')
        _build_ext.run(self)


class bdist_egg(_bdist_egg):
    """ A bdist_egg subclass that runs build_frontend """
    def run(self):
        self.run_command('build_frontend')
        _bdist_egg.run(self)


class bdist_wheel(_bdist_wheel):
    """ A bdist_wheel subclass that runs build_frontend """
    def run(self):
        self.run_command('build_frontend')
        _bdist_wheel.run(self)


def do_frontend_build(dist, *args, **kwargs):
    commands = {
       'build_frontend': build_frontend,
       'build_ext': build_ext,
       'bdist_egg': bdist_egg,
       'bdist_wheel': bdist_wheel,
    }
    dist.cmdclass.update(commands)
