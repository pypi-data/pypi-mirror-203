import pytest


class TestMain:
    def test_launcher(self):
        from w2w_ecs_autopublish_dummy import launcher
        launcher()

    def test_launcher_with_wrong_arguments(self):
        from w2w_ecs_autopublish_dummy import launcher
        with pytest.raises(TypeError):
            launcher("What")
