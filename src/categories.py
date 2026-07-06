CATEGORY_MAP = {

    # Movies
    "ersent": "Movies",
    "blywcm": "Movies",
    "blyflx": "Movies",
    "blygld": "Movies",
    "b4umov": "Movies",
    "altmov": "Movies",
    "mahply": "Movies",
    "p_runact": "Movies",

    # Music
    "yrfmus": "Music",
    "9xjalw": "Music",
    "run9xm": "Music",
    "sagmus": "Music",
    "saghar": "Music",

    # Sports
    "amuspo": "Sports",
    "xtrspo": "Sports",
    "criusa": "Sports",
    "mmaatv": "Sports",

    # Kids
    "lookid": "Kids",
    "carcar": "Kids",

    # News
    "abp_news": "News",
    "abpmaj": "News",
    "abpasm": "News",
    "abpana": "News",
    "tv9bha": "News",
    "tv9mar": "News",
    "tv9tel": "News",
    "tv9news9": "News",
    "newnat": "News",
    "india_tv_news": "News",
    "n18ind": "News",
    "n18cnn": "News",
}


def get_category(channel_id: str) -> str:
    return CATEGORY_MAP.get(channel_id, "Entertainment")