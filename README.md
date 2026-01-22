# Farm Simulator for Multimedia Exercise

このプロジェクトは、マルチメディア演習の最終課題としてPython3およびPyGameを利用して作成したシンプルな農業シミュレーションゲームです。

## 内容

ゲーム画面は以下のようになっています。

<img width="1282" height="752" alt="image" src="https://github.com/user-attachments/assets/61a3871b-8aac-4dac-90d8-e919e9cacfe4" />

### 情報

左上に現在の日数や資源の情報が表示されています。このうち、金が10万になるようにするのがこのゲームの最終目的になります。

### 畑

茶色の部分が畑となっており、20 x 10のタイル状に配置されています。

このタイルをクリックすることで、スタミナを消費して、タイルに対してアクションを実行することができます。
このアクションは持っているツールとクリックしたタイルの状態によって異なり、

- 鍬 かつ 土 ![land](farm_sim_me/assets/land.png)
  
  耕された土に変化させる

- ジョウロ かつ 耕された土 ![tilled](farm_sim_me/assets/tilled.png)
  
  湿った土に変化させる

- 種 かつ 湿った土 ![hydrated](farm_sim_me/assets/hydrated.png)
  
  種を植える

- 鎌 かつ 成長しきった作物 ![crop-3](farm_sim_me/assets/crop-3.png)
  
  作物を収穫し、タイルを土に戻す

### ツール表示

一番右の列の最上部に現在持っているツールが表示されており、右クリックすることで切り替えることができます。

鍬 ![hoe](farm_sim_me/assets/tools/hoe.png) → ジョウロ ![watering](farm_sim_me/assets/tools/watering.png) → 種 ![seed](farm_sim_me/assets/tools/seed.png) → 鎌 ![scythe](farm_sim_me/assets/tools/scythe.png)

というように切り替わります。

### アクション

ツール表示画面の下には、各種アクションを実行できるボタンが配置されています。

- 小麦を売却 ![store_sell](farm_sim_me/assets/store_sell.png)

  小麦をすべて売却します。小麦1つにつき30G入手できます。

- 種を購入 ![store_buy](farm_sim_me/assets/store_buy.png)

  種を購入します。種1つにつき10G消費します。  
  1度の購入数は初期が10、最大スタミナが500以上で100、5000以上で1000となります。

- スタミナ強化 ![upgrade_stamina](farm_sim_me/assets/upgrade_stamina.png)

  小麦を消費して最大スタミナを強化します。
  1度の強化量は初期が10、最大スタミナが500以上で100、5000以上で1000となります。

- 睡眠でスタミナ回復 ![sleep](farm_sim_me/assets/sleep.png)

  睡眠することでスタミナを最大値まで回復させます。日数が増加します。

## 実行方法

1. 以下のコマンドを利用してリポジトリをクローン、もしくはZIPファイルとして入手し、展開します。

    ```sh
    git clone https://github.com/Keinsleif/farm_sim_me
    ```

2. 入手したフォルダ内に入ります。

    ```sh
    cd farm_sim_me
    ```

3. 依存関係をインストールします。

    ```sh
    pip install .
    ```

    or

    ```sh
    pip install pygame-ce
    ```

    or

   ```sh
   pip install pygame
   ```

5. モジュールをスクリプトとして実行するか、main.pyを実行します。

    ```sh
    python -m farm_sim_me
    ```

    or

    ```sh
    python main.py
    ```

> [!NOTE]
> uvを利用している場合は、3以降の手順を以下のように置き換えます。
> ```sh
> uv run -m farm_sim_me
> ```
>
> or
>
> ```sh
> uv run main.py
> ```
