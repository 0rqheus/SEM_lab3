import os
from get_file_stats import get_file_stats

def get_all_file_paths_from_folder(folder_path, extention):
    paths = []
    files = os.listdir(folder_path)
    for f in files:
        file_path = folder_path + '/' + f
        if os.path.isdir(file_path):
            paths = paths + get_all_file_paths_from_folder(file_path, extention)
        elif f.endswith(extention):
            paths.append(file_path)
    return paths

def main():
    folder = 'D:/Downloads/stable-diffusion-webui-master'
    extention = '.py'

    physical_lines = 0
    code_lines = 0
    empty_lines = 0
    logical_lines = 0
    comment_lines = 0
    comment_level = 0

    files = get_all_file_paths_from_folder(folder, extention)
    for f in files:
        print(f)
        stats = get_file_stats(f)
        code_lines += stats['code_lines']
        empty_lines += stats['empty_lines']
        physical_lines += stats['physical_lines']
        logical_lines += stats['logical_lines']
        comment_lines += stats['comment_lines']
        comment_level = max(stats['comment_level'], comment_level)
    
    print('Physical lines:', physical_lines)
    print('Code lines:', code_lines)
    print('Logical lines:', logical_lines)
    print('Empty lines:', empty_lines)
    print('Comment lines:', comment_lines)
    print('Comment level:', comment_level)

main()