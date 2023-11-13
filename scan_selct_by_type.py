import os
import magic  # 用于识别文件类型
import chardet  # 用于检测文件编码


# 判断一个字符串是否为回文串
def is_palindrome(s):
    return s == s[::-1]


# 1. 扫描e盘中的所有文件
def scan_directory(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

# 2. 识别文件类型
def identify_file_type(file_path):
    mime = magic.Magic()
    file_type = mime.from_file(file_path)
    return file_type

# 3. 将不同格式的文件保存到不同的文件中
def save_files_by_type(file_list, output_dir):
    file_types = {
        'DICOM': [],
        'HL7': [],
        'CDA': [],
        'FHIR': [],
        'JSON': [],
        'text': [],
        'pdf': [],
        'word': [],
        'excel': [],
        'xml': []
    }

    for file_path in file_list:
        file_type = identify_file_type(file_path)

        if 'DICOM' in file_type:
            file_types['DICOM'].append(file_path)
        elif 'HL7' in file_type:
            file_types['HL7'].append(file_path)
        elif 'CDA' in file_type:
            file_types['CDA'].append(file_path)
        elif 'FHIR' in file_type or 'json' in file_type:
            file_types['FHIR'].append(file_path)
        elif 'json' in file_type:
            file_types['JSON'].append(file_path)
        elif 'text' in file_type:
            file_types['text'].append(file_path)
        elif 'pdf' in file_type:
            file_types['pdf'].append(file_path)
        elif 'word' in file_type:
            file_types['word'].append(file_path)
        elif 'excel' in file_type:
            file_types['excel'].append(file_path)
        elif 'xml' in file_type:
            file_types['xml'].append(file_path)

    for file_type, file_paths in file_types.items():
        if file_paths:
            output_file = os.path.join(output_dir, file_type + "_files.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                for file_path in file_paths:
                    try:
                        file_path = file_path.encode('utf-8', 'ignore').decode('utf-8')
                        f.write(file_path + '\n')
                    except Exception as e:
                        print(f"Error writing file path: {e}")

if __name__ == '__main__':
    e_drive_path = "E:\\"  # 修改为您的E盘路径
    output_directory = "output_directory1"  # 修改为保存文件路径

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    file_list = scan_directory(e_drive_path)
    save_files_by_type(file_list, output_directory)
