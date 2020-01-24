# ROS_repo_robosys
ROSを用いて，タクトスイッチを押すとLEDが点灯するプログラムを作成．
myled.pyのプログラムが，サブスクライバー
パブリッシャー(button.py)側から，タクトスイッチのON,OFFの信号をサブスクライバ(myled.py)へ渡し，LEDが点灯する． <br/>

実行方法は，下記のコマンドを入力. <br/>
roslaunch myled myled.launch

<メッセージ内容と動作内容> <br/>
  0 -> LED_OFF <br/>
  1 -> LED_ON <br/>


YouTube(デモ動画)のリンク <br/>
https://youtu.be/ZiUk0CSw4l0
<br/>

参考にしたwebサイト・書籍は下記の通りのです．
* https://ryuichiueda.github.io/robosys2019/lesson13.html#/8
* http://make.bcde.jp/raspberry-pi/gpio%E3%81%A7led%E3%81%AE%E7%82%B9%E6%BB%85python/
* https://qiita.com/MENDY/items/0089b0f52acf23b7d3f1
* ROSではじめるロボットプログラム， 小倉崇， 工学社， 2015
