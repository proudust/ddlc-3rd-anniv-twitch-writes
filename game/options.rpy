define build.name = "Twitch Writes Mod"
define build.destination = "dists"
define build.directory_name = build.name.replace(" ", "_")

define config.developer = True
define config.layers = [ "master", "transient", "screens", "overlay", "front" ]

init python hide:
    # Run git describe
    try:
        import subprocess
        describe = subprocess.check_output(["git", "-C", config.basedir, "describe", "--tags"], shell=True)
        config.version = str(describe[1:-1])
    except subprocess.CalledProcessError:
        pass

    package_name = ("v" + config.version) if config.version != "" else "unknown"
    build.package("v" + config.version, "zip", build.name, description="DDLC Compatible Mod")

    build.archive("twitch-writes", build.name)
    build.classify("game/tl/Japanese/twitch-writes.rpyc", "twitch-writes")
    build.classify("game/twitch-writes.rpyc", "twitch-writes")

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.rpy", None)
    build.classify("**.psd", None)
    build.classify("**.sublime-project", None)
    build.classify("**.sublime-workspace", None)
    build.classify("/music/*.*", None)
    build.classify("script-regex.txt", None)
    build.classify("/game/10", None)
    build.classify("/game/cache/*.*", None)

    build.classify("**.rpa", None)
    build.classify("options.rpy", None)

    # Copy README.txt
    import shutil
    shutil.copy(config.basedir + "/README.md", config.basedir + "/README.txt")
    build.classify("README.txt", build.name)
    build.classify("ddmm-mod.json", build.name)

    build.include_old_themes = False
