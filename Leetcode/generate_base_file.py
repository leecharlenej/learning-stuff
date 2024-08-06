#--------------------------------------------------------
# Fill this in
# -------------------------------------------------------
difficulty_level = 'easy'
function_name = 'mySqrt'
test_cases_num = 2
var_list = ['x']

#--------------------------------------------------------
# To get largest count.
# -------------------------------------------------------
import os

def get_largest_prefix(directory):
    files = os.listdir(directory)
    largest_num = 0

    for file in files:
        if file.endswith('.py'):
            prefix = file.split('_')[0]

            try:
                prefix_num = int(prefix)
                if prefix_num > largest_num:
                    largest_num = prefix_num
            except ValueError:
                pass
    return largest_num

count = get_largest_prefix('Leetcode') + 1

#--------------------------------------------------------
# Script starts here
# -------------------------------------------------------

count_str = str(count) if len(str(count)) > 1 else '0' + str(count)
folder_name = 'Leetcode'
file_name = f'{count_str}_{difficulty_level}_{function_name}.py'
file_path = os.path.join(folder_name, file_name)

file_content = f"""
        return

if __name__ == "__main__":
"""

for i in range(0,test_cases_num):
    file_content += f"    {var_list[0]}{i} = ''\n"

for i in range(0,test_cases_num):
    file_content += f"    print(Solution().{function_name}({var_list[0]}{i}))\n"

with open(file_path,'w') as f:
    f.write(file_content)
