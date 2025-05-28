<h1 align="center">🌀 Krita Canvas Rotation Tool</h1>

<p align="center">
  精细控制画布旋转的 Krita Python 插件<br>
  ショートカットでキャンバス回転を精密にコントロールできる Krita 用 Python プラグイン<br>
  A Krita plugin for smooth and precise canvas rotation via shortcuts.
</p>


  <p align="center">
    <a href="/docs/README_CN.md">中文</a>
    ·
    <a href="README.md">Englins</a>
    ·
    <a href="/docs/README_JP.md">日本語</a>
  </p>


---


<br>



## ✨ Features

* 🎯 **Micro Rotation**
  Rotate the canvas in small, precise steps (e.g. 0.1° \~ 5.0°).
  Useful for fine adjustments and manual control.

<p align="center">
<img src="https://github.com/user-attachments/assets/0833f353-807e-4098-a4c1-504cf7856f69" width="400px" />
</p>

* 🌀 **Coarse Rotation with Snap Alignment**
  Snap the canvas to the nearest fixed angles (e.g. 15°, 30°, 45°...).


<p align="center">
<img src="https://github.com/user-attachments/assets/7a4435da-0ec6-40e2-b3ad-f55cdefc60d6" width="400px" />
</p>

* ⚙️ **Customizable Step Settings**
  You can set both micro and coarse rotation step values via the `Rotation Setting` dialog:

<p align="center">
<img src="https://github.com/user-attachments/assets/5ebc084e-d438-433d-81d7-962f114055f1" width="200px" />
</p>

* 🎮 **Keyboard Shortcut Friendly**
  Default key bindings:

  ```
  Ctrl + 4 → Micro Rotate Counterclockwise  
  Ctrl + 6 → Micro Rotate Clockwise  
  Alt  + 4 → Coarse Rotate Counterclockwise  
  Alt  + 6 → Coarse Rotate Clockwise
  ```

* 🧩 **Integrated with Krita Menu**
  Easily accessible from:
  `Tools > Scripts > Krita Canva Rotation Tool`

<p align="center">
<img src="https://github.com/user-attachments/assets/d2daf112-5413-40d7-9b38-bbcef72780c8" width="600px" />
</p>

<br>
<br>
<br>




## 📦 Installation


### Step 1：Download the Plugin

> Go to the [releases](https://github.com/motoyinc/KritaCanvasRotationTool/releases) section of this repository and download the latest `KritaCanvasRotationTool.zip
` file.  
> ⚠️ **Do not unzip it** — keep the file as `.zip`.

<br>

### Step 2：Install in Krita

> Open Krita  
> Go to: `Tools > Scripts > Import Python Plugin from File`  
> Select the downloaded `KritaCanvasRotationTool.zip` file  
> After import, **restart Krita** to apply the plugin

<p align="center">
<img src="https://github.com/user-attachments/assets/796bb903-c394-48d6-8543-9fb4ca4ba5a9" width="600px" />
</p>


### Step 3：Enable the Plugin

> Go to: `Settings > Configure Krita > Python Plugin Manager`  
> Locate `Krita Canvas Rotation Tool`, check the box to enable ✅  
> Click OK and **restart Krita** again

<p align="center">
<img src="https://github.com/user-attachments/assets/27aeec63-e282-4221-9adf-be1a713018c7" width="600px" />
</p>

<br>
<br>
<br>


## 🛠️ How to Use

1. Open **Krita**, go to the top menu:
   **`Tools > Scripts > Krita Canva Rotation Tool`**

<p align="center">
<img src="https://github.com/user-attachments/assets/8fd21413-6b49-4fb2-8bcf-c3df13a3916a" width="600px" />
</p>


2. Inside this menu, you will find several rotation actions:

   * **Rotation Setting**: Open a settings dialog where you can customize:

     * **Micro Rotate Step**: the small rotation amount (e.g. 0.1°–5.0°)
     * **Coarse Rotate Step**: the larger, snap-based rotation amount (e.g. 15°, 30°, etc.)

<p align="center">
<img src="https://github.com/user-attachments/assets/5ebc084e-d438-433d-81d7-962f114055f1" width="200px" />
</p>


3. The menu also provides these rotation commands:

   * **Coarse Rotate Canvas + / -** → Large step rotation (e.g. 15°)
   * **Micro Rotate Canvas + / -** → Small incremental rotation

<p align="center">
<img src="https://github.com/user-attachments/assets/d2daf112-5413-40d7-9b38-bbcef72780c8" width="600px" />
</p>


4. You can assign or change shortcuts for these actions from
   **`Settings > Configure Krita > Keyboard Shortcuts`**.

<p align="center">
<img src="https://github.com/user-attachments/assets/31ddce83-4b50-4f87-a124-f3a72545396d" width="600px" />
</p>



