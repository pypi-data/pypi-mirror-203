import unittest
import os

from . import toolkit
from . import versioning


def create_scaffold():
    return os.system(
        'npm install -g npm aws-cdk',
        'cdk init app --language python',
        'python -m venv .venv',
        '.venv/scripts/activate',
        'python -m pip install -U pip',
        'python -m pip install -r requirements.txt',
    )

def create_test_file(project_name):
    with open('tests/__init__.py') as file:
        file.write(f'''import jadecobra.toolkit

class Test{project_name}(jadecobra.toolkit.TestCase):

    def test_failure(self):
        self.assertFalse(True)'''
        )

def create_scent():
    with open('scent.py') as file:
        file.write("""import sniffer.api
import subprocess
watch_paths = ['tests/', 'src/']

@sniffer.api.runnable
def run_tests(*args):
    if subprocess.run(
        'python -m unittest -f tests/*.*',
        shell=True
    ).returncode == 0:
        return True""")


def create_tdd_cdk_project(project_name):
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    create_scaffold()
    os.remove('requirements-dev.txt')
    create_test_file(project_name)
    create_scent()
    os.system('sniffer')


class TestCase(unittest.TestCase):

    maxDiff = None

    def create_cdk_templates(self):
        '''Create CloudFormation using CDK with presets'''
        result = toolkit.run_in_shell(
            (
                'cdk ls '
                '--no-version-reporting '
                '--no-path-metadata '
                '--no-asset-metadata'
            )
        )
        self.assertEqual(result.returncode, 0)

    def assert_cdk_templates_equal(self, stack_name):
        '''Check if stack_name in cdk.out folder and tests/fixtures are the same'''
        self.assertEqual(
            toolkit.read_json(f"cdk.out/{stack_name}"),
            toolkit.read_json(f"tests/fixtures/{stack_name}")
        )

    def assert_attributes_equal(self, thing=None, attributes=None):
        '''Check that the given attributes match the attributes of thing'''
        self.assertEqual(
            sorted(dir(thing)), sorted(attributes)
        )