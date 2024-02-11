import email
import re
from email.message import Message

from dataclasses import dataclass
from typing import TextIO, Optional, cast
from bs4 import BeautifulSoup
from bs4.element import Tag


@dataclass
class Wine:
    name: str
    vintage: str


def get_wine_name(td_tag: Tag) -> str:
    bold_tag = cast(Optional[Tag], td_tag.find("b"))
    if bold_tag is not None:
        content = str(bold_tag.contents[0])
    else:
        content = str(td_tag.contents[0])
    split_content = re.split(r"\(([^)]*)\)[^(]*$", content)
    wine_name = split_content[0]
    return wine_name.strip()


def get_wine_vintage(td_tag: Tag) -> str:
    return str(td_tag.contents[0]).strip()


def extract_html_payload(email_file: TextIO) -> str:
    # Find HTML Message
    b = email.message_from_file(email_file)
    parts: list[Message] = b.get_payload()
    html_message: Message | None = None
    for part in parts:
        headers = part.items()
        for header, value in headers:
            if header == "Content-Type" and "text/html" in value:
                html_message = part

    if html_message is None:
        return ""

    return cast(str, html_message.get_payload(decode=True))


def load_wines_from_email(email_file: TextIO) -> list[Wine]:
    # Find HTML Message
    html = extract_html_payload(email_file)
    soup = BeautifulSoup(html)

    wine_table = soup.find(
        lambda tag: tag.name == "th" and "Vintage" in tag.contents
    ).parent.parent  # type: ignore
    table_data_rows = wine_table.select("tr:has(td)")  # type: ignore
    wine_data = []
    for row in table_data_rows:
        table_data_cells = row.find_all("td")
        name_cell = table_data_cells[1]
        vintage_cell = table_data_cells[0]
        wine = Wine(
            name=get_wine_name(name_cell), vintage=get_wine_vintage(vintage_cell)
        )
        wine_data.append(wine)

    return wine_data
