from collections import OrderedDict, namedtuple
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


def dict_to_string(input_dict: dict, separator=" - ") -> str:
    """

    :param input_dict:
    :param separator:
    :return:
    """
    combined_list = list()
    for key, value in input_dict.items():
        combined_list.append(
            f"{value.tag}"
        ) if value.tag_data == "NONE" else combined_list.append(
            f"{colored(value.tag, value.tag_color)} : {colored(value.tag_data, value.tag_data_color)}"
        )
    return separator.join(combined_list)


class Dynamic:
    def __init__(self, title: str = "Py-OneLiner"):
        self._d_data = OrderedDict()
        self._title = title

    def _d_data_reset(self):
        """
        Reset the print data
        :return:
        """
        self._d_data = OrderedDict()

    def _refresh_tag(
        self, tag: str, tag_data: str, tag_color: str, tag_data_color: str
    ):
        """
        Update the value associated with the tag

        :param tag:
        :param tag_data:
        :return:
        """
        colored_print = namedtuple(
            "Data", ["tag", "tag_data", "tag_color", "tag_data_color"]
        )
        self._d_data[tag] = colored_print(tag, tag_data, tag_color, tag_data_color)

    def _filter_d_data_for_nested_loop(self, tag: str) -> OrderedDict:
        """
        In case of nested loop filter the data, so completed nested loop are removed from the console
        and print data just till 'tag'
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

    def one_line(
        self,
        tag,
        tag_data=None,
        tag_color="grey",
        tag_data_color="grey",
        to_reset_data: bool = False,
        to_new_line_data: bool = False,
        print_now: bool = True,
    ):
        """

        :param tag:
        :param tag_data:
        :param tag_color:
        :param tag_data_color:
        :param to_reset_data: will reset the print string
        :param to_new_line_data: to switch to new line after this 'tag'
        :param print_now: whether to print at the current tag, if False, the 'tag' and 'tag_data' will be updated and
        print when print_now will be true
        :return:
        """

        if tag_data is None:
            tag_data = "NONE"

        if tag_color is None and tag_data_color is not None:
            tag_color = "grey"

        if tag_color is not None and tag_data_color is None:
            tag_data_color = "grey"

        if to_reset_data:
            self._d_data_reset()

        self._d_data = (
            self._filter_d_data_for_nested_loop(tag)
            if (len(self._d_data) > 1 and tag in self._d_data)
            else self._d_data
        )

        self._refresh_tag(
            tag, tag_data, tag_color, tag_data_color
        )

        if print_now:
            if to_new_line_data:
                d_print_new_line(f"{self._title} : {dict_to_string(self._d_data)}")
            else:
                d_print(f"{self._title} : {dict_to_string(self._d_data)}")
