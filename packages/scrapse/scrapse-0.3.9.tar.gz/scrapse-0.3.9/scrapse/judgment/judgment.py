import typer
from scrapse.judgment.commands import extraction

judgment_app = typer.Typer()
judgment_app.command()(extraction.extraction)

"""
from scrapse.leggitalia.commands import dump_judgments
from scrapse.leggitalia.commands import scrap_voices
from scrapse.leggitalia.commands import save_cookie
from scrapse.leggitalia.commands import show_filters

leggitalia_app.command()(dump_judgments.dump_judgments)
leggitalia_app.command()(scrap_voices.scrap_voices)
leggitalia_app.command()(save_cookie.save_cookie)
leggitalia_app.command()(show_filters.show_filters)"""

@judgment_app.callback()
def callback():
    """Dedicated command to extraction"""


if __name__ == "__main__":
    judgment_app()
