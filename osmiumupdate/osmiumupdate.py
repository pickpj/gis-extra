import subprocess
import os
from pathlib import Path

downloadpath = os.path.expanduser("~/Websites")
mapfile = os.path.expanduser("~/Documents/cod/python/osmupdate/us-latest.osm.pbf")
geofabrikurl = "https://download.geofabrik.de/north-america/us-updates/"

def dl_diff():
    wget = ["wget", "-np", "-m", "-P", downloadpath, geofabrikurl]
    wg = subprocess.run(wget)
    if not wg.returncode:
        return True
    return False


def applydiff():
    lastupd = os.path.getmtime(mapfile)
    diff = [x for x in list(Path(downloadpath).rglob("*.osc.gz")) if x.stat().st_mtime > lastupd]

    if not diff:
        subprocess.call("echo No new change files found > /dev/pts/0", shell=True)
        return False

    subprocess.run(["mv", "-f", mapfile, os.path.dirname(mapfile)+"/us-prev.osm.pbf"])

    osmiumdiff = ["osmium", "apply-changes", "-Oo", mapfile, os.path.dirname(mapfile)+"/us-prev.osm.pbf", *[str(f) for f in diff]]
    od = subprocess.run(osmiumdiff)

    if not od.returncode:
        return True
    return False


def main():
    if not dl_diff():
        subprocess.run("echo Osmium Map Update failed during download > /dev/pts/0", shell=True)
        return

    if not applydiff():
        subprocess.run("echo Osmium Map Update failed during merge > /dev/pts/0", shell=True)
        return

if __name__ == "__main__":
    main()