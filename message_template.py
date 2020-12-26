def main_menu():
    template = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "size": "micro",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "N2單字",
                        "data": "N2"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "N3單字",
                        "data": "N3"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "N4單字",
                        "data": "N4"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "N5單字",
                        "data": "N5"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "我的收藏",
                        "data": "favorite"
                    }
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "測驗",
                        "data": "test"
                    }
                }
            ]
        }
    }
    return template


def contentInput(level, japan, spell, tune, chinese, index, next_state, num=5, delete=False):
    template = {
        "type": "carousel",
        "contents": []
    }
    if not delete:
        for i in range(num):
            template["contents"].append({
                "type": "bubble",
                "size": "kilo",
                "direction": "ltr",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "級數 : " + level[i],
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "bottom"
                        },
                        {
                            "type": "text",
                            "text": "日文 : " + japan[i],
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center",
                            "margin": "none"
                        },
                        {
                            "type": "text",
                            "text": "假名 : " + spell[i],
                            "size": "md",
                            "color": "#ffffff"
                        },
                        {
                            "type": "text",
                            "text": "重音 : " + tune[i],
                            "size": "md",
                            "color": "#ffffff"
                        },
                        {
                            "type": "text",
                            "text": "中文 : " + chinese[i],
                            "size": "md",
                            "color": "#ffffff"
                        }
                    ],
                    "backgroundColor": "#27ACB2",
                    "paddingTop": "19px",
                    "paddingAll": "12px",
                    "paddingBottom": "16px",
                    "width": "100%"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": 'postback',
                                        "label": '加入收藏',
                                        "data": 'a' + str(index[i]) + level[i]
                                    }
                                }
                            ],
                            "flex": 1
                        }
                    ],
                    "spacing": "md",
                    "paddingAll": "12px"
                },
                "styles": {
                    "header": {
                        "separator": False
                    },
                    "footer": {
                        "separator": False
                    }
                }
            },

            )
    else:
        for i in range(num):
            template["contents"].append({
                "type": "bubble",
                "size": "kilo",
                "direction": "ltr",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "級數 : " + level[i],
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "bottom"
                        },
                        {
                            "type": "text",
                            "text": "日文 : " + japan[i],
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center",
                            "margin": "none"
                        },
                        {
                            "type": "text",
                            "text": "假名 : " + spell[i],
                            "size": "md",
                            "color": "#ffffff"
                        },
                        {
                            "type": "text",
                            "text": "重音 : " + tune[i],
                            "size": "md",
                            "color": "#ffffff"
                        },
                        {
                            "type": "text",
                            "text": "中文 : " + chinese[i],
                            "size": "md",
                            "color": "#ffffff"
                        }
                    ],
                    "backgroundColor": "#27ACB2",
                    "paddingTop": "19px",
                    "paddingAll": "12px",
                    "paddingBottom": "16px",
                    "width": "100%"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": 'postback',
                                        "label": '移除收藏',
                                        "data": 'd' + str(index[i]) + level[i]
                                    }
                                }
                            ],
                            "flex": 1
                        }
                    ],
                    "spacing": "md",
                    "paddingAll": "12px"
                },
                "styles": {
                    "header": {
                        "separator": False
                    },
                    "footer": {
                        "separator": False
                    }
                }
            }, )

    template["contents"].append({
        "type": "bubble",
        "size": "kilo",
        "direction": "ltr",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "繼續",
                        "data": next_state
                    },
                    "flex": 1,
                    "gravity": "bottom",
                    "height": "md",
                    "position": "relative",
                    "margin": "none"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "回主選單",
                        "data": "return_main"
                    },
                    "flex": 1
                }
            ]
        },
        "styles": {
            "footer": {
                "separator": False
            }
        }
    })

    return template


def test_type_choose():
    template = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "選擇測驗項目 : "
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "讀音",
                                "data": "spell"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "中文意思",
                                "data": "chinese"
                            }
                        }
                    ]
                }
            ]
        }
    }
    return template


def test_level_choose(question_type):
    template = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "選擇級數 : "
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "N2",
                                "data": question_type + "N2"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "N3",
                                "data": question_type + "N3"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "N4",
                                "data": question_type + "N4"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "N5",
                                "data": question_type + "N5"
                            }
                        }
                    ]
                }
            ]
        }
    }
    return template


def test_spell_option(level, japan, spell_option, tune, chinese, index, answer):
    template = {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "級數 : " + level,
                            "size": "md"
                        },
                        {
                            "type": "text",
                            "text": "日文 :" + japan,
                            "size": "md"
                        },
                        {
                            "type": "text",
                            "text": "重音 : " + tune,
                            "size": "md"
                        },
                        {
                            "type": "text",
                            "text": "中文 : " + chinese,
                            "size": "md"
                        }
                    ],
                    "alignItems": "flex-start",
                    "paddingAll": "none",
                    "offsetEnd": "xxl",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "margin": "none",
                    "position": "relative",
                    "spacing": "none"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": spell_option[0],
                                "data": 'squestion' + answer[0] + str(index) + level
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": spell_option[1],
                                "data": 'squestion' + answer[1] + str(index) + level
                            }
                        }
                    ],
                    "spacing": "md"
                }
            ]
        },
        "action": {
            "type": "message",
            "text": "test",
            "label": "test"
        }
    }
    return template


def test_chinese_option(level, japan, spell, tune, chinese_option, index, answer):
    template = {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "級數 : " + level,
                            "size": "md"
                        },
                        {
                            "type": "text",
                            "text": "假名 : " + spell,
                            "size": "md"
                        },
                        {
                            "type": "text",
                            "text": "重音 : " + tune,
                            "size": "md"
                        }
                    ],
                    "alignItems": "flex-start",
                    "paddingAll": "none",
                    "offsetEnd": "xxl",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "margin": "none",
                    "position": "relative",
                    "spacing": "none"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": chinese_option[0],
                                "data": 'cquestion' + answer[0] + str(index) + level
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": chinese_option[1],
                                "data": 'cquestion' + answer[1] + str(index) + level
                            }
                        }
                    ],
                    "spacing": "md"
                }
            ]
        },
        "action": {
            "type": "message",
            "text": "test",
            "label": "test"
        }
    }
    return template


def test_spell_answer_result(level, index, spell):
    template = {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "答案 : " + spell,
                            "size": "md"
                        }
                    ],
                    "alignItems": "flex-start",
                    "paddingAll": "none",
                    "offsetEnd": "xxl",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "margin": "none",
                    "position": "relative",
                    "spacing": "none"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "加入收藏",
                                "data": 'ta' + str(index) + level
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "下一題",
                                "data": "nextspell" + level
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "結束測驗",
                                "data": "return_main"
                            }
                        }
                    ],
                    "spacing": "md",
                    "action": {
                        "type": "message",
                        "label": "action",
                        "text": "hello"
                    }
                }
            ]
        },
        "action": {
            "type": "message",
            "text": "test",
            "label": "test"
        }
    }
    return template


def test_chinese_answer_result(level, index, chinese):
    template = {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "答案 : " + chinese,
                            "size": "md"
                        }
                    ],
                    "alignItems": "flex-start",
                    "paddingAll": "none",
                    "offsetEnd": "xxl",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "margin": "none",
                    "position": "relative",
                    "spacing": "none"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "加入收藏",
                                "data": 'ta' + str(index) + level
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "下一題",
                                "data": "nextchinese" + level
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "結束測驗",
                                "data": "return_main"
                            }
                        }
                    ],
                    "spacing": "md",
                    "action": {
                        "type": "message",
                        "label": "action",
                        "text": "hello"
                    }
                }
            ]
        },
        "action": {
            "type": "message",
            "text": "test",
            "label": "test"
        }
    }
    return template


def after_mail():
    template = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "傳送完成",
                    "align": "center"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "回主選單",
                        "data": "return_main"
                    }
                }
            ]
        }
    }
    return template


def no_favorite():
    template = {
        "type": "carousel",
        "contents": []
    }
    template["contents"].append(
        {
            "type": "bubble",
            "size": "kilo",
            "direction": "ltr",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "收藏為空",
                        "align": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "回主選單",
                            "data": "return_main"
                        },
                        "flex": 1
                    }
                ]
            },
            "styles": {
                "footer": {
                    "separator": False
                }
            }
        })
    return template
