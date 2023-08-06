import os
import shutil
from mkdocs.plugins import BasePlugin


class MaterialVALighthousePlugin(BasePlugin):

    def __init__(self):
        self.enabled = True

    def on_pre_build(self, config):
        self.copy_over_css()
        self.copy_over_logo()

        return config

    @staticmethod
    def copy_over_logo():
        os.makedirs("docs/assets/images", exist_ok=True)
        logo_src_path = os.path.join(os.path.dirname(__file__), "lighthouse-logo-for-MKDocs.png")
        logo_dst_path = "docs/assets/images/lighthouse-logo-for-MKDocs.png"
        shutil.copyfile(logo_src_path, logo_dst_path)

    @staticmethod
    def copy_over_css():
        os.makedirs("docs/stylesheets", exist_ok=True)
        extra_css_path = "docs/stylesheets/extra.css"
        custom_css_path = os.path.join(os.path.dirname(__file__), "custom.css")
        shutil.copyfile(custom_css_path, extra_css_path)
