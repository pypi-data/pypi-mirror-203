import click
from wavescout import WaveScout, WaveScoutFactory
import os

@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.option("--export_slices", is_flag=True, help="Export audio slices as a zip file.")
@click.argument("output_path", type=click.Path())
@click.option("--measures_per_slice", type=int, default=16, help="Number of measures per slice.")

def main(input_path, export_slices, output_path, measures_per_slice):
    if os.path.isfile(input_path):
        scout = WaveScout(input_path)
        output_base = os.path.splitext(os.path.basename(input_path))[0]
        scout.export(os.path.join(output_path, f"{output_base}_beat_map.txt"))

        if export_slices:
            scout.export(os.path.join(output_path, f"{output_base}_slices.zip"), export_slices=True, measures_per_slice=measures_per_slice)
    elif os.path.isdir(input_path):
        factory = WaveScoutFactory(input_path)
        maps = factory.create_maps()

        for map in maps:
            map.export(os.path.join(output_path, f"{map.input_file_basename}_beat_map.txt"))

            if export_slices:
                map.export(os.path.join(output_path, f"{map.input_file_basename}_slices.zip"), export_slices=True)
    else:
        click.echo(f"Invalid input path: {input_path}")

if __name__ == "__main__":
    main()