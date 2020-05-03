import template
import firestore
from linebot.models import (FlexSendMessage, QuickReply, QuickReplyButton, MessageAction)


def main_message(pref_name):
    update = firestore.get_update() + " 更新"

    if pref_name == "全国":
        pref_name = "日本国内"
        cases = firestore.get_total_cases()
        deaths = firestore.get_total_deaths()
        before_cases = firestore.get_before_total_cases()
        before_deaths = firestore.get_before_total_deaths()
        pcr = firestore.get_total_pcr()
        before_pcr = firestore.get_before_total_pcr()
        output_msg = "【日本国内】\n感染者数: {} / 死亡者数: {}".format(cases, deaths)
    else:
        cases = firestore.get_pref_cases(pref_name)
        deaths = firestore.get_pref_deaths(pref_name)
        before_cases = firestore.get_before_pref_cases(pref_name)
        before_deaths = firestore.get_before_pref_deaths(pref_name)
        pcr = firestore.get_pref_pcr(pref_name)
        before_pcr = firestore.get_before_pref_pcr(pref_name)
        output_msg = "【{}】\n感染者数: {} / 死亡者数: {}".format(pref_name, cases, deaths)

    if cases >= before_cases:
        cases_ratio = "+" + str(cases - before_cases)
    else:
        cases_ratio = "-" + str(before_cases - cases)

    deaths_ratio = "+" + str(deaths - before_deaths)

    if pcr >= before_pcr:
        pcr_ratio = "+" + str(pcr - before_pcr)
    else:
        pcr_ratio = "-" + str(before_pcr - pcr)

    data_dic = {
        "update": update,
        "pref_name": pref_name,
        "cases": str(cases),
        "cases_ratio": cases_ratio,
        "deaths": str(deaths),
        "deaths_ratio": deaths_ratio,
        "pcr": str(pcr),
        "pcr_ratio": pcr_ratio
    }

    flex_message = template.main_message_template(data_dic)
    items = [QuickReplyButton(action=MessageAction(text=item, label=item)) for item in firestore.get_top_pref()]
    return FlexSendMessage(alt_text=output_msg, contents=flex_message, quick_reply=QuickReply(items=items))


def others_message(input_msg):
    items = [QuickReplyButton(action=MessageAction(text=item, label=item)) for item in firestore.get_top_pref()]

    if input_msg == "支援":
        output_msg = "支援"
        content = template.donate_message_template
    elif input_msg == "ヘルプ":
        output_msg = "ヘルプ"
        content = template.help_message_template
    else:
        output_msg = "入力された値が間違っています。"
        content = template.failure_message_template

    return FlexSendMessage(alt_text=output_msg, contents=content, quick_reply=QuickReply(items=items))
