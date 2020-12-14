import os

from flask_assets import Bundle

from contentagregator import assets, app

dirs = ['static', 'modules']
for path in dirs:
    assets.append_path(os.path.join(app.root_path, path))

vendors_js = Bundle(
    'scripts/vendors/jquery-3.5.1.min.js',
    'scripts/vendors/popper.js',
    'scripts/vendors/jquery-ui.min.js',
    'scripts/vendors/bootstrap.min.js',
    output='scripts/vendors/vendors.js',
    filters='jsmin'
)

base_css = Bundle(
    'css/google_fonts.css',
    'css/vendors/normalize.min.css',
    'css/vendors/fontawesome.min.css',
    'css/vendors/bootstrap.min.css',
    'css/vendors/jquery-ui.min.css',
    'css/general.css',
    output='css/base.css',
    filters='cssmin'
)


assets.register('vendors_js', vendors_js)
assets.register('base_css', base_css)

def build():
    vendors_js.build()
    base_css.build()