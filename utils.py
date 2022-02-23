from aiogram.utils.helper import Helper, HelperMode, ListItem
class TestStates(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1_register = ListItem()
    TEST_STATE_2_register_password = ListItem()
    TEST_STATE_3_register_group = ListItem()
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()