## 用于BeamNG车辆配置菜单的汉化

汉化对应配件全部写进字典了 `config.py`    

* 单独把车包解压出来，`根目录\content\vehicles`这里就是你所有官方车的配置文件
* 然后运行`delete.py`把多余的图片文件模型文件删掉，只保留`.jbeam`文件
* 然后运行`main.py`把字典内的汉化对照替换进`.jbeam`文件里
* 最后把替换好的文件压缩成`.zip`文件，然后把`.zip`文件放到mod/repo下
* 汉化完成；如果要汉化mod车，操作方法一样，需要手动把配件标识符对照的字符串添加到字典内`config.py`
* 或者手动打开mod内的`.jbeam`文件。找到对应的配件和子配件名称，修改成中文即可

单纯汉化不需要此工具  
请假如QQ群：`781038950` 下载汉化包即可