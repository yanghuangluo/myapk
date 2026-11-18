[app]

# 应用版本号
version = 1.0.0

# 应用标题（显示在手机桌面）
title = 贪吃蛇

# 包名与包域名，最终包名为 org.yanghuangluo.snake
package.name = snake
package.domain = org.yanghuangluo

# 源码目录与需要打包的扩展名
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_dirs = tests, bin, .buildozer, .git, __pycache__

# 运行依赖：python3 为 p4a 引导，kivy 为界面框架
requirements = python3,kivy

# 屏幕方向：portrait 竖屏 / landscape 横屏 / all 横竖均可
orientation = portrait

# Android 构建参数
android.minapi = 21
android.ndk = 23b
android.api = 33
# CI 自动化：自动接受 Android SDK 许可协议，避免卡在 Accept? (y/N)
android.accept_sdk_license = True

# 图标（可选，放到 icons 目录后取消注释）
# icon.filename = %(source.dir)s/icons/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
