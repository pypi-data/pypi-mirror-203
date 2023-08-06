import ast
import io
import json
import keyword
import shutil
import subprocess
import urllib.request
from pathlib import Path
from zipfile import ZipFile

VERSION = "6.4.0"
PKG_DIR = Path(__file__).parent.parent / "src" / "fonticon_fa6"
URL = "https://github.com/FortAwesome/Font-Awesome/releases/download/{0}/fontawesome-free-{0}-desktop.zip"  # noqa


def get_data(version, pkg_dir):
    font_dir = Path(pkg_dir) / "fonts"
    font_dir.mkdir(exist_ok=True)
    metadata = None
    otfs = []

    url = URL.format(version)
    with urllib.request.urlopen(url) as response:
        with ZipFile(io.BytesIO(response.read())) as thezip:
            for zipinfo in thezip.infolist():
                if zipinfo.filename.endswith(".otf") or "LICENSE" in zipinfo.filename:
                    dest = font_dir / Path(zipinfo.filename).name
                    with thezip.open(zipinfo) as source, open(dest, "wb") as target:
                        shutil.copyfileobj(source, target)
                        print("writing", dest)
                    if str(dest).endswith("otf"):
                        otfs.append(dest)
                elif zipinfo.filename.endswith("metadata/icons.json"):
                    with thezip.open(zipinfo) as f:
                        metadata = json.loads(f.read())
    out = []
    for otf in otfs:
        if "Brands" in str(otf):
            style = "brands"
        elif "Solid" in str(otf):
            style = "solid"
        else:
            style = "regular"

        charmap = {k: v["unicode"] for k, v in metadata.items() if style in v["styles"]}
        name = f"FA{version[0]}{style[0].upper()}"
        out.append((charmap, otf, name))
    return out


def normkey(key: str):
    if key[0].isdigit():
        key = "_" + key
    if keyword.iskeyword(key):
        key += "_"
    key = key.replace("-", "_")
    if not key.isidentifier():
        raise ValueError(f"not identifier: {key}")
    return key


TEMPLATE = """
from pathlib import Path

from ._iconfont import IconFont

FONTS = Path(__file__).parent / "fonts"


class {name}(IconFont):
    '''{doc}.'''
    __font_file__ = str(FONTS / "{file}")
""".strip()


def build(data, version, pkg):
    init = f"__version__ = {version!r}\n\n"
    _all = []

    for charmap, otf, name in data:
        code = TEMPLATE.format(name=name, doc=otf.stem, file=otf.name) + "\n\n"
        for key, glpyh in charmap.items():
            line = f"{normkey(key)} = '\\u{glpyh}'"
            try:
                ast.parse(line)
            except SyntaxError:
                continue
            code += f"    {line}\n"

        dest = Path(pkg) / f"{name.lower()}.py"
        dest.write_text(code)
        print("writing", dest)

        init += f"from .{name.lower()} import {name}\n"
        _all.append(name)

    init = f"__all__ = {_all!r}\n" + init
    (Path(pkg) / "__init__.py").write_text(init)
    print("writing __init__.py")


def main(version, root):
    build(get_data(version, root), version, root)
    subprocess.run(["pre-commit", "run", "--all-files"])


if __name__ == "__main__":
    main(version=VERSION, root=PKG_DIR)
