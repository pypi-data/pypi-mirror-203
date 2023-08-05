import requests
import datetime


def validate_date(date):
    if date:
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except:
            raise ValueError(
                f"Date format '{date}' not valid. Please enter a valid format."
            )
    return datetime.date.today().strftime("%Y-%m-%d")


def request_get_with_timeout(url: str, timeout_time: float = 5):
    try:
        r = requests.get(url, timeout=timeout_time)
        if r.status_code == 200:
            return r
        r.raise_for_status()
    except requests.exceptions.Timeout:
        raise requests.exceptions.Timeout(
            f"No response from url after {timeout_time} seconds."
        )


def all_news(start: str = "", end: str = "", timeout_time: float = 5) -> list:
    start = validate_date(start)
    end = validate_date(end)

    url_plantao_b3 = f"https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/ListarTitulosNoticias?agencia=18&palavra=&dataInicial={start}&dataFinal={end}"
    r = request_get_with_timeout(url_plantao_b3, timeout_time=timeout_time)
    return [new["NwsMsg"] for new in r.json()]


def search_new(
    string: str, start: str = "", end: str = "", timeout_time: float = 5
) -> list:
    start = validate_date(start)
    end = validate_date(end)
    _all_news = all_news(start=start, end=end, timeout_time=timeout_time)
    return [new for new in _all_news if string in new["headline"]]


def get_new(new: dict) -> list:
    id_new = new["id"]
    id_agencia = new["IdAgencia"]
    date_time = new["dateTime"]
    new_url = f"https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/Detail?idNoticia={id_new}&agencia={id_agencia}&dataNoticia={date_time}"
    r = request_get_with_timeout(new_url)
    return r.text
