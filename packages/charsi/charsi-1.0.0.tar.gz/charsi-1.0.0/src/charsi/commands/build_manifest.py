from pathlib import Path

import click

from charsi.manifest import ManifestFile


@click.command('build-manifest')
@click.argument('manifest-file', metavar='FILE', type=click.Path(exists=True, dir_okay=False), required=True)
def build_manifest_command(manifest_file: str):
    manifest = ManifestFile()
    manifest.load_file(Path(manifest_file))

    for task in manifest.tasks:
        task.run()
