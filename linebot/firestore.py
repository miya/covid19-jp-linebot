from collections import Counter
import firebase_admin
from firebase_admin import firestore


firebase_admin.initialize_app()
db = firestore.client()
col_ref = db.collection("data")

n = "now"
b = "before"


def get_update():
    """
    Returns
    -------
    アップデート時間: str
    """
    return col_ref.document(n).get().to_dict()["detail"]["update"]


def get_total_cases():
    """
    Returns
    -------
    全国の現在の総感染者数: int
    """
    return col_ref.document(n).get().to_dict()["total"]["total_cases"]


def get_before_total_cases():
    """
    Returns
    -------
    全国の前日の総感染者数: int
    """
    return col_ref.document(b).get().to_dict()["total"]["total_cases"]


def get_total_deaths():
    """
    Returns
    -------
    全国の現在の総死亡者数: int
    """
    return col_ref.document(n).get().to_dict()["total"]["total_deaths"]


def get_before_total_deaths():
    """
    Returns
    -------
    全国の前日の総死亡者数の取得: int
    """
    return col_ref.document(b).get().to_dict()["total"]["total_deaths"]


def get_pref_cases(pref_name):
    """
    Parameters
    ----------
    pref_name: str
        都道府県名

    Returns
    -------
    対象の現在の総感染者数: int
    """
    return col_ref.document(n).get().to_dict()["prefectures"][pref_name]["cases"]


def get_before_pref_cases(pref_name):
    """
    Parameters
    ----------
    pref_name: str
        都道府県名

    Returns
    -------
    対象の前日の総感染者数: int
    """
    return col_ref.document(b).get().to_dict()["prefectures"][pref_name]["cases"]


def get_pref_deaths(pref_name):
    """
    Parameters
    ----------
    pref_name: str
        都道府県名

    Returns
    -------
    対象の現在の総死亡者数: int
    """
    return col_ref.document(n).get().to_dict()["prefectures"][pref_name]["deaths"]


def get_before_pref_deaths(pref_name):
    """
    Parameters
    ----------
    pref_name: str
        都道府県名

    Returns
    -------
    対象の前日の総死亡者数: int
    """
    return col_ref.document(b).get().to_dict()["prefectures"][pref_name]["deaths"]


def get_total_pcr():
    """
    Returns
    -------
    全国のpcr検査数: int
    """
    return col_ref.document(n).get().to_dict()["total"]["total_pcr"]


def get_before_total_pcr():
    """
    Returns
    -------
    全国の前日のpcr検査数: int

    """
    return col_ref.document(b).get().to_dict()["total"]["total_pcr"]


def get_pref_pcr(pref_name):
    """
    Parameters
    ----------
    pref_name: str
        都道府県名

    Returns
    -------
    対象都市の現在のpcr検査数

    """
    return col_ref.document(n).get().to_dict()["prefectures"][pref_name]["pcr"]


def get_before_pref_pcr(pref_name):
    """
    Parameters
    ----------
    pref_name: str
        都道府県名

    Returns
    -------
    対象都市の前日のpcr検査数
    """
    return col_ref.document(b).get().to_dict()["prefectures"][pref_name]["pcr"]


def get_top_pref():
    """
    Returns
    -------
    全国 + 現在の感染者数上位12都市: list
    """
    pref_data = {}
    pref = col_ref.document(n).get().to_dict()["prefectures"]
    [pref_data.update({i: pref[i]["cases"]}) for i in pref]
    sorted_list = [i for i, j in Counter(pref_data).most_common()][:12]
    sorted_list.insert(0, "全国")
    return sorted_list
