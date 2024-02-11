from app.email_loader import load_wines_from_email


def test_should_get_wine_names_from_email() -> None:
    with open("Insider's Advantage.eml") as fp:
        wines = load_wines_from_email(fp)
    assert wines[0].name == "¿Como No? Stag's Leap District Petite Sirah"


def test_should_get_wine_vintages_from_email() -> None:
    with open("Insider's Advantage.eml") as fp:
        wines = load_wines_from_email(fp)
    assert wines[0].vintage == "2017"


def test_should_get_null_wine_vintages_from_email() -> None:
    with open("Insider's Advantage.eml") as fp:
        wines = load_wines_from_email(fp)
    assert wines[11].vintage == ""
