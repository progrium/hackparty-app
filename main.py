import sys, os

package_dir = "pkgs"
package_dir_path = os.path.join(os.path.dirname(__file__), package_dir)

# Allow unzipped packages to be imported
# from packages folder
sys.path.insert(0, package_dir_path)

# Append zip archives to path for zipimport
for filename in os.listdir(package_dir_path):
    if filename.endswith((".zip", ".egg")):
        sys.path.insert(0, "%s/%s" % (package_dir_path, filename))

from hackparty import app

def main():
    from google.appengine.ext.webapp.util import run_wsgi_app
    run_wsgi_app(app)

# Use App Engine app caching
if __name__ == "__main__":
    main()
