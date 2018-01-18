# -*- coding:utf-8 -*-
# @Time   : 2018/1/18 19:36
from src.handle_string import HandleString


class CaptureSignal():
    def __int__(self):
        pass

    def get_signal_info(self, file_name, signal_index):
        """
        :param file_name:无人机信号文件名
        :param signal_index: 待输出的信号序号
        :return:将要输出的提示字符串
        """
        if signal_index < 0 or signal_index > self._get_file_lines(file_name):
            return self._print_no_signal(signal_index)
        with open(file_name) as fd:
            index = 0
            # id 为无人机的id
            # location 为当前无人机的位置
            id = None
            location = None
            for line in fd:
                list_ = HandleString.split_str(line.replace("\n", ""))
                list_2int = HandleString.str2int(list_[1:])
                # 当这个为文件的第一行时候，经过分割的长度应该为4
                # 当这个为文件的第N行时候，经过分割的长度应该为7 N>1
                if index == 0:
                    if len(list_) == 4 and HandleString.vaild_id(list_[0]) and list_2int != None:
                        id = list_[0]
                        location = HandleString.str2int(list_[1:])
                    else:
                        fd.close()
                        return self._print_wrong_signal(signal_index)
                else:
                    if len(list_) == 7 and list_[0] == id and list_2int != None:
                        if self._is_right_location(location, list_2int[0:3]):
                            location = list(map(lambda x, y: x + y, location, list_2int[3:]))
                        else:
                            fd.close()
                            return self._print_wrong_signal(signal_index)
                    else:
                        fd.close()
                        return self._print_wrong_signal(signal_index)
                if index == signal_index:
                    fd.close()
                    return self._print_right_signal(id, signal_index, location)
                index = index + 1
        fd.close()
        return self._print_no_signal(signal_index)

    def _get_file_lines(self, file_name):
        """
        :param file_name: 文件名
        :return: 计算文件行数
        """
        count = 0
        with open(file_name, "r", encoding='utf-8') as fp:
            while 1:
                buffer = fp.read(8 * 1024 * 1024)
                if not buffer:
                    break
                count += buffer.count('\n')
            fp.close()
        return count

    def _is_right_location(self, pre_location, now_location):
        """
        :param pre_location:根据前一条信息计算出来的位置
        :param now_location:根据当前信息得到的位置信息
        :return:相等返回True
        """
        return True if pre_location == now_location else False

    def _print_no_signal(self, signal_index):
        """
        :param signal_index:
        :return:打印没发现信号的错误
        """
        info = "cannot find " + str(signal_index)
        return info

    def _print_right_signal(self, id, signal_index, location):
        """
        :param id: 无人机ID
        :param signal_index:消息序列号
        :param location: 此时无人机位置
        :return: 打印正常无人机信号
        """

        info = [id, str(signal_index), str(location[0]), str(location[1]), str(location[2])]

        return " ".join(info)

    def _print_wrong_signal(self, signal_index):
        """
        :param signal_index:消息序列号
        :return: 打印故障无人机信号
        """
        info = "Error:" + str(signal_index)
        return info
