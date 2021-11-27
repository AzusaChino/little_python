import curses
import time

stdscr = curses.initscr()
curses.noecho()
stdscr.addstr(1, 2, "HelloGitHub")
# 新建窗口，高为 5 宽为 25，在命令行窗口的 四行六列处
new_win = curses.newwin(5, 25, 4, 6)
# 使用阻塞等待模式
new_win.nodelay(False)
# 在新窗口的 2 行 3 列处添加文字
new_win.addstr(2, 3, "www.HelloGitHub.com")
# 给新窗口添加边框，其中边框符号可以这是，这里使用默认字符
new_win.border()
# 刷新窗口
stdscr.refresh()
# 等待字符输入（这里会一直等待输入）
new_win.getch()
# 删除新窗口对象
del new_win
# 清除所有内容（比 erase 更彻底）
stdscr.clear()
# 重新添加文字
stdscr.addstr(1, 2, "HelloGitHub")
# 刷新窗口
stdscr.refresh()
# 等待两秒钟
time.sleep(2)
# 结束 curses 模式，恢复到正常命令行模式
curses.endwin()
