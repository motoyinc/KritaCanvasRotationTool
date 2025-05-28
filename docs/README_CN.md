<h1 align="center">🌀 Krita 画布旋转工具</h1>

<p align="center">
  精细控制画布旋转的 Krita Python 插件<br>
  ショートカットでキャンバス回転を精密にコントロールできる Krita 用 Python プラグイン<br>
  A Krita plugin for smooth and precise canvas rotation via shortcuts.
</p>


<p align="center">
  <a href="/docs/README_CN.md">中文</a>
  ·
  <a href="https://github.com/motoyinc/KritaCanvasRotationTool/blob/master/README.md">English</a>
  ·
  <a href="/docs/README_JP.md">日本語</a>
</p>


---


<br>



## ✨ 功能特色

* 🎯 **微调旋转**
  以 0.1° ～ 5.0° 的精度进行小幅旋转，适合进行细致的画布调整和手动控制。

<p align="center">
<img src="https://github.com/user-attachments/assets/0833f353-807e-4098-a4c1-504cf7856f69" width="400px" />
</p>

* 🌀 **对齐吸附的大幅旋转**
  快速对齐到固定角度（例如 15°、30°、45° 等）。

<p align="center">
<img src="https://github.com/user-attachments/assets/7a4435da-0ec6-40e2-b3ad-f55cdefc60d6" width="400px" />
</p>

* ⚙️ **旋转步长可自定义**
  在 `Rotation Setting` 设置窗口中，你可以分别设置微调与粗调旋转角度：

<p align="center">
<img src="https://github.com/user-attachments/assets/5ebc084e-d438-433d-81d7-962f114055f1" width="200px" />
</p>

* 🎮 **快捷键友好设计**
  默认快捷键如下：

  ```
  Ctrl + 4 → 微调逆时针旋转  
  Ctrl + 6 → 微调顺时针旋转  
  Alt  + 4 → 粗调逆时针旋转  
  Alt  + 6 → 粗调顺时针旋转
  ```

* 🧩 **完全集成至 Krita 菜单**
  插件入口可在此找到：
  `工具（Tools）> 脚本（Scripts）> Krita Canva Rotation Tool`

<p align="center">
<img src="https://github.com/user-attachments/assets/d2daf112-5413-40d7-9b38-bbcef72780c8" width="600px" />
</p>

<br>
<br>
<br>


## 📦 安装方式

### 第一步：下载插件

> 前往本仓库的 [releases](https://github.com/motoyinc/KritaCanvasRotationTool/releases) 页面，下载最新的 `KritaCanvasRotationTool.zip
` 文件。  
> ⚠️ **不要解压**，保持为 `.zip` 格式。

<br>

### 第二步：在 Krita 中导入插件

> 打开 Krita  
> 菜单栏选择：`工具 > 脚本 > 从文件打开 Python 插件`  
> 选择刚才下载的 `KritaCanvasRotationTool.zip`
 文件  
> 导入完成后，**重启 Krita**

<p align="center">
<img src="https://github.com/user-attachments/assets/b8d6a779-7d50-45aa-bcc0-95b43f26728c" width="600px" />
</p>


### 第三步：启用插件

> 打开：`设置 > 配置 Krita > Python 插件管理器`  
> 找到 `Krita Canvas Rotation Tool` 插件，勾选启用 ✅  
> 点击“确定”，并**再次重启 Krita**

<p align="center">
<img src="https://github.com/user-attachments/assets/2fe2a259-b485-47db-a299-3406c381a93e" width="600px" />
</p>


<br>
<br>
<br>


## 🛠️ 使用方法


1. 打开 **Krita**，点击顶部菜单：
   **`工具 > 脚本 > Krita Canva Rotation Tool`**

   <p align="center">
   <img src="https://github.com/user-attachments/assets/8fd21413-6b49-4fb2-8bcf-c3df13a3916a" width="600px" />
   </p>

2. 在该菜单中，你将看到多个旋转操作：

   * **Rotation Setting**：打开设置窗口，可以配置：

     * **微调步进值**（Micro Rotate Step）：小幅旋转角度（如 0.1°–5.0°）
     * **粗调步进值**（Coarse Rotate Step）：大幅吸附角度（如 15°、30° 等）

   <p align="center">
   <img src="https://github.com/user-attachments/assets/5ebc084e-d438-433d-81d7-962f114055f1" width="200px" />
   </p>

3. 菜单中还包含以下旋转命令：

   * **Coarse Rotate Canvas + / -** → 大步旋转（如 15°）
   * **Micro Rotate Canvas + / -** → 小步精细旋转

   <p align="center">
   <img src="https://github.com/user-attachments/assets/d2daf112-5413-40d7-9b38-bbcef72780c8" width="600px" />
   </p>

4. 你可以在以下路径修改快捷键设置：
   **`设置 > 配置 Krita > 快捷键`**

   <p align="center">
   <img src="https://github.com/user-attachments/assets/31ddce83-4b50-4f87-a124-f3a72545396d" width="600px" />
   </p>



