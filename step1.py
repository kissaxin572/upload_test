import os

def scan_and_save_files(starting_directory, output_file):
    """
    os.walk 的返回值是一个生成器(generator),也就是说我们需要用循环不断的遍历它（不可以直接print），来获得所有的内容。
    每次遍历的对象都是返回的是一个三元元组(root,dirs,files)
    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    """
    
    with open(output_file, 'w', encoding='utf-8') as output:
        for root, directories, files in os.walk(starting_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    # 将文件路径和文件名写入文档
                    output.write(file_path + "\n")
                except UnicodeEncodeError:
                    # 处理编码问题，忽略无法编码的文件名
                    pass

# 指定E盘为起始目录，并指定要保存的文件路径
starting_directory = "E:\\"
output_file = "file_paths.txt"

scan_and_save_files(starting_directory, output_file)
