# 贪吃蛇（Kivy）Android APK

基于 Python + Kivy 的贪吃蛇小游戏，通过 Buildozer 在 GitHub Actions 的 Linux 容器中打包为 Android APK。

## 目录说明

- `main.py`：游戏主程序（Kivy 界面 + 触摸方向控制）
- `requirements.txt`：本地桌面运行依赖
- `buildozer.spec`：Buildozer 打包配置（应用名、包名、依赖、Android 参数）
- `.github/workflows/build-apk.yml`：GitHub Actions 自动构建 APK 工作流

## 本地桌面运行

```bash
pip install -r requirements.txt
python main.py
```

## 云端构建 APK

推送到仓库 `main` / `master` 分支，或在仓库 Actions 页面手动触发 `Build Android APK` 工作流。

1. 进入仓库 **Actions** 标签页，选择 `Build Android APK`
2. 等待构建完成（首次构建需下载 Android SDK/NDK，约 20–40 分钟）
3. 在本次运行页面底部 **Artifacts** 中下载 `snake-game-apk`，解压即得到 `bin/` 下的 debug APK，可安装到 Android 手机

## 包信息

- 应用名：贪吃蛇
- 包名：`org.yanghuangluo.snake`
- 版本：1.0.0
