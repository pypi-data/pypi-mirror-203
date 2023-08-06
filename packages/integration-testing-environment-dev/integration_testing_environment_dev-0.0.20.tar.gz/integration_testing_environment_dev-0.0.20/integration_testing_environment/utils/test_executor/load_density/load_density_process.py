import json
import sys

from integration_testing_environment.extend.mail_thunder_extend.mail_thunder_setting import send_after_test
from integration_testing_environment.utils.exception.exception_tags import wrong_test_data_format_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITETestExecutorException
from integration_testing_environment.utils.file_process.get_dir_file_list import ask_and_get_dir_files_as_list
from integration_testing_environment.utils.test_executor.task_process_manager import TaskProcessManager


def call_load_density_test(test_format_code: str, program_buffer: int = 1024000):
    try:
        TaskProcessManager(
            "je_load_density",
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_load_density",
            exec_str=test_format_code,
        )
    except json.decoder.JSONDecodeError as error:
        print(
            repr(error) +
            "\n"
            + wrong_test_data_format_exception_tag,
            file=sys.stderr
        )
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def call_load_density_test_with_send(test_format_code: str, program_buffer: int = 1024000):
    try:
        TaskProcessManager(
            title_name="je_load_density",
            task_done_trigger_function=send_after_test,
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_load_density",
            exec_str=test_format_code,
        )
    except json.decoder.JSONDecodeError as error:
        print(
            repr(error) +
            "\n"
            + wrong_test_data_format_exception_tag,
            file=sys.stderr
        )
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def call_load_density_test_multi_file(program_buffer: int = 1024000):
    try:
        need_to_execute_list: list = ask_and_get_dir_files_as_list()
        if need_to_execute_list is not None and isinstance(need_to_execute_list, list) and len(need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_load_density_test(test_script_json.read(), program_buffer)
    except Exception as error:
        print(repr(error), file=sys.stderr)


def call_load_density_test_multi_file_and_send(program_buffer: int = 1024000):
    try:
        need_to_execute_list: list = ask_and_get_dir_files_as_list()
        if need_to_execute_list is not None and isinstance(need_to_execute_list, list) and len(need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_load_density_test_with_send(test_script_json.read(), program_buffer)
    except Exception as error:
        print(repr(error), file=sys.stderr)
