import os

# ディレクトリサイズを取得する関数を定義
def get_dir_size(path):
    total=0
    with os.scandir(path) as dir_paths:
        for object in dir_paths:
            # print(object.name)  #.name でファイル名を取り出し
            
            # ファイルならばファイルサイズを取得
            if object.is_file(follow_symlinks=False):  # シンボリックリンクは無視
                total += object.stat().st_size

            # ディレクトリならばパスを get_dir_size関数に渡してファイルサイズを取得
            elif object.is_dir(follow_symlinks=False):  # シンボリックリンクは無視
                total += get_dir_size(object.path)

    return total

# パスを入力 (パス前後の引用符(")があれば削除)
input_path = input("サイズ調査するパスを入力: ").replace('"','')

# 表示
print(round(get_dir_size(input_path)/1000000000, 2), "GB")  #round関数は偶数への丸めである事に留意