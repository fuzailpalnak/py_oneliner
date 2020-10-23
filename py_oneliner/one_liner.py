from collections import OrderedDict
from sys import stdout
from termcolor import colored


def d_print(data: str):
    """

    :param data:
    :return:
    """
    stdout.write("\r\033[1;37m>>\x1b[K" + data.__str__())
    stdout.flush()


def d_print_new_line(data: str):
    """

    :param data:
    :return:
    """
    stdout.write("\n")
    d_print(data)


def dict_to_string(input_dict: dict, separator=", ") -> str:
    """

    :param input_dict:
    :param separator:
    :return:
    """
    combined_list = list()
    for key, value in input_dict.items():
        combined_list.append(f"{key}") if value[
            5:-4
        ] == "NONE" else combined_list.append(f"{key} : {value}")
    return separator.join(combined_list)


class Dynamic:
    def __init__(self, title: str = "Dynamic"):
        self._d_data = OrderedDict()
        self._title = title

    def _d_data_refresh(self):
        self._d_data = OrderedDict()

    def _refresh_value(self, tag: str, tag_data: str):
        """

        :param tag:
        :param tag_data:
        :return:
        """
        self._d_data[tag] = tag_data

    def _filter_d_data(self, tag: str) -> OrderedDict:
        """

        :param tag:
        :return:
        """
        filter_data = OrderedDict()
        filtered_keys = list(self._d_data.keys())[
            : list(self._d_data.keys()).index(tag)
        ]
        for tag in filtered_keys:
            filter_data[tag] = self._d_data[tag]
        return filter_data

    def print(
        self,
        tag,
        tag_data="NONE",
        tag_color: str = "red",
        tag_data_color: str = "red",
        is_refresh_data_at: bool = False,
        is_new_line_data_at: bool = False,
        print_now: bool = True
    ):
        """

        :param tag:
        :param tag_data:
        :param tag_color:
        :param tag_data_color:
        :param is_refresh_data_at:
        :param is_new_line_data_at:
        :param print_now:
        :return:
        """

        if is_refresh_data_at:
            self._d_data_refresh()

        self._d_data = (
            self._filter_d_data(tag)
            if (len(self._d_data) > 1 and tag in self._d_data)
            else self._d_data
        )
        self._refresh_value(colored(tag, tag_color), colored(tag_data, tag_data_color))

        if print_now:
            if is_new_line_data_at:
                d_print_new_line(f"{self._title} : {dict_to_string(self._d_data)}")
            else:
                d_print(f"{self._title} : {dict_to_string(self._d_data)}")
