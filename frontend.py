"""Entrada do Streamlit: execute `streamlit run frontend.py` na raiz."""

from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent / "app" / "frontend.py"), run_name="__main__")
