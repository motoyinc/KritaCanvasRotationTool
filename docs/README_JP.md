<h1 align="center">🌀 Krita キャンバス回転ツール</h1>

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



## ✨ 機能紹介

* 🎯 **マイクロ回転**
  0.1°〜5.0° の小さなステップでキャンバスを回転。

<p align="center">
<img src="https://github.com/user-attachments/assets/0833f353-807e-4098-a4c1-504cf7856f69" width="400px" />
</p>

* 🌀 **スナップ付きの大きな回転**
  キャンバスを固定角度（15°、30°、45°など）にスナップ。スムーズなアニメーションにも対応。

<p align="center">
<img src="https://github.com/user-attachments/assets/7a4435da-0ec6-40e2-b3ad-f55cdefc60d6" width="400px" />
</p>

* ⚙️ **回転ステップのカスタマイズ**
  `Rotation Setting` ダイアログから、マイクロ回転・スナップ回転のステップを個別に設定可能です。

<p align="center">
<img src="https://github.com/user-attachments/assets/5ebc084e-d438-433d-81d7-962f114055f1" width="200px" />
</p>

* 🎮 **ショートカットに最適化**
  デフォルトのキー割り当ては以下の通りです：

  ```
  Ctrl + 4 → マイクロ回転・反時計回り  
  Ctrl + 6 → マイクロ回転・時計回り  
  Alt  + 4 → スナップ回転・反時計回り  
  Alt  + 6 → スナップ回転・時計回り
  ```

* 🧩 **Krita メニューと統合**
  メニューから簡単にアクセスできます：
  `ツール > スクリプト > Krita Canva Rotation Tool`

<p align="center">
<img src="https://github.com/user-attachments/assets/d2daf112-5413-40d7-9b38-bbcef72780c8" width="600px" />
</p>

<br>
<br>
<br>



## 📦 インストール手順

### 手順 1：プラグインのダウンロード

> リポジトリの [Releases](https://github.com/motoyinc/RotateCanvasTool/releases) ページから `KritaCanvasRotationTool.zip` をダウンロードしてください。  
> ⚠️ **解凍しないでください**。zip ファイルのまま保持します。

<br>

### 手順 2：Krita に読み込む

> Krita を起動します  
> `ツール > スクリプト > Python プラグインをファイルから読み込む` を選択します  
> ダウンロードした `KritaCanvasRotationTool.zip` を選択します  
> 終了後、**Krita を再起動**します

<p align="center">
<img src="https://github.com/user-attachments/assets/a60bc45c-e12b-45db-9b85-34af944407e9" width="600px" />
</p>

### 手順 3：プラグインを有効化

> `設定 > Krita を設定 > Python プラグインマネージャー` を開きます  
> `Krita Canvas Rotation Tool` を探して、チェックを入れ ✅  
> OK を押して、**Krita をもう一度再起動**してください

<p align="center">
<img src="https://github.com/user-attachments/assets/74a96abb-4962-437a-a45f-53b1f60e55d3" width="600px" />
</p>

<br>
<br>
<br>


## 🛠️ 使い方

1. **Krita** を開き、上部メニューに移動します：
   **`ツール > スクリプト > Krita Canva Rotation Tool`**

   <p align="center">
   <img src="https://github.com/user-attachments/assets/8fd21413-6b49-4fb2-8bcf-c3df13a3916a" width="600px" />
   </p>

2. このメニューには、以下のような回転操作が含まれています：

   * **Rotation Setting**：設定ダイアログを開きます。以下の項目が調整可能：

     * **マイクロ回転ステップ**：小さな回転角度（例：0.1°〜5.0°）
     * **スナップ回転ステップ**：固定角度への回転（例：15°、30°など）

   <p align="center">
   <img src="https://github.com/user-attachments/assets/5ebc084e-d438-433d-81d7-962f114055f1" width="200px" />
   </p>

3. メニューには以下の回転コマンドもあります：

   * **Coarse Rotate Canvas + / -** → 大きなステップの回転（例：15°）
   * **Micro Rotate Canvas + / -** → 細かいステップでの回転

   <p align="center">
   <img src="https://github.com/user-attachments/assets/d2daf112-5413-40d7-9b38-bbcef72780c8" width="600px" />
   </p>

4. 以下のパスからショートカットキーを変更できます：
   **`設定 > Krita を設定 > キーボードショートカット`**

   <p align="center">
   <img src="https://github.com/user-attachments/assets/31ddce83-4b50-4f87-a124-f3a72545396d" width="600px" />
   </p>
