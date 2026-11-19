[app]
title = Top Markeet
package.name = topmarkeet
package.domain = org.topmarkeet
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,requests,urllib3,chardet,idna,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
