
from flet import app, AppView

from src.app import *

if __name__ == "__main__":
    app(App, view=AppView.FLET_APP, assets_dir="src/ui/assets")
