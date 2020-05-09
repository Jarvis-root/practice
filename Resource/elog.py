import logging
import time
import os
import sys

log_path = r'D:\PycharmProjects\Practice\Report'


class TestLog:
    """
    日志记录模块
    """
    def __init__(self):

        t = time.strftime('%Y-%m-%d-%M-%S')
        self.logname = os.path.join(log_path, '{}.log'.format(t))  # 文件的命名
        self.logger = logging.getLogger()   # 创建日志记录器
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式：
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(msg)s')

    def _get_log(self, level, msg):
        """

        :return:
        """
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)  # 设置日志打印的格式
        self.logger.addHandler(fh)  # 将Handler添加到logger中

        # 创建一个StreamHandler,用于输出到控制台
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.formatter)
        self.logger.addHandler(sh)

        if level == 'info' or 'INFO':
            self.logger.info(msg)
        elif level == 'debug' or 'DEBUG':
            self.logger.debug(msg)
        elif level == 'warning' or 'WARNING':
            self.logger.warning(msg)
        elif level == 'error' or 'ERROR':
            self.logger.error(msg)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        fh.close()  # 关闭打开的文件

    def debug(self, msg):
        self._get_log('debug', msg)

    def info(self, msg):
        self._get_log('info', msg)

    def warning(self, msg):
        self._get_log('warning', msg)

    def error(self, msg):
        self._get_log('error', msg)


log = TestLog()

aw_LogDebug = log.debug
aw_LogInfo = log.info
aw_LogWarning = log.warning
aw_LogError = log.error


if __name__ == "__main__":
    log = TestLog()
    log.info("---测试开始----")
    log.info("输入密码")
    log.warning("----测试----")
