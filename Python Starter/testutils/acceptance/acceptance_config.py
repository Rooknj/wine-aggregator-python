from pydantic import BaseSettings


class SvcSettings(BaseSettings):
    # Config is logged -- do not store secrets here!
    genos_url: str = "http://localhost:8000"
    # genstudio = dict(
    #     use_genos=True,
    #     env="e2e",
    #     model_name="gpt-3.5-turbo",
    #     temperature=0,
    # )
    # idps_policy_id: str = ""
    # idps_endpoint: str = ""
    # idps_aws_profile: str = "genos-plugin"
    # qbo_endpoint: str = "localhost:8081"


class AcceptanceSettings(SvcSettings):
    genos_url: str = "https://localhost:8443"


def get_settings() -> SvcSettings:
    import os

    env = os.environ.get("APP_ENV", "local")
    if env == "local":
        return SvcSettings()
    elif env == "acceptance":
        return AcceptanceSettings()
    else:
        raise ValueError(f"Unknown environment: {env}")
