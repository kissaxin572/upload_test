import os

def scan_and_save_files_by_type(starting_directory, output_directory):
    """
    扫描指定目录中所有文件，并按照文件类型保存到指定目录中。

    参数：
    starting_directory (str): 起始目录的路径。
    output_directory (str): 输出目录的路径。

    返回：
    无

    """

    for root, directories, files in os.walk(starting_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_extension = file_name.split('.')[-1].lower()  # 获取文件扩展名并转为小写
            output_file = None

            if file_extension in ["doc", "docx"]:
                output_file = os.path.join(output_directory, "word_files.txt")
            elif file_extension in ["xls", "xlsx"]:
                output_file = os.path.join(output_directory, "excel_files.txt")
            elif file_extension == "xml":
                output_file = os.path.join(output_directory, "xml_files.txt")
            elif file_extension == "pdf":
                output_file = os.path.join(output_directory, "pdf_files.txt")
            elif file_extension == "txt":
                output_file = os.path.join(output_directory, "txt_files.txt")
            elif file_extension == "dicom":
                output_file = os.path.join(output_directory, "dicom_files.txt")
            elif file_extension == "hl7":
                output_file = os.path.join(output_directory, "hl7_files.txt")
            elif file_extension == "cda":
                output_file = os.path.join(output_directory, "cda_files.txt") 
            elif file_extension == "fhir":
                output_file = os.path.join(output_directory, "fhir_files.txt")
            elif file_extension == "json":
                output_file = os.path.join(output_directory, "json_files.txt")
            elif file_extension == "csv":
                output_file = os.path.join(output_directory, "csv_files.txt")          

            if output_file:
                try:
                    with open(output_file, 'a', encoding='utf-8') as output:
                        output.write(file_path + "\n")
                except UnicodeEncodeError:
                    pass
# 指定E盘为起始目录
starting_directory = "E:\\"

# 指定保存不同类型文件路径的输出目录
output_directory = "output_directory"

# 创建输出目录（如果不存在）
os.makedirs(output_directory, exist_ok=True)

scan_and_save_files_by_type(starting_directory, output_directory)
