import os
import shutil
import yaml
from mkdocs.plugins import BasePlugin


class MkdocsMaterialVaLighthousePlugin(BasePlugin):

    def __init__(self):
        self.mkdocs_data = None
        self.enabled = True

    def on_pre_build(self, config):
        os.makedirs("docs/stylesheets", exist_ok=True)
        extra_css_path = "docs/stylesheets/extra.css"
        custom_css_path = os.path.join(os.path.dirname(__file__), "custom.css")

        shutil.copyfile(custom_css_path, extra_css_path)

        with open("mkdocs.yml", "r") as mkdocs_file:
            self.mkdocs_data = yaml.safe_load(mkdocs_file)

        self.insert_logo()
        self.insert_css()

        with open("mkdocs.yml", "w") as mkdocs_file:
            yaml.safe_dump(self.mkdocs_data, mkdocs_file, default_flow_style=None, sort_keys=False)

        return config

    def insert_css(self):
        if "extra_css" not in self.mkdocs_data:
            self.mkdocs_data["extra_css"] = []
        if "stylesheets/extra.css" not in self.mkdocs_data["extra_css"]:
            self.mkdocs_data["extra_css"].append("stylesheets/extra.css")

    def insert_logo(self):
        if "theme" not in self.mkdocs_data:
            self.mkdocs_data["theme"] = {}
        if "logo" not in self.mkdocs_data["theme"]:
            self.mkdocs_data["theme"]["logo"] = "assets/images/lighthouse-logo-for-MKDocs.png"
