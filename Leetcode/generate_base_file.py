count = 6
difficulty_level = 'easy'
function_name = 'strStr'

import os

count_str = str(count) if len(str(count)) > 1 else '0' + str(count)
folder_name = 'Leetcode'
file_name = f'{count_str}_{difficulty_level}_{function_name}.py'
file_path = os.path.join(folder_name, file_name)
file_content = f"""

if __name__ == "__main__":
    s1 = ''
    s2 = ''
    s3 = ''
    print(Solution().{function_name}(s1))
    print(Solution().{function_name}(s2))
    print(Solution().{function_name}(s3))
"""

with open(file_path,'w') as f:
    f.write(file_content)
