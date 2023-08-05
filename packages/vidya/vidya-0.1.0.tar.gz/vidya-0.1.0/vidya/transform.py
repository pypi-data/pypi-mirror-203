
import typer
from rich import print

from vidya.utils.css_to_csv import transform_css_to_csv
from vidya.utils.os import create_dir_if_not_exists


app = typer.Typer()


@app.command()
def css_to_csv(
    css_file: typer.FileText = typer.Argument(
        ...,
        help="CSS file to transform"
    ),
    csv_file: typer.FileTextWrite = typer.Option(
        None, "--output", "-o", help="Output CSV file"
    )
):
    try:
        print("Transforming CSS to CSV")
        if csv_file is None:
            csv_file_name = css_file.name.replace(".css", ".csv")
            csv_file = open(csv_file_name, "w", encoding="utf-8")

        create_dir_if_not_exists(csv_file.name)
        transform_css_to_csv(css_file, csv_file)
        print(f"Saved to {csv_file.name}")
    except Exception as e:
        print(f"Error transforming CSS to CSV: {e}")
        raise typer.Abort()
    finally:
        csv_file.close()
