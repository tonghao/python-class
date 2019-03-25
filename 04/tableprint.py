def table_print(list):
    ```
    输入list:字符串列表
    打印为右对齐表格

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

    ```
    pass


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

    table_print(tableData)