class GlobalConfig:
    @staticmethod
    def tusi_art_base_url():
        return "https://api.tusiart.cn/community-web/v1"

    @staticmethod
    def tusi_art_get_model_detail_url():
        return GlobalConfig.tusi_art_base_url() + "/model/detail"