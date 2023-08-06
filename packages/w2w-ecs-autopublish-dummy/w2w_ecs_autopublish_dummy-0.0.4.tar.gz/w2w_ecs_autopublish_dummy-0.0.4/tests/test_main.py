import pytest


class TestMain:
    def test_main(self):
        from w2w_ecs_autopublish_dummy.main import main
        main()

    def test_main_wrong_arguments(self):
        from w2w_ecs_autopublish_dummy.main import main
        with pytest.raises(TypeError):
            main("What")
