import typer

import vidya.transform

app = typer.Typer()


app.add_typer(vidya.transform.app, name="transform")
