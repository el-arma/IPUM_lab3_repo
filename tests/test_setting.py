from settings import Settings


def try_settings(env):
    s = Settings(ENVIRONMENT=env)

    assert s.ENVIRONMENT == "test"
    assert s.APP_NAME == "my_app"


def test_settings_loaded(monkeypatch):
    # Mock load_secrets to avoid subprocess in test
    monkeypatch.setattr(
        Settings, "load_secrets", lambda self, file_path="secrets.yaml": None
    )
