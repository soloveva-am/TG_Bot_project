from aiogram.utils.helper import Helper, HelperMode, ListItem
class TestStates(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1_REGISTER = ListItem()
    TEST_STATE_2_REGISTER_PASSWORD = ListItem()
    TEST_STATE_3_REGISTER_GROUP = ListItem()
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()